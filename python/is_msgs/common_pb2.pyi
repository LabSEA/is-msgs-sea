from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DataType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN_TYPE: _ClassVar[DataType]
    FLOAT_TYPE: _ClassVar[DataType]
    DOUBLE_TYPE: _ClassVar[DataType]
    INT32_TYPE: _ClassVar[DataType]
    INT64_TYPE: _ClassVar[DataType]
UNKNOWN_TYPE: DataType
FLOAT_TYPE: DataType
DOUBLE_TYPE: DataType
INT32_TYPE: DataType
INT64_TYPE: DataType

class Header(_message.Message):
    __slots__ = ("stamp", "frame_id")
    STAMP_FIELD_NUMBER: _ClassVar[int]
    FRAME_ID_FIELD_NUMBER: _ClassVar[int]
    stamp: _timestamp_pb2.Timestamp
    frame_id: str
    def __init__(self, stamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., frame_id: _Optional[str] = ...) -> None: ...

class Vector3(_message.Message):
    __slots__ = ("x", "y", "z")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    z: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., z: _Optional[float] = ...) -> None: ...

class Quaternion(_message.Message):
    __slots__ = ("x", "y", "z", "w")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    W_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    z: float
    w: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., z: _Optional[float] = ..., w: _Optional[float] = ...) -> None: ...

class Twist(_message.Message):
    __slots__ = ("linear", "angular")
    LINEAR_FIELD_NUMBER: _ClassVar[int]
    ANGULAR_FIELD_NUMBER: _ClassVar[int]
    linear: Vector3
    angular: Vector3
    def __init__(self, linear: _Optional[_Union[Vector3, _Mapping]] = ..., angular: _Optional[_Union[Vector3, _Mapping]] = ...) -> None: ...

class Transform(_message.Message):
    __slots__ = ("translation", "rotation")
    TRANSLATION_FIELD_NUMBER: _ClassVar[int]
    ROTATION_FIELD_NUMBER: _ClassVar[int]
    translation: Vector3
    rotation: Quaternion
    def __init__(self, translation: _Optional[_Union[Vector3, _Mapping]] = ..., rotation: _Optional[_Union[Quaternion, _Mapping]] = ...) -> None: ...

class TransformStamped(_message.Message):
    __slots__ = ("header", "child_frame_id", "transform")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    CHILD_FRAME_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSFORM_FIELD_NUMBER: _ClassVar[int]
    header: Header
    child_frame_id: str
    transform: Transform
    def __init__(self, header: _Optional[_Union[Header, _Mapping]] = ..., child_frame_id: _Optional[str] = ..., transform: _Optional[_Union[Transform, _Mapping]] = ...) -> None: ...

class SamplingSettings(_message.Message):
    __slots__ = ("frequency", "delay")
    FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    DELAY_FIELD_NUMBER: _ClassVar[int]
    frequency: _wrappers_pb2.FloatValue
    delay: _wrappers_pb2.FloatValue
    def __init__(self, frequency: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]] = ..., delay: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]] = ...) -> None: ...

class SyncRequest(_message.Message):
    __slots__ = ("entities", "sampling")
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    SAMPLING_FIELD_NUMBER: _ClassVar[int]
    entities: _containers.RepeatedScalarFieldContainer[str]
    sampling: SamplingSettings
    def __init__(self, entities: _Optional[_Iterable[str]] = ..., sampling: _Optional[_Union[SamplingSettings, _Mapping]] = ...) -> None: ...

class FieldSelector(_message.Message):
    __slots__ = ("fields",)
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    fields: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, fields: _Optional[_Iterable[int]] = ...) -> None: ...

class Shape(_message.Message):
    __slots__ = ("dims",)
    class Dimension(_message.Message):
        __slots__ = ("size", "name")
        SIZE_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        size: int
        name: str
        def __init__(self, size: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...
    DIMS_FIELD_NUMBER: _ClassVar[int]
    dims: _containers.RepeatedCompositeFieldContainer[Shape.Dimension]
    def __init__(self, dims: _Optional[_Iterable[_Union[Shape.Dimension, _Mapping]]] = ...) -> None: ...

class Tensor(_message.Message):
    __slots__ = ("shape", "type", "floats", "doubles", "ints32", "ints64")
    SHAPE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    FLOATS_FIELD_NUMBER: _ClassVar[int]
    DOUBLES_FIELD_NUMBER: _ClassVar[int]
    INTS32_FIELD_NUMBER: _ClassVar[int]
    INTS64_FIELD_NUMBER: _ClassVar[int]
    shape: Shape
    type: DataType
    floats: _containers.RepeatedScalarFieldContainer[float]
    doubles: _containers.RepeatedScalarFieldContainer[float]
    ints32: _containers.RepeatedScalarFieldContainer[int]
    ints64: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, shape: _Optional[_Union[Shape, _Mapping]] = ..., type: _Optional[_Union[DataType, str]] = ..., floats: _Optional[_Iterable[float]] = ..., doubles: _Optional[_Iterable[float]] = ..., ints32: _Optional[_Iterable[int]] = ..., ints64: _Optional[_Iterable[int]] = ...) -> None: ...

class Position(_message.Message):
    __slots__ = ("x", "y", "z", "precise", "header")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    PRECISE_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    z: float
    precise: Vector3
    header: Header
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., z: _Optional[float] = ..., precise: _Optional[_Union[Vector3, _Mapping]] = ..., header: _Optional[_Union[Header, _Mapping]] = ...) -> None: ...

class Orientation(_message.Message):
    __slots__ = ("yaw", "pitch", "roll", "quaternion", "header")
    YAW_FIELD_NUMBER: _ClassVar[int]
    PITCH_FIELD_NUMBER: _ClassVar[int]
    ROLL_FIELD_NUMBER: _ClassVar[int]
    QUATERNION_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    yaw: float
    pitch: float
    roll: float
    quaternion: Quaternion
    header: Header
    def __init__(self, yaw: _Optional[float] = ..., pitch: _Optional[float] = ..., roll: _Optional[float] = ..., quaternion: _Optional[_Union[Quaternion, _Mapping]] = ..., header: _Optional[_Union[Header, _Mapping]] = ...) -> None: ...

class Pose(_message.Message):
    __slots__ = ("position", "orientation", "header")
    POSITION_FIELD_NUMBER: _ClassVar[int]
    ORIENTATION_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    position: Position
    orientation: Orientation
    header: Header
    def __init__(self, position: _Optional[_Union[Position, _Mapping]] = ..., orientation: _Optional[_Union[Orientation, _Mapping]] = ..., header: _Optional[_Union[Header, _Mapping]] = ...) -> None: ...

class Speed(_message.Message):
    __slots__ = ("linear", "angular", "twist", "header")
    LINEAR_FIELD_NUMBER: _ClassVar[int]
    ANGULAR_FIELD_NUMBER: _ClassVar[int]
    TWIST_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    linear: float
    angular: float
    twist: Twist
    header: Header
    def __init__(self, linear: _Optional[float] = ..., angular: _Optional[float] = ..., twist: _Optional[_Union[Twist, _Mapping]] = ..., header: _Optional[_Union[Header, _Mapping]] = ...) -> None: ...

class PoseWithCovariance(_message.Message):
    __slots__ = ("pose", "covariance")
    POSE_FIELD_NUMBER: _ClassVar[int]
    COVARIANCE_FIELD_NUMBER: _ClassVar[int]
    pose: Pose
    covariance: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, pose: _Optional[_Union[Pose, _Mapping]] = ..., covariance: _Optional[_Iterable[float]] = ...) -> None: ...

class SpeedWithCovariance(_message.Message):
    __slots__ = ("speed", "covariance")
    SPEED_FIELD_NUMBER: _ClassVar[int]
    COVARIANCE_FIELD_NUMBER: _ClassVar[int]
    speed: Speed
    covariance: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, speed: _Optional[_Union[Speed, _Mapping]] = ..., covariance: _Optional[_Iterable[float]] = ...) -> None: ...

class ConsumerInfo(_message.Message):
    __slots__ = ("consumers",)
    CONSUMERS_FIELD_NUMBER: _ClassVar[int]
    consumers: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, consumers: _Optional[_Iterable[str]] = ...) -> None: ...

class ConsumerList(_message.Message):
    __slots__ = ("info",)
    class InfoEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ConsumerInfo
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ConsumerInfo, _Mapping]] = ...) -> None: ...
    INFO_FIELD_NUMBER: _ClassVar[int]
    info: _containers.MessageMap[str, ConsumerInfo]
    def __init__(self, info: _Optional[_Mapping[str, ConsumerInfo]] = ...) -> None: ...

class Phrase(_message.Message):
    __slots__ = ("content", "confidence", "language")
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    content: _containers.RepeatedScalarFieldContainer[str]
    confidence: float
    language: str
    def __init__(self, content: _Optional[_Iterable[str]] = ..., confidence: _Optional[float] = ..., language: _Optional[str] = ...) -> None: ...
