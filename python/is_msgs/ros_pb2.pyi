from google.protobuf import struct_pb2 as _struct_pb2
from is_msgs import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ROSMessage(_message.Message):
    __slots__ = ("type", "content")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    type: str
    content: _struct_pb2.Struct
    def __init__(self, type: _Optional[str] = ..., content: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class TFMessage(_message.Message):
    __slots__ = ("transforms",)
    TRANSFORMS_FIELD_NUMBER: _ClassVar[int]
    transforms: _containers.RepeatedCompositeFieldContainer[_common_pb2.TransformStamped]
    def __init__(self, transforms: _Optional[_Iterable[_Union[_common_pb2.TransformStamped, _Mapping]]] = ...) -> None: ...
