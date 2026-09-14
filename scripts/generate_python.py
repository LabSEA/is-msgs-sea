"""Generate and stage the Python protobuf modules reproducibly."""

import shutil
import tempfile
from importlib.resources import files
from pathlib import Path

from grpc_tools import protoc


def transform(source: str) -> str:
    return source.replace('import "is/msgs/', 'import "is_msgs/')


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    source_dir = root / "src" / "is" / "msgs"
    package_dir = root / "python" / "is_msgs"
    package_dir.mkdir(parents=True, exist_ok=True)

    protos = sorted(source_dir.glob("*.proto"))
    generated_names = {
        suffix
        for proto in protos
        for suffix in (f"{proto.stem}_pb2.py", f"{proto.stem}_pb2.pyi", proto.name)
    }
    for artifact in generated_names:
        (package_dir / artifact).unlink(missing_ok=True)

    with tempfile.TemporaryDirectory(prefix="is-msgs-codegen-") as temp:
        staging = Path(temp)
        transformed_dir = staging / "is_msgs"
        transformed_dir.mkdir()
        for proto in protos:
            (transformed_dir / proto.name).write_text(transform(proto.read_text()))

        grpc_include = files("grpc_tools") / "_proto"
        result = protoc.main(
            [
                "grpc_tools.protoc",
                f"--proto_path={staging}",
                f"--proto_path={grpc_include}",
                f"--python_out={root / 'python'}",
                f"--pyi_out={root / 'python'}",
                *[str(transformed_dir / proto.name) for proto in protos],
            ]
        )
        if result:
            return result

        for proto in protos:
            shutil.copy2(transformed_dir / proto.name, package_dir / proto.name)

    typed_marker = package_dir / "py.typed"
    if not typed_marker.exists():
        typed_marker.touch()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
