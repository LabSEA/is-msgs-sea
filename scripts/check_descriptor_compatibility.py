"""Verify that the current schemas are wire-compatible with v1.1.18."""

import subprocess
import tempfile
from importlib.resources import files
from pathlib import Path

from google.protobuf import descriptor_pb2
from grpc_tools import protoc

BASELINE = "v1.1.18"


def _git(root, *arguments):
    return subprocess.check_output(["git", "-C", str(root), *arguments], text=True)


def _compile(proto_root, protos, descriptor_path):
    grpc_include = files("grpc_tools") / "_proto"
    result = protoc.main(
        [
            "grpc_tools.protoc",
            f"--proto_path={proto_root}",
            f"--proto_path={grpc_include}",
            f"--descriptor_set_out={descriptor_path}",
            *[str(proto) for proto in protos],
        ]
    )
    if result:
        raise RuntimeError(f"protoc failed with exit code {result}")


def _messages(package, messages, parent=""):
    output = {}
    for message in messages:
        local_name = f"{parent}.{message.name}" if parent else message.name
        full_name = f"{package}.{local_name}"
        fields = {}
        for field in message.field:
            fields[field.name] = (
                field.number,
                field.type,
                field.type_name,
                field.label,
                field.oneof_index if field.HasField("oneof_index") else None,
            )
        output[full_name] = fields
        output.update(_messages(package, message.nested_type, local_name))
    return output


def _nested_enums(package, messages, parent=""):
    output = {}
    for message in messages:
        local_name = f"{parent}.{message.name}" if parent else message.name
        for enum in message.enum_type:
            output[f"{package}.{local_name}.{enum.name}"] = {
                value.name: value.number for value in enum.value
            }
        output.update(_nested_enums(package, message.nested_type, local_name))
    return output


def _surface(descriptor_path):
    descriptor_set = descriptor_pb2.FileDescriptorSet.FromString(descriptor_path.read_bytes())
    messages = {}
    enums = {}
    for proto in descriptor_set.file:
        if not proto.package.startswith("is."):
            continue
        messages.update(_messages(proto.package, proto.message_type))
        enums.update(_nested_enums(proto.package, proto.message_type))
        for enum in proto.enum_type:
            enums[f"{proto.package}.{enum.name}"] = {
                value.name: value.number for value in enum.value
            }
    return messages, enums


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    paths = _git(root, "ls-tree", "-r", "--name-only", BASELINE, "src/is/msgs").splitlines()
    proto_paths = [path for path in paths if path.endswith(".proto")]

    with tempfile.TemporaryDirectory(prefix="is-msgs-compat-") as temp:
        temp_root = Path(temp)
        baseline_root = temp_root / "baseline"
        for path in proto_paths:
            target = baseline_root / path.removeprefix("src/")
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(_git(root, "show", f"{BASELINE}:{path}"))

        baseline_descriptor = temp_root / "baseline.pb"
        current_descriptor = temp_root / "current.pb"
        _compile(
            baseline_root,
            [baseline_root / path.removeprefix("src/") for path in proto_paths],
            baseline_descriptor,
        )
        current_protos = sorted((root / "src" / "is" / "msgs").glob("*.proto"))
        _compile(root / "src", current_protos, current_descriptor)

        old_messages, old_enums = _surface(baseline_descriptor)
        new_messages, new_enums = _surface(current_descriptor)

    errors = []
    for name, old_fields in old_messages.items():
        current_fields = new_messages.get(name)
        if current_fields is None:
            errors.append(f"message removed: {name}")
            continue
        for field, signature in old_fields.items():
            if current_fields.get(field) != signature:
                errors.append(f"field changed: {name}.{field}")
    for name, old_values in old_enums.items():
        current_values = new_enums.get(name)
        if current_values is None:
            errors.append(f"enum removed: {name}")
            continue
        for value, number in old_values.items():
            if current_values.get(value) != number:
                errors.append(f"enum value changed: {name}.{value}")

    if errors:
        raise RuntimeError("Incompatible descriptor changes:\n" + "\n".join(errors))
    print(f"All {len(old_messages)} messages and {len(old_enums)} enums remain compatible")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
