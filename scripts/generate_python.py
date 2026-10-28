"""Generate Python artifacts in staging before replacing any packaged files."""

import os
import tempfile
from importlib.resources import files
from pathlib import Path

from is_msgs.utils.build import transform_imports
from schema_manifest import discover_schemas


def transform(source: str) -> str:
    return transform_imports(source)


def generate(root: Path) -> int:
    from grpc_tools import protoc

    protos = discover_schemas(root)
    package_dir = root / "python/is_msgs"
    # Use the destination filesystem so each os.replace is atomic.
    package_dir.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".is-msgs-codegen-", dir=package_dir.parent) as temp:
        staging = Path(temp)
        transformed_dir = staging / "is_msgs"
        transformed_dir.mkdir()
        for proto in protos:
            (transformed_dir / proto.name).write_text(
                transform(proto.read_text(encoding="utf-8")), encoding="utf-8"
            )
        result = protoc.main(
            [
                "grpc_tools.protoc",
                f"--proto_path={staging}",
                f"--proto_path={files('grpc_tools') / '_proto'}",
                f"--python_out={staging}",
                f"--pyi_out={staging}",
                *[str(transformed_dir / proto.name) for proto in protos],
            ]
        )
        if result:
            return result
        expected = {
            name
            for proto in protos
            for name in (proto.name, f"{proto.stem}_pb2.py", f"{proto.stem}_pb2.pyi")
        }
        for name in expected:
            if not (transformed_dir / name).is_file():
                raise RuntimeError(f"protoc did not produce {name}")
        package_dir.mkdir(exist_ok=True)
        stale = {
            path
            for pattern in ("*.proto", "*_pb2.py", "*_pb2.pyi")
            for path in package_dir.glob(pattern)
            if path.name not in expected
        }
        for name in sorted(expected):
            artifact, target = transformed_dir / name, package_dir / name
            if not target.exists() or target.read_bytes() != artifact.read_bytes():
                os.replace(artifact, target)
        for path in stale:
            path.unlink()
        (package_dir / "py.typed").touch(exist_ok=True)
    return 0


def main() -> int:
    return generate(Path(__file__).resolve().parents[1])


if __name__ == "__main__":
    raise SystemExit(main())
