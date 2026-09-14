"""Compile application protos that import schemas shipped by is-msgs-sea."""

import argparse
import os
import tempfile
from importlib.resources import files
from pathlib import Path

import is_msgs


def get_include() -> str:
    """Return the directory containing the installed ``is_msgs`` package."""
    return str(Path(is_msgs.__file__).resolve().parent.parent)


def _transform(source: str) -> str:
    return source.replace('import "is/msgs/', 'import "is_msgs/')


def compile_protos(proto_files, output=".") -> int:
    """Compile one or more proto files into *output* using pinned grpcio-tools."""
    try:
        from grpc_tools import protoc
    except ImportError as error:
        raise RuntimeError(
            "Protocol Buffer compilation requires 'is-msgs-sea[codegen]'"
        ) from error

    sources = [Path(proto).resolve() for proto in proto_files]
    for source in sources:
        if source.suffix != ".proto":
            raise ValueError(f"'{source}' is not a .proto file")
        if not source.is_file():
            raise FileNotFoundError(source)

    output_dir = Path(output).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    common_root = Path(os.path.commonpath([str(source.parent) for source in sources]))
    with tempfile.TemporaryDirectory(prefix="is-msgs-user-proto-") as temp:
        staging = Path(temp)
        transformed = []
        for source in sources:
            target = staging / source.relative_to(common_root)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(_transform(source.read_text()))
            transformed.append(target.relative_to(staging))

        grpc_include = files("grpc_tools") / "_proto"
        return protoc.main(
            [
                "grpc_tools.protoc",
                f"--proto_path={staging}",
                f"--proto_path={get_include()}",
                f"--proto_path={grpc_include}",
                f"--python_out={output_dir}",
                *[str(proto) for proto in transformed],
            ]
        )


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Compile protos importing canonical is/msgs schemas"
    )
    parser.add_argument("proto", nargs="+", help="proto files to compile")
    parser.add_argument("-o", "--output", default=".", help="generated module directory")
    arguments = parser.parse_args(argv)
    return compile_protos(arguments.proto, arguments.output)


if __name__ == "__main__":
    raise SystemExit(main())
