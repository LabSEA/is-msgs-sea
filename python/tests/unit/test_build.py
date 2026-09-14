import importlib.util

import pytest
from is_msgs.utils.build import compile_protos

pytest.importorskip("grpc_tools")


def test_compile_external_proto_with_canonical_import(tmp_path):
    source = tmp_path / "example.proto"
    source.write_text(
        'syntax = "proto3";\n'
        'import "is/msgs/common.proto";\n'
        'package example;\n'
        'message Located { is.common.Pose pose = 1; }\n'
    )
    output = tmp_path / "generated"

    assert compile_protos([source], output) == 0

    generated = output / "example_pb2.py"
    spec = importlib.util.spec_from_file_location("example_pb2", generated)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    assert module.Located.DESCRIPTOR.fields_by_name["pose"].message_type.full_name == (
        "is.common.Pose"
    )


def test_compile_preserves_application_import_layout(tmp_path):
    package = tmp_path / "application"
    package.mkdir()
    dependency = package / "types.proto"
    dependency.write_text(
        'syntax = "proto3";\npackage application;\nmessage Identifier { string value = 1; }\n'
    )
    service = package / "service.proto"
    service.write_text(
        'syntax = "proto3";\n'
        'import "types.proto";\n'
        'package application;\n'
        'message Request { Identifier id = 1; }\n'
    )
    output = tmp_path / "generated"

    assert compile_protos([dependency, service], output) == 0
    assert (output / "types_pb2.py").is_file()
    assert (output / "service_pb2.py").is_file()
