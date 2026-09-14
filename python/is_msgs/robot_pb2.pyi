from is_msgs import common_pb2 as _common_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PointFieldDataType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    POINT_FIELD_DATATYPE_UNSPECIFIED: _ClassVar[PointFieldDataType]
    POINT_FIELD_INT8: _ClassVar[PointFieldDataType]
    POINT_FIELD_UINT8: _ClassVar[PointFieldDataType]
    POINT_FIELD_INT16: _ClassVar[PointFieldDataType]
    POINT_FIELD_UINT16: _ClassVar[PointFieldDataType]
    POINT_FIELD_INT32: _ClassVar[PointFieldDataType]
    POINT_FIELD_UINT32: _ClassVar[PointFieldDataType]
    POINT_FIELD_FLOAT32: _ClassVar[PointFieldDataType]
    POINT_FIELD_FLOAT64: _ClassVar[PointFieldDataType]
POINT_FIELD_DATATYPE_UNSPECIFIED: PointFieldDataType
POINT_FIELD_INT8: PointFieldDataType
POINT_FIELD_UINT8: PointFieldDataType
POINT_FIELD_INT16: PointFieldDataType
POINT_FIELD_UINT16: PointFieldDataType
POINT_FIELD_INT32: PointFieldDataType
POINT_FIELD_UINT32: PointFieldDataType
POINT_FIELD_FLOAT32: PointFieldDataType
POINT_FIELD_FLOAT64: PointFieldDataType

class RangeScan(_message.Message):
    __slots__ = ("angles", "ranges", "header", "angle_min", "angle_max", "angle_increment", "time_increment", "scan_time", "range_min", "range_max", "intensities")
    ANGLES_FIELD_NUMBER: _ClassVar[int]
    RANGES_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ANGLE_MIN_FIELD_NUMBER: _ClassVar[int]
    ANGLE_MAX_FIELD_NUMBER: _ClassVar[int]
    ANGLE_INCREMENT_FIELD_NUMBER: _ClassVar[int]
    TIME_INCREMENT_FIELD_NUMBER: _ClassVar[int]
    SCAN_TIME_FIELD_NUMBER: _ClassVar[int]
    RANGE_MIN_FIELD_NUMBER: _ClassVar[int]
    RANGE_MAX_FIELD_NUMBER: _ClassVar[int]
    INTENSITIES_FIELD_NUMBER: _ClassVar[int]
    angles: _containers.RepeatedScalarFieldContainer[float]
    ranges: _containers.RepeatedScalarFieldContainer[float]
    header: _common_pb2.Header
    angle_min: float
    angle_max: float
    angle_increment: float
    time_increment: float
    scan_time: float
    range_min: float
    range_max: float
    intensities: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, angles: _Optional[_Iterable[float]] = ..., ranges: _Optional[_Iterable[float]] = ..., header: _Optional[_Union[_common_pb2.Header, _Mapping]] = ..., angle_min: _Optional[float] = ..., angle_max: _Optional[float] = ..., angle_increment: _Optional[float] = ..., time_increment: _Optional[float] = ..., scan_time: _Optional[float] = ..., range_min: _Optional[float] = ..., range_max: _Optional[float] = ..., intensities: _Optional[_Iterable[float]] = ...) -> None: ...

class Imu(_message.Message):
    __slots__ = ("header", "orientation", "orientation_covariance", "angular_velocity", "angular_velocity_covariance", "linear_acceleration", "linear_acceleration_covariance")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ORIENTATION_FIELD_NUMBER: _ClassVar[int]
    ORIENTATION_COVARIANCE_FIELD_NUMBER: _ClassVar[int]
    ANGULAR_VELOCITY_FIELD_NUMBER: _ClassVar[int]
    ANGULAR_VELOCITY_COVARIANCE_FIELD_NUMBER: _ClassVar[int]
    LINEAR_ACCELERATION_FIELD_NUMBER: _ClassVar[int]
    LINEAR_ACCELERATION_COVARIANCE_FIELD_NUMBER: _ClassVar[int]
    header: _common_pb2.Header
    orientation: _common_pb2.Quaternion
    orientation_covariance: _containers.RepeatedScalarFieldContainer[float]
    angular_velocity: _common_pb2.Vector3
    angular_velocity_covariance: _containers.RepeatedScalarFieldContainer[float]
    linear_acceleration: _common_pb2.Vector3
    linear_acceleration_covariance: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, header: _Optional[_Union[_common_pb2.Header, _Mapping]] = ..., orientation: _Optional[_Union[_common_pb2.Quaternion, _Mapping]] = ..., orientation_covariance: _Optional[_Iterable[float]] = ..., angular_velocity: _Optional[_Union[_common_pb2.Vector3, _Mapping]] = ..., angular_velocity_covariance: _Optional[_Iterable[float]] = ..., linear_acceleration: _Optional[_Union[_common_pb2.Vector3, _Mapping]] = ..., linear_acceleration_covariance: _Optional[_Iterable[float]] = ...) -> None: ...

class Odometry(_message.Message):
    __slots__ = ("header", "child_frame_id", "pose", "twist")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    CHILD_FRAME_ID_FIELD_NUMBER: _ClassVar[int]
    POSE_FIELD_NUMBER: _ClassVar[int]
    TWIST_FIELD_NUMBER: _ClassVar[int]
    header: _common_pb2.Header
    child_frame_id: str
    pose: _common_pb2.PoseWithCovariance
    twist: _common_pb2.SpeedWithCovariance
    def __init__(self, header: _Optional[_Union[_common_pb2.Header, _Mapping]] = ..., child_frame_id: _Optional[str] = ..., pose: _Optional[_Union[_common_pb2.PoseWithCovariance, _Mapping]] = ..., twist: _Optional[_Union[_common_pb2.SpeedWithCovariance, _Mapping]] = ...) -> None: ...

class PointField(_message.Message):
    __slots__ = ("name", "offset", "datatype", "count")
    NAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    DATATYPE_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    name: str
    offset: int
    datatype: PointFieldDataType
    count: int
    def __init__(self, name: _Optional[str] = ..., offset: _Optional[int] = ..., datatype: _Optional[_Union[PointFieldDataType, str]] = ..., count: _Optional[int] = ...) -> None: ...

class PointCloud(_message.Message):
    __slots__ = ("header", "height", "width", "fields", "is_bigendian", "point_step", "row_step", "data", "is_dense")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    IS_BIGENDIAN_FIELD_NUMBER: _ClassVar[int]
    POINT_STEP_FIELD_NUMBER: _ClassVar[int]
    ROW_STEP_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    IS_DENSE_FIELD_NUMBER: _ClassVar[int]
    header: _common_pb2.Header
    height: int
    width: int
    fields: _containers.RepeatedCompositeFieldContainer[PointField]
    is_bigendian: bool
    point_step: int
    row_step: int
    data: bytes
    is_dense: bool
    def __init__(self, header: _Optional[_Union[_common_pb2.Header, _Mapping]] = ..., height: _Optional[int] = ..., width: _Optional[int] = ..., fields: _Optional[_Iterable[_Union[PointField, _Mapping]]] = ..., is_bigendian: bool = ..., point_step: _Optional[int] = ..., row_step: _Optional[int] = ..., data: _Optional[bytes] = ..., is_dense: bool = ...) -> None: ...

class RobotConfig(_message.Message):
    __slots__ = ("speed",)
    SPEED_FIELD_NUMBER: _ClassVar[int]
    speed: _common_pb2.Speed
    def __init__(self, speed: _Optional[_Union[_common_pb2.Speed, _Mapping]] = ...) -> None: ...

class BasicMoveTask(_message.Message):
    __slots__ = ("positions", "speeds", "final_orientation", "allowed_error", "rate")
    POSITIONS_FIELD_NUMBER: _ClassVar[int]
    SPEEDS_FIELD_NUMBER: _ClassVar[int]
    FINAL_ORIENTATION_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_ERROR_FIELD_NUMBER: _ClassVar[int]
    RATE_FIELD_NUMBER: _ClassVar[int]
    positions: _containers.RepeatedCompositeFieldContainer[_common_pb2.Position]
    speeds: _containers.RepeatedCompositeFieldContainer[_common_pb2.Speed]
    final_orientation: _common_pb2.Orientation
    allowed_error: float
    rate: float
    def __init__(self, positions: _Optional[_Iterable[_Union[_common_pb2.Position, _Mapping]]] = ..., speeds: _Optional[_Iterable[_Union[_common_pb2.Speed, _Mapping]]] = ..., final_orientation: _Optional[_Union[_common_pb2.Orientation, _Mapping]] = ..., allowed_error: _Optional[float] = ..., rate: _Optional[float] = ...) -> None: ...

class RobotTaskRequest(_message.Message):
    __slots__ = ("id", "basic_move_task")
    ID_FIELD_NUMBER: _ClassVar[int]
    BASIC_MOVE_TASK_FIELD_NUMBER: _ClassVar[int]
    id: int
    basic_move_task: BasicMoveTask
    def __init__(self, id: _Optional[int] = ..., basic_move_task: _Optional[_Union[BasicMoveTask, _Mapping]] = ...) -> None: ...

class RobotTaskReply(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class RobotControllerProgress(_message.Message):
    __slots__ = ("id", "current_speed", "current_pose", "desired_pose", "error", "completion", "sources", "begin", "end")
    ID_FIELD_NUMBER: _ClassVar[int]
    CURRENT_SPEED_FIELD_NUMBER: _ClassVar[int]
    CURRENT_POSE_FIELD_NUMBER: _ClassVar[int]
    DESIRED_POSE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    COMPLETION_FIELD_NUMBER: _ClassVar[int]
    SOURCES_FIELD_NUMBER: _ClassVar[int]
    BEGIN_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    id: int
    current_speed: _common_pb2.Speed
    current_pose: _common_pb2.Pose
    desired_pose: _common_pb2.Pose
    error: float
    completion: float
    sources: _containers.RepeatedScalarFieldContainer[str]
    begin: _timestamp_pb2.Timestamp
    end: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[int] = ..., current_speed: _Optional[_Union[_common_pb2.Speed, _Mapping]] = ..., current_pose: _Optional[_Union[_common_pb2.Pose, _Mapping]] = ..., desired_pose: _Optional[_Union[_common_pb2.Pose, _Mapping]] = ..., error: _Optional[float] = ..., completion: _Optional[float] = ..., sources: _Optional[_Iterable[str]] = ..., begin: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class PathRequest(_message.Message):
    __slots__ = ("id", "destination_pose", "robot_gateway_id", "rate", "allowed_error")
    ID_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_POSE_FIELD_NUMBER: _ClassVar[int]
    ROBOT_GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    RATE_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_ERROR_FIELD_NUMBER: _ClassVar[int]
    id: int
    destination_pose: _common_pb2.Pose
    robot_gateway_id: int
    rate: float
    allowed_error: float
    def __init__(self, id: _Optional[int] = ..., destination_pose: _Optional[_Union[_common_pb2.Pose, _Mapping]] = ..., robot_gateway_id: _Optional[int] = ..., rate: _Optional[float] = ..., allowed_error: _Optional[float] = ...) -> None: ...
