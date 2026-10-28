"""Check additive wire and generated API compatibility against a Git baseline.

Strict by design: removals are rejected even when reserved (major-version work).
Oneof order and explicit versus implicit default packing are not API changes.
"""

import argparse
import re
import subprocess
import tempfile
from dataclasses import dataclass, field
from importlib.resources import files
from pathlib import Path

from google.protobuf import descriptor_pb2 as dp
from schema_manifest import discover_schemas

BASELINE = "v1.1.18"


def _git(root, *arguments):
    return subprocess.check_output(["git", "-C", str(root), *arguments], text=True)


def release_baseline(root):
    """Select the newest reachable release, excluding the clean release under test."""
    version = (root / ".version").read_text(encoding="utf-8").strip()
    if not re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", version):
        raise ValueError(".version must contain MAJOR.MINOR.PATCH")
    candidate = tuple(map(int, version.split(".")))
    head = _git(root, "rev-parse", "HEAD").strip()
    schemas_changed = bool(
        _git(root, "status", "--porcelain", "--untracked-files=all", "--", "src/is/msgs")
    )
    releases = []
    for tag in _git(root, "tag", "--merged", "HEAD", "--list", "v*").splitlines():
        match = re.fullmatch(r"v([0-9]+)\.([0-9]+)\.([0-9]+)", tag)
        if not match:
            continue
        numbers = tuple(map(int, match.groups()))
        if numbers > candidate:
            continue
        if (
            numbers == candidate
            and _git(root, "rev-parse", f"{tag}^{{commit}}").strip() == head
            and not schemas_changed
        ):
            continue
        releases.append((numbers, tag))
    if not releases:
        raise RuntimeError(
            "No previous reachable release; fetch release tags or use --baseline-ref"
        )
    return max(releases)[1]


def _compile(proto_root, protos, descriptor_path):
    from grpc_tools import protoc

    result = protoc.main(
        [
            "grpc_tools.protoc",
            f"--proto_path={proto_root}",
            f"--proto_path={files('grpc_tools') / '_proto'}",
            f"--descriptor_set_out={descriptor_path}",
            *[str(proto) for proto in protos],
        ]
    )
    if result:
        raise RuntimeError(f"protoc failed with exit code {result}")


@dataclass
class Surface:
    files: dict = field(default_factory=dict)
    messages: dict = field(default_factory=dict)
    enums: dict = field(default_factory=dict)
    extensions: dict = field(default_factory=dict)
    services: dict = field(default_factory=dict)


def _surface(descriptor_set):
    surface = Surface()

    def visit(prefix, messages, proto):
        for message in messages:
            name = f"{prefix}.{message.name}".lstrip(".")
            surface.messages[name] = (message, proto.syntax or "proto2")
            for enum in message.enum_type:
                surface.enums[f"{name}.{enum.name}"] = enum
            for extension in message.extension:
                surface.extensions[f"{name}.{extension.name}"] = (extension, message, proto)
            visit(name, message.nested_type, proto)

    for proto in descriptor_set.file:
        # Include every owned file, regardless of its package; validate.proto
        # and files whose package was renamed must not silently disappear.
        if not proto.name.startswith(("is/msgs/", "is_msgs/")):
            continue
        surface.files[proto.name] = proto
        visit(proto.package, proto.message_type, proto)
        for enum in proto.enum_type:
            surface.enums[f"{proto.package}.{enum.name}".lstrip(".")] = enum
        for extension in proto.extension:
            surface.extensions[f"{proto.package}.{extension.name}".lstrip(".")] = (
                extension,
                None,
                proto,
            )
        for service in proto.service:
            surface.services[f"{proto.package}.{service.name}".lstrip(".")] = service
    return surface


def _oneof_name(field, message):
    if not field.HasField("oneof_index") or message is None or field.proto3_optional:
        return None
    return message.oneof_decl[field.oneof_index].name


def _field_signature(field, message, syntax):
    packable = field.type not in {
        dp.FieldDescriptorProto.TYPE_STRING,
        dp.FieldDescriptorProto.TYPE_BYTES,
        dp.FieldDescriptorProto.TYPE_MESSAGE,
        dp.FieldDescriptorProto.TYPE_GROUP,
    }
    packed = None
    if field.label == dp.FieldDescriptorProto.LABEL_REPEATED and packable:
        packed = field.options.packed if field.options.HasField("packed") else syntax == "proto3"
    return (
        field.number,
        field.type,
        field.type_name,
        field.label,
        field.extendee,
        _oneof_name(field, message),
        field.proto3_optional,
        field.json_name or _json_name(field.name),
        field.default_value if field.HasField("default_value") else None,
        packed,
        field.options.ctype,
        field.options.jstype,
    )


def _json_name(name):
    parts = name.split("_")
    return parts[0] + "".join(part[:1].upper() + part[1:] for part in parts[1:])


def _ranges_cover(old_ranges, new_ranges, *, inclusive=False):
    new = sorted((item.start, item.end + inclusive) for item in new_ranges)
    for old in old_ranges:
        cursor, end = old.start, old.end + inclusive
        for start, stop in new:
            if start > cursor:
                break
            if stop > cursor:
                cursor = stop
            if cursor >= end:
                break
        if cursor < end:
            return False
    return True


def _check_reservations(name, old, new, errors, *, enum=False):
    if not set(old.reserved_name) <= set(new.reserved_name):
        errors.append(f"reserved names removed: {name}")
    if not _ranges_cover(old.reserved_range, new.reserved_range, inclusive=enum):
        errors.append(f"reserved numbers removed: {name}")


def compare_descriptors(old_set, new_set):
    """Return actionable diagnostics; additions remain compatible by default."""
    old, new = _surface(old_set), _surface(new_set)
    if not old.files:
        raise ValueError("baseline contains no owned schema files")
    errors = []
    file_options = (
        "java_package",
        "java_outer_classname",
        "java_multiple_files",
        "optimize_for",
        "go_package",
        "cc_generic_services",
        "java_generic_services",
        "py_generic_services",
        "cc_enable_arenas",
        "objc_class_prefix",
        "csharp_namespace",
        "swift_prefix",
        "php_class_prefix",
        "php_namespace",
        "php_metadata_namespace",
        "ruby_package",
    )
    for name, previous in old.files.items():
        current = new.files.get(name)
        if current is None:
            errors.append(f"file removed: {name}")
            continue
        if (previous.package, previous.syntax or "proto2", previous.edition) != (
            current.package,
            current.syntax or "proto2",
            current.edition,
        ):
            errors.append(f"package, syntax or edition changed: {name}")
        for option in file_options:
            if getattr(previous.options, option) != getattr(current.options, option):
                errors.append(f"file option changed: {name}.{option}")
        public = {previous.dependency[index] for index in previous.public_dependency}
        now_public = {current.dependency[index] for index in current.public_dependency}
        if not public <= now_public:
            errors.append(f"public imports removed: {name}")

    for name, (previous, old_syntax) in old.messages.items():
        entry = new.messages.get(name)
        if entry is None:
            errors.append(f"message removed: {name}")
            continue
        current, new_syntax = entry
        if previous.options.map_entry != current.options.map_entry:
            errors.append(f"map entry changed: {name}")
        _check_reservations(name, previous, current, errors)
        if not _ranges_cover(previous.extension_range, current.extension_range):
            errors.append(f"extension ranges removed: {name}")
        fields = {item.name: item for item in current.field}
        old_fields = {item.name for item in previous.field}
        for item in previous.field:
            replacement = fields.get(item.name)
            if replacement is None or _field_signature(item, previous, old_syntax) != (
                _field_signature(replacement, current, new_syntax)
            ):
                errors.append(f"field changed or removed: {name}.{item.name} (tag {item.number})")
        for item in current.field:
            if (
                item.name not in old_fields
                and item.label == dp.FieldDescriptorProto.LABEL_REQUIRED
            ):
                errors.append(f"required field added: {name}.{item.name}")

        # Synthetic optional oneofs are an implementation detail, not public unions.
        def real_oneofs(message):
            synthetic = {item.oneof_index for item in message.field if item.proto3_optional}
            return {
                item.name
                for index, item in enumerate(message.oneof_decl)
                if index not in synthetic
            }

        if not real_oneofs(previous) <= real_oneofs(current):
            errors.append(f"oneof removed or renamed: {name}")

    for name, previous in old.enums.items():
        current = new.enums.get(name)
        if current is None:
            errors.append(f"enum removed: {name}")
            continue
        values = {item.name: item.number for item in current.value}
        for item in previous.value:
            if values.get(item.name) != item.number:
                errors.append(f"enum value changed or removed: {name}.{item.name}")
        if (
            previous.value
            and current.value
            and previous.value[0].number != current.value[0].number
        ):
            errors.append(f"enum default changed: {name}")
        _check_reservations(name, previous, current, errors, enum=True)

    for name, (previous, old_parent, old_file) in old.extensions.items():
        entry = new.extensions.get(name)
        if entry is None:
            errors.append(f"extension removed: {name}")
            continue
        current, new_parent, new_file = entry
        if _field_signature(previous, old_parent, old_file.syntax or "proto2") != (
            _field_signature(current, new_parent, new_file.syntax or "proto2")
        ):
            errors.append(f"extension changed: {name}")

    for name, previous in old.services.items():
        current = new.services.get(name)
        if current is None:
            errors.append(f"service removed: {name}")
            continue
        methods = {item.name: item for item in current.method}
        for item in previous.method:
            replacement = methods.get(item.name)

            def signature(method):
                return (
                    method.input_type,
                    method.output_type,
                    method.client_streaming,
                    method.server_streaming,
                )

            if replacement is None or signature(item) != signature(replacement):
                errors.append(f"service method changed or removed: {name}.{item.name}")
    return errors


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    baseline = parser.add_mutually_exclusive_group()
    baseline.add_argument("--baseline-ref", default=BASELINE)
    baseline.add_argument("--latest-release", action="store_true")
    arguments = parser.parse_args(argv)
    root = Path(__file__).resolve().parents[1]
    baseline_ref = release_baseline(root) if arguments.latest_release else arguments.baseline_ref
    paths = _git(
        root, "ls-tree", "-r", "--name-only", baseline_ref, "src/is/msgs"
    ).splitlines()
    proto_paths = [path for path in paths if path.endswith(".proto")]
    if not proto_paths:
        raise RuntimeError("baseline contains no schemas")
    with tempfile.TemporaryDirectory(prefix="is-msgs-compat-") as temp:
        temp_root = Path(temp)
        baseline_root = temp_root / "baseline"
        for path in proto_paths:
            target = baseline_root / path.removeprefix("src/")
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(
                _git(root, "show", f"{baseline_ref}:{path}"), encoding="utf-8"
            )
        baseline_descriptor, current_descriptor = temp_root / "old.pb", temp_root / "new.pb"
        _compile(
            baseline_root,
            [baseline_root / path.removeprefix("src/") for path in proto_paths],
            baseline_descriptor,
        )
        _compile(root / "src", discover_schemas(root), current_descriptor)
        old = dp.FileDescriptorSet.FromString(baseline_descriptor.read_bytes())
        new = dp.FileDescriptorSet.FromString(current_descriptor.read_bytes())
    errors = compare_descriptors(old, new)
    if errors:
        raise RuntimeError("Incompatible descriptor changes:\n" + "\n".join(errors))
    surface = _surface(old)
    print(
        f"Compatible with {baseline_ref}: {len(surface.messages)} messages, "
        f"{len(surface.enums)} enums, "
        f"{len(surface.extensions)} extensions, {len(surface.services)} services"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
