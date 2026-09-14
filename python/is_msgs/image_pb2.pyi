from google.protobuf import wrappers_pb2 as _wrappers_pb2
from is_msgs import validate_pb2 as _validate_pb2
from is_msgs import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TimestampSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TIMESTAMP_SOURCE_UNSPECIFIED: _ClassVar[TimestampSource]
    TIMESTAMP_SOURCE_CAMERA: _ClassVar[TimestampSource]
    TIMESTAMP_SOURCE_GATEWAY_RECEIVE: _ClassVar[TimestampSource]

class ImageFormats(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PNG: _ClassVar[ImageFormats]
    JPEG: _ClassVar[ImageFormats]
    WebP: _ClassVar[ImageFormats]

class ColorSpaces(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RGB: _ClassVar[ColorSpaces]
    GRAY: _ClassVar[ColorSpaces]
    YCbCr: _ClassVar[ColorSpaces]
    HSV: _ClassVar[ColorSpaces]

class HumanKeypoints(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN_HUMAN_KEYPOINT: _ClassVar[HumanKeypoints]
    HEAD: _ClassVar[HumanKeypoints]
    NOSE: _ClassVar[HumanKeypoints]
    NECK: _ClassVar[HumanKeypoints]
    RIGHT_SHOULDER: _ClassVar[HumanKeypoints]
    RIGHT_ELBOW: _ClassVar[HumanKeypoints]
    RIGHT_WRIST: _ClassVar[HumanKeypoints]
    LEFT_SHOULDER: _ClassVar[HumanKeypoints]
    LEFT_ELBOW: _ClassVar[HumanKeypoints]
    LEFT_WRIST: _ClassVar[HumanKeypoints]
    RIGHT_HIP: _ClassVar[HumanKeypoints]
    RIGHT_KNEE: _ClassVar[HumanKeypoints]
    RIGHT_ANKLE: _ClassVar[HumanKeypoints]
    LEFT_HIP: _ClassVar[HumanKeypoints]
    LEFT_KNEE: _ClassVar[HumanKeypoints]
    LEFT_ANKLE: _ClassVar[HumanKeypoints]
    RIGHT_EYE: _ClassVar[HumanKeypoints]
    LEFT_EYE: _ClassVar[HumanKeypoints]
    RIGHT_EAR: _ClassVar[HumanKeypoints]
    LEFT_EAR: _ClassVar[HumanKeypoints]
    CHEST: _ClassVar[HumanKeypoints]

class ObjectLabels(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN_OBJECT: _ClassVar[ObjectLabels]
    HUMAN_SKELETON: _ClassVar[ObjectLabels]
TIMESTAMP_SOURCE_UNSPECIFIED: TimestampSource
TIMESTAMP_SOURCE_CAMERA: TimestampSource
TIMESTAMP_SOURCE_GATEWAY_RECEIVE: TimestampSource
PNG: ImageFormats
JPEG: ImageFormats
WebP: ImageFormats
RGB: ColorSpaces
GRAY: ColorSpaces
YCbCr: ColorSpaces
HSV: ColorSpaces
UNKNOWN_HUMAN_KEYPOINT: HumanKeypoints
HEAD: HumanKeypoints
NOSE: HumanKeypoints
NECK: HumanKeypoints
RIGHT_SHOULDER: HumanKeypoints
RIGHT_ELBOW: HumanKeypoints
RIGHT_WRIST: HumanKeypoints
LEFT_SHOULDER: HumanKeypoints
LEFT_ELBOW: HumanKeypoints
LEFT_WRIST: HumanKeypoints
RIGHT_HIP: HumanKeypoints
RIGHT_KNEE: HumanKeypoints
RIGHT_ANKLE: HumanKeypoints
LEFT_HIP: HumanKeypoints
LEFT_KNEE: HumanKeypoints
LEFT_ANKLE: HumanKeypoints
RIGHT_EYE: HumanKeypoints
LEFT_EYE: HumanKeypoints
RIGHT_EAR: HumanKeypoints
LEFT_EAR: HumanKeypoints
CHEST: HumanKeypoints
UNKNOWN_OBJECT: ObjectLabels
HUMAN_SKELETON: ObjectLabels

class Image(_message.Message):
    __slots__ = ("data", "uri", "header", "sequence", "timestamp_source")
    DATA_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_SOURCE_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    uri: str
    header: _common_pb2.Header
    sequence: int
    timestamp_source: TimestampSource
    def __init__(self, data: _Optional[bytes] = ..., uri: _Optional[str] = ..., header: _Optional[_Union[_common_pb2.Header, _Mapping]] = ..., sequence: _Optional[int] = ..., timestamp_source: _Optional[_Union[TimestampSource, str]] = ...) -> None: ...

class RawImage(_message.Message):
    __slots__ = ("header", "resolution", "encoding", "is_bigendian", "step", "data")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    ENCODING_FIELD_NUMBER: _ClassVar[int]
    IS_BIGENDIAN_FIELD_NUMBER: _ClassVar[int]
    STEP_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    header: _common_pb2.Header
    resolution: Resolution
    encoding: str
    is_bigendian: bool
    step: int
    data: bytes
    def __init__(self, header: _Optional[_Union[_common_pb2.Header, _Mapping]] = ..., resolution: _Optional[_Union[Resolution, _Mapping]] = ..., encoding: _Optional[str] = ..., is_bigendian: bool = ..., step: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...

class CompressedImage(_message.Message):
    __slots__ = ("header", "format", "image")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    header: _common_pb2.Header
    format: str
    image: Image
    def __init__(self, header: _Optional[_Union[_common_pb2.Header, _Mapping]] = ..., format: _Optional[str] = ..., image: _Optional[_Union[Image, _Mapping]] = ...) -> None: ...

class ImageFormat(_message.Message):
    __slots__ = ("format", "compression")
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    COMPRESSION_FIELD_NUMBER: _ClassVar[int]
    format: ImageFormats
    compression: _wrappers_pb2.FloatValue
    def __init__(self, format: _Optional[_Union[ImageFormats, str]] = ..., compression: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]] = ...) -> None: ...

class Vertex(_message.Message):
    __slots__ = ("x", "y", "z")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    z: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., z: _Optional[float] = ...) -> None: ...

class BoundingPoly(_message.Message):
    __slots__ = ("vertices",)
    VERTICES_FIELD_NUMBER: _ClassVar[int]
    vertices: _containers.RepeatedCompositeFieldContainer[Vertex]
    def __init__(self, vertices: _Optional[_Iterable[_Union[Vertex, _Mapping]]] = ...) -> None: ...

class Resolution(_message.Message):
    __slots__ = ("height", "width")
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    height: int
    width: int
    def __init__(self, height: _Optional[int] = ..., width: _Optional[int] = ...) -> None: ...

class ColorSpace(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: ColorSpaces
    def __init__(self, value: _Optional[_Union[ColorSpaces, str]] = ...) -> None: ...

class ImageSettings(_message.Message):
    __slots__ = ("resolution", "format", "color_space", "region")
    RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    COLOR_SPACE_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    resolution: Resolution
    format: ImageFormat
    color_space: ColorSpace
    region: BoundingPoly
    def __init__(self, resolution: _Optional[_Union[Resolution, _Mapping]] = ..., format: _Optional[_Union[ImageFormat, _Mapping]] = ..., color_space: _Optional[_Union[ColorSpace, _Mapping]] = ..., region: _Optional[_Union[BoundingPoly, _Mapping]] = ...) -> None: ...

class PointAnnotation(_message.Message):
    __slots__ = ("id", "score", "position")
    ID_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    id: int
    score: float
    position: Vertex
    def __init__(self, id: _Optional[int] = ..., score: _Optional[float] = ..., position: _Optional[_Union[Vertex, _Mapping]] = ...) -> None: ...

class ObjectAnnotation(_message.Message):
    __slots__ = ("label", "id", "score", "region", "keypoints", "embedding")
    LABEL_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    KEYPOINTS_FIELD_NUMBER: _ClassVar[int]
    EMBEDDING_FIELD_NUMBER: _ClassVar[int]
    label: str
    id: int
    score: float
    region: BoundingPoly
    keypoints: _containers.RepeatedCompositeFieldContainer[PointAnnotation]
    embedding: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, label: _Optional[str] = ..., id: _Optional[int] = ..., score: _Optional[float] = ..., region: _Optional[_Union[BoundingPoly, _Mapping]] = ..., keypoints: _Optional[_Iterable[_Union[PointAnnotation, _Mapping]]] = ..., embedding: _Optional[_Iterable[float]] = ...) -> None: ...

class ObjectAnnotations(_message.Message):
    __slots__ = ("objects", "resolution", "frame_id")
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    FRAME_ID_FIELD_NUMBER: _ClassVar[int]
    objects: _containers.RepeatedCompositeFieldContainer[ObjectAnnotation]
    resolution: Resolution
    frame_id: int
    def __init__(self, objects: _Optional[_Iterable[_Union[ObjectAnnotation, _Mapping]]] = ..., resolution: _Optional[_Union[Resolution, _Mapping]] = ..., frame_id: _Optional[int] = ...) -> None: ...
