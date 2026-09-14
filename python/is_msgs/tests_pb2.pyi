from is_msgs import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Foo(_message.Message):
    __slots__ = ("myint", "myfloat", "mydouble")
    MYINT_FIELD_NUMBER: _ClassVar[int]
    MYFLOAT_FIELD_NUMBER: _ClassVar[int]
    MYDOUBLE_FIELD_NUMBER: _ClassVar[int]
    myint: int
    myfloat: float
    mydouble: float
    def __init__(self, myint: _Optional[int] = ..., myfloat: _Optional[float] = ..., mydouble: _Optional[float] = ...) -> None: ...

class Bar(_message.Message):
    __slots__ = ("myfoo", "myfloat")
    MYFOO_FIELD_NUMBER: _ClassVar[int]
    MYFLOAT_FIELD_NUMBER: _ClassVar[int]
    myfoo: Foo
    myfloat: float
    def __init__(self, myfoo: _Optional[_Union[Foo, _Mapping]] = ..., myfloat: _Optional[float] = ...) -> None: ...

class Repeats(_message.Message):
    __slots__ = ("foos", "foo2", "int32s", "uint32s", "floats", "doubles", "int64s", "uint64s")
    FOOS_FIELD_NUMBER: _ClassVar[int]
    FOO2_FIELD_NUMBER: _ClassVar[int]
    INT32S_FIELD_NUMBER: _ClassVar[int]
    UINT32S_FIELD_NUMBER: _ClassVar[int]
    FLOATS_FIELD_NUMBER: _ClassVar[int]
    DOUBLES_FIELD_NUMBER: _ClassVar[int]
    INT64S_FIELD_NUMBER: _ClassVar[int]
    UINT64S_FIELD_NUMBER: _ClassVar[int]
    foos: _containers.RepeatedCompositeFieldContainer[Foo]
    foo2: Foo
    int32s: _containers.RepeatedScalarFieldContainer[int]
    uint32s: _containers.RepeatedScalarFieldContainer[int]
    floats: _containers.RepeatedScalarFieldContainer[float]
    doubles: _containers.RepeatedScalarFieldContainer[float]
    int64s: _containers.RepeatedScalarFieldContainer[int]
    uint64s: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, foos: _Optional[_Iterable[_Union[Foo, _Mapping]]] = ..., foo2: _Optional[_Union[Foo, _Mapping]] = ..., int32s: _Optional[_Iterable[int]] = ..., uint32s: _Optional[_Iterable[int]] = ..., floats: _Optional[_Iterable[float]] = ..., doubles: _Optional[_Iterable[float]] = ..., int64s: _Optional[_Iterable[int]] = ..., uint64s: _Optional[_Iterable[int]] = ...) -> None: ...
