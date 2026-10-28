from copy import deepcopy

import pytest
from google.protobuf import descriptor_pb2 as dp


def surface():
    descriptors = dp.FileDescriptorSet()
    proto = descriptors.file.add(
        name="is/msgs/example.proto", package="is.example", syntax="proto3"
    )
    message = proto.message_type.add(name="Sample")
    message.field.add(
        name="value",
        number=1,
        type=dp.FieldDescriptorProto.TYPE_INT32,
        label=dp.FieldDescriptorProto.LABEL_OPTIONAL,
    )
    message.oneof_decl.add(name="first")
    message.oneof_decl.add(name="second")
    message.field.add(
        name="choice",
        number=2,
        type=dp.FieldDescriptorProto.TYPE_STRING,
        label=dp.FieldDescriptorProto.LABEL_OPTIONAL,
        oneof_index=0,
    )
    message.nested_type.add(name="Nested").field.add(
        name="bytes",
        number=1,
        type=dp.FieldDescriptorProto.TYPE_BYTES,
        label=dp.FieldDescriptorProto.LABEL_OPTIONAL,
    )
    message.reserved_range.add(start=10, end=15)
    message.reserved_name.append("removed")
    enum = proto.enum_type.add(name="Kind")
    enum.value.add(name="UNKNOWN", number=0)
    enum.value.add(name="VALID", number=1)
    enum.reserved_range.add(start=8, end=10)
    proto.extension.add(
        name="rules",
        number=919191,
        type=dp.FieldDescriptorProto.TYPE_BOOL,
        label=dp.FieldDescriptorProto.LABEL_OPTIONAL,
        extendee=".google.protobuf.FieldOptions",
    )
    proto.service.add(name="Service").method.add(
        name="Call", input_type=".is.example.Sample", output_type=".is.example.Sample"
    )
    return descriptors


@pytest.mark.parametrize(
    "mutation,diagnostic",
    [
        (lambda p: setattr(p, "package", "other"), "package"),
        (lambda p: setattr(p, "syntax", "proto2"), "syntax"),
        (lambda p: setattr(p.message_type[0].field[0], "number", 9), "field"),
        (lambda p: setattr(p.message_type[0].field[0], "name", "renamed"), "field"),
        (
            lambda p: setattr(
                p.message_type[0].field[0], "type", dp.FieldDescriptorProto.TYPE_SINT32
            ),
            "field",
        ),
        (
            lambda p: setattr(
                p.message_type[0].field[0], "label", dp.FieldDescriptorProto.LABEL_REPEATED
            ),
            "field",
        ),
        (lambda p: setattr(p.message_type[0].field[0], "proto3_optional", True), "field"),
        (lambda p: setattr(p.message_type[0].field[0], "json_name", "custom"), "field"),
        (lambda p: setattr(p.message_type[0].oneof_decl[0], "name", "renamed"), "oneof"),
        (
            lambda p: setattr(p.message_type[0].nested_type[0].field[0], "number", 3),
            "Nested.bytes",
        ),
        (lambda p: setattr(p.message_type[0].options, "map_entry", True), "map entry"),
        (lambda p: p.message_type[0].ClearField("reserved_name"), "reserved names"),
        (lambda p: setattr(p.message_type[0].reserved_range[0], "end", 14), "reserved numbers"),
        (lambda p: p.ClearField("extension"), "extension removed"),
        (lambda p: setattr(p.extension[0], "number", 919192), "extension changed"),
        (
            lambda p: setattr(p.extension[0], "extendee", ".google.protobuf.MessageOptions"),
            "extension",
        ),
        (lambda p: setattr(p.enum_type[0].value[1], "number", 2), "enum value"),
        (lambda p: setattr(p.enum_type[0].reserved_range[0], "end", 9), "reserved numbers"),
        (lambda p: setattr(p.service[0].method[0], "server_streaming", True), "service method"),
        (lambda p: setattr(p.options, "java_package", "com.changed"), "file option"),
    ],
)
def test_breaking_changes_are_detected(script, mutation, diagnostic):
    checker = script("check_descriptor_compatibility")
    old = surface()
    new = deepcopy(old)
    mutation(new.file[0])
    assert any(diagnostic in error for error in checker.compare_descriptors(old, new))


def test_oneof_reordering_and_additive_fields_are_compatible(script):
    checker = script("check_descriptor_compatibility")
    old = surface()
    new = deepcopy(old)
    message = new.file[0].message_type[0]
    message.oneof_decl[0].name, message.oneof_decl[1].name = "second", "first"
    message.field[1].oneof_index = 1
    message.field.add(
        name="new",
        number=3,
        type=dp.FieldDescriptorProto.TYPE_STRING,
        label=dp.FieldDescriptorProto.LABEL_OPTIONAL,
    )
    message.reserved_range[0].end = 20
    assert checker.compare_descriptors(old, new) == []


def test_proto3_implicit_packing_equals_explicit_true(script):
    checker = script("check_descriptor_compatibility")
    old = surface()
    old.file[0].message_type[0].field[0].label = dp.FieldDescriptorProto.LABEL_REPEATED
    new = deepcopy(old)
    new.file[0].message_type[0].field[0].options.packed = True
    assert checker.compare_descriptors(old, new) == []
    new.file[0].message_type[0].field[0].options.packed = False
    assert checker.compare_descriptors(old, new)


def test_new_required_field_is_rejected_and_empty_baseline_is_error(script):
    checker = script("check_descriptor_compatibility")
    old = surface()
    new = deepcopy(old)
    new.file[0].message_type[0].field.add(
        name="required",
        number=3,
        type=dp.FieldDescriptorProto.TYPE_STRING,
        label=dp.FieldDescriptorProto.LABEL_REQUIRED,
    )
    assert any("required field added" in error for error in checker.compare_descriptors(old, new))
    with pytest.raises(ValueError, match="baseline"):
        checker.compare_descriptors(dp.FileDescriptorSet(), new)
