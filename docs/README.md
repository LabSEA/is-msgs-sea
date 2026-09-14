# Documentação dos protocolos
<a name="top"></a>

## Table of Contents

- [is/msgs/camera.proto](#is_msgs_camera-proto)
    - [AddTransformationReply](#is-vision-AddTransformationReply)
    - [AddTransformationRequest](#is-vision-AddTransformationRequest)
    - [CameraCalibration](#is-vision-CameraCalibration)
    - [CameraConfig](#is-vision-CameraConfig)
    - [CameraSetting](#is-vision-CameraSetting)
    - [CameraSettings](#is-vision-CameraSettings)
    - [FrameTransformation](#is-vision-FrameTransformation)
    - [FrameTransformations](#is-vision-FrameTransformations)
    - [GetCalibrationReply](#is-vision-GetCalibrationReply)
    - [GetCalibrationRequest](#is-vision-GetCalibrationRequest)
    - [GetTransformationReply](#is-vision-GetTransformationReply)
    - [GetTransformationRequest](#is-vision-GetTransformationRequest)
    - [IdPair](#is-vision-IdPair)
    - [PTZControl](#is-vision-PTZControl)
  
    - [CameraConfigFields](#is-vision-CameraConfigFields)
  
- [is/msgs/common.proto](#is_msgs_common-proto)
    - [ConsumerInfo](#is-common-ConsumerInfo)
    - [ConsumerList](#is-common-ConsumerList)
    - [ConsumerList.InfoEntry](#is-common-ConsumerList-InfoEntry)
    - [FieldSelector](#is-common-FieldSelector)
    - [Header](#is-common-Header)
    - [Orientation](#is-common-Orientation)
    - [Phrase](#is-common-Phrase)
    - [Pose](#is-common-Pose)
    - [PoseWithCovariance](#is-common-PoseWithCovariance)
    - [Position](#is-common-Position)
    - [Quaternion](#is-common-Quaternion)
    - [SamplingSettings](#is-common-SamplingSettings)
    - [Shape](#is-common-Shape)
    - [Shape.Dimension](#is-common-Shape-Dimension)
    - [Speed](#is-common-Speed)
    - [SpeedWithCovariance](#is-common-SpeedWithCovariance)
    - [SyncRequest](#is-common-SyncRequest)
    - [Tensor](#is-common-Tensor)
    - [Transform](#is-common-Transform)
    - [TransformStamped](#is-common-TransformStamped)
    - [Twist](#is-common-Twist)
    - [Vector3](#is-common-Vector3)
  
    - [DataType](#is-common-DataType)
  
- [is/msgs/image.proto](#is_msgs_image-proto)
    - [BoundingPoly](#is-vision-BoundingPoly)
    - [ColorSpace](#is-vision-ColorSpace)
    - [CompressedImage](#is-vision-CompressedImage)
    - [Image](#is-vision-Image)
    - [ImageFormat](#is-vision-ImageFormat)
    - [ImageSettings](#is-vision-ImageSettings)
    - [ObjectAnnotation](#is-vision-ObjectAnnotation)
    - [ObjectAnnotations](#is-vision-ObjectAnnotations)
    - [PointAnnotation](#is-vision-PointAnnotation)
    - [RawImage](#is-vision-RawImage)
    - [Resolution](#is-vision-Resolution)
    - [Vertex](#is-vision-Vertex)
  
    - [ColorSpaces](#is-vision-ColorSpaces)
    - [HumanKeypoints](#is-vision-HumanKeypoints)
    - [ImageFormats](#is-vision-ImageFormats)
    - [ObjectLabels](#is-vision-ObjectLabels)
    - [TimestampSource](#is-vision-TimestampSource)
  
- [is/msgs/power.proto](#is_msgs_power-proto)
    - [PowerInfo](#is-common-PowerInfo)
  
    - [PowerInfo.BatteryStatus](#is-common-PowerInfo-BatteryStatus)
    - [PowerInfo.BatteryType](#is-common-PowerInfo-BatteryType)
  
- [is/msgs/robot.proto](#is_msgs_robot-proto)
    - [BasicMoveTask](#is-robot-BasicMoveTask)
    - [Imu](#is-robot-Imu)
    - [Odometry](#is-robot-Odometry)
    - [PathRequest](#is-robot-PathRequest)
    - [PointCloud](#is-robot-PointCloud)
    - [PointField](#is-robot-PointField)
    - [RangeScan](#is-robot-RangeScan)
    - [RobotConfig](#is-robot-RobotConfig)
    - [RobotControllerProgress](#is-robot-RobotControllerProgress)
    - [RobotTaskReply](#is-robot-RobotTaskReply)
    - [RobotTaskRequest](#is-robot-RobotTaskRequest)
  
    - [PointFieldDataType](#is-robot-PointFieldDataType)
  
- [is/msgs/ros.proto](#is_msgs_ros-proto)
    - [ROSMessage](#is-ros-ROSMessage)
    - [TFMessage](#is-ros-TFMessage)
  
- [is/msgs/tests.proto](#is_msgs_tests-proto)
    - [Bar](#is-tests-Bar)
    - [Foo](#is-tests-Foo)
    - [Repeats](#is-tests-Repeats)
  
- [is/msgs/validate.proto](#is_msgs_validate-proto)
    - [AnyRules](#is-validate-AnyRules)
    - [BoolRules](#is-validate-BoolRules)
    - [BytesRules](#is-validate-BytesRules)
    - [DoubleRules](#is-validate-DoubleRules)
    - [DurationRules](#is-validate-DurationRules)
    - [EnumRules](#is-validate-EnumRules)
    - [FieldRules](#is-validate-FieldRules)
    - [Fixed32Rules](#is-validate-Fixed32Rules)
    - [Fixed64Rules](#is-validate-Fixed64Rules)
    - [FloatRules](#is-validate-FloatRules)
    - [Int32Rules](#is-validate-Int32Rules)
    - [Int64Rules](#is-validate-Int64Rules)
    - [MapRules](#is-validate-MapRules)
    - [MessageRules](#is-validate-MessageRules)
    - [RepeatedRules](#is-validate-RepeatedRules)
    - [SFixed32Rules](#is-validate-SFixed32Rules)
    - [SFixed64Rules](#is-validate-SFixed64Rules)
    - [SInt32Rules](#is-validate-SInt32Rules)
    - [SInt64Rules](#is-validate-SInt64Rules)
    - [StringRules](#is-validate-StringRules)
    - [TimestampRules](#is-validate-TimestampRules)
    - [UInt32Rules](#is-validate-UInt32Rules)
    - [UInt64Rules](#is-validate-UInt64Rules)
  
    - [File-level Extensions](#is_msgs_validate-proto-extensions)
    - [File-level Extensions](#is_msgs_validate-proto-extensions)
    - [File-level Extensions](#is_msgs_validate-proto-extensions)
  
- [Scalar Value Types](#scalar-value-types)



<a name="is_msgs_camera-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## is/msgs/camera.proto



<a name="is-vision-AddTransformationReply"></a>

### AddTransformationReply







<a name="is-vision-AddTransformationRequest"></a>

### AddTransformationRequest







<a name="is-vision-CameraCalibration"></a>

### CameraCalibration
Models the calibration parameters of a camera.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [int64](#int64) |  | Camera id. |
| calibrated_at | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  | When the calibration was performed. |
| error | [double](#double) |  | Average reprojection error. |
| resolution | [Resolution](#is-vision-Resolution) |  | Resolution used during calibration. |
| intrinsic | [is.common.Tensor](#is-common-Tensor) |  | Intrinsic matrix with shape=[3,3]. |
| distortion | [is.common.Tensor](#is-common-Tensor) |  | Distortion coefficients with shape=[1,5]. |
| extrinsic | [FrameTransformation](#is-vision-FrameTransformation) | repeated | Extrinsic tranformations. Used to transform from the camera frame to a world frame and vice versa. |






<a name="is-vision-CameraConfig"></a>

### CameraConfig
Camera parameters.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| sampling | [is.common.SamplingSettings](#is-common-SamplingSettings) |  | Sampling parameters. |
| image | [ImageSettings](#is-vision-ImageSettings) |  | Image parameters. |
| camera | [CameraSettings](#is-vision-CameraSettings) |  | Internal camera parameters. |
| stream_channel_id | [google.protobuf.Int32Value](#google-protobuf-Int32Value) |  | Stream Channel parameter |
| channel_id | [google.protobuf.Int32Value](#google-protobuf-Int32Value) |  | Channel Parameter |
| ptzcontrol | [PTZControl](#is-vision-PTZControl) |  | Camera PTZ control parameters. |






<a name="is-vision-CameraSetting"></a>

### CameraSetting



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| automatic | [bool](#bool) |  | True if the camera should automatically assign this parameter. |
| ratio | [float](#float) |  | Ratio assigned to the parameter where 0.0 is the lowest value and 1.0 the highest. |
| option | [string](#string) |  | For use when the camera requires a string type parameter. |






<a name="is-vision-CameraSettings"></a>

### CameraSettings



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| brightness | [CameraSetting](#is-vision-CameraSetting) |  |  |
| exposure | [CameraSetting](#is-vision-CameraSetting) |  |  |
| focus | [CameraSetting](#is-vision-CameraSetting) |  |  |
| gain | [CameraSetting](#is-vision-CameraSetting) |  |  |
| gamma | [CameraSetting](#is-vision-CameraSetting) |  |  |
| hue | [CameraSetting](#is-vision-CameraSetting) |  |  |
| iris | [CameraSetting](#is-vision-CameraSetting) |  |  |
| saturation | [CameraSetting](#is-vision-CameraSetting) |  |  |
| sharpness | [CameraSetting](#is-vision-CameraSetting) |  |  |
| shutter | [CameraSetting](#is-vision-CameraSetting) |  |  |
| white_balance_bu | [CameraSetting](#is-vision-CameraSetting) |  |  |
| white_balance_rv | [CameraSetting](#is-vision-CameraSetting) |  |  |
| zoom | [CameraSetting](#is-vision-CameraSetting) |  |  |
| contrast | [CameraSetting](#is-vision-CameraSetting) |  |  |






<a name="is-vision-FrameTransformation"></a>

### FrameTransformation
Represent the tranformation between two coordinate systems.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| from | [int64](#int64) |  | Id of the &#34;from&#34; frame. |
| to | [int64](#int64) |  | Id of the &#34;to&#34; frame. |
| tf | [is.common.Tensor](#is-common-Tensor) |  | Transformation matrix [R T; 0 1] with shape = [4,4]. |
| expiration | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  | Timepoint where this transformation is still valid. If not present the transformation will be considered to be valid forever. |






<a name="is-vision-FrameTransformations"></a>

### FrameTransformations



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| tfs | [FrameTransformation](#is-vision-FrameTransformation) | repeated | List of transformations. |






<a name="is-vision-GetCalibrationReply"></a>

### GetCalibrationReply



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| calibrations | [CameraCalibration](#is-vision-CameraCalibration) | repeated | Sequence of calibrations relative to the requested IDs. |






<a name="is-vision-GetCalibrationRequest"></a>

### GetCalibrationRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ids | [int64](#int64) | repeated | IDs of the cameras to return the calibration from. |






<a name="is-vision-GetTransformationReply"></a>

### GetTransformationReply



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| transformations | [FrameTransformation](#is-vision-FrameTransformation) | repeated | Sequence of transformations relative to the requested ids. |






<a name="is-vision-GetTransformationRequest"></a>

### GetTransformationRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ids | [IdPair](#is-vision-IdPair) | repeated | Sequence of pairs (from -&gt; to) describing the desired transformations |






<a name="is-vision-IdPair"></a>

### IdPair



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| from | [int64](#int64) |  |  |
| to | [int64](#int64) |  |  |






<a name="is-vision-PTZControl"></a>

### PTZControl



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| absolute | [is.common.Position](#is-common-Position) |  | Absolute position |
| step | [is.common.Position](#is-common-Position) |  | Relative position using steps |





 


<a name="is-vision-CameraConfigFields"></a>

### CameraConfigFields
Request selector/filter for CameraSettings. Used to select what fields
should be present in an CameraConfig GET request.
See [FieldSelector](#is.common.FieldSelector) for more information.

| Name | Number | Description |
| ---- | ------ | ----------- |
| ALL | 0 | Fill everything. |
| SAMPLING_SETTINGS | 1 | Fill sampling settings. |
| IMAGE_SETTINGS | 2 | Fill image settings. |
| CAMERA_SETTINGS | 3 | Fill camera settings. |
| STREAM_CHANNEL_ID | 4 | Fill stream channel settings |
| CHANNEL_ID | 5 | Fill camera channel settings |
| PTZCONTROL_SETTINGS | 6 | Fill camera control settings |


 

 

 



<a name="is_msgs_common-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## is/msgs/common.proto



<a name="is-common-ConsumerInfo"></a>

### ConsumerInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| consumers | [string](#string) | repeated | List of consumers. |






<a name="is-common-ConsumerList"></a>

### ConsumerList



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| info | [ConsumerList.InfoEntry](#is-common-ConsumerList-InfoEntry) | repeated | Consumer Information for each topic. |






<a name="is-common-ConsumerList-InfoEntry"></a>

### ConsumerList.InfoEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [string](#string) |  |  |
| value | [ConsumerInfo](#is-common-ConsumerInfo) |  |  |






<a name="is-common-FieldSelector"></a>

### FieldSelector
Used to select the desired fields of a message on a &#34;Get&#34; RPC.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| fields | [uint32](#uint32) | repeated | List of fields that should be filled. |






<a name="is-common-Header"></a>

### Header
Common timestamp and frame identifier used by stamped sensor messages.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| stamp | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| frame_id | [string](#string) |  |  |






<a name="is-common-Orientation"></a>

### Orientation



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| yaw | [float](#float) |  | Rotation around x. |
| pitch | [float](#float) |  | Rotation around y. |
| roll | [float](#float) |  | Rotation around z. |
| quaternion | [Quaternion](#is-common-Quaternion) |  | Original quaternion when available; Euler fields remain for compatibility. |
| header | [Header](#is-common-Header) |  | Present when the source is a stamped orientation message. |






<a name="is-common-Phrase"></a>

### Phrase



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| content | [string](#string) | repeated | List of words. |
| confidence | [float](#float) |  | Confidence of recognized phrase. |
| language | [string](#string) |  | Identifies language using Locale Name pattern. |






<a name="is-common-Pose"></a>

### Pose



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| position | [Position](#is-common-Position) |  |  |
| orientation | [Orientation](#is-common-Orientation) |  |  |
| header | [Header](#is-common-Header) |  |  |






<a name="is-common-PoseWithCovariance"></a>

### PoseWithCovariance



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| pose | [Pose](#is-common-Pose) |  |  |
| covariance | [double](#double) | repeated | Row-major 6x6 covariance matrix. |






<a name="is-common-Position"></a>

### Position



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| x | [float](#float) |  | Position in the x axis. |
| y | [float](#float) |  | Position in the y axis. |
| z | [float](#float) |  | Position in the z axis. |
| precise | [Vector3](#is-common-Vector3) |  | Double-precision representation for consumers that require it. |
| header | [Header](#is-common-Header) |  | Present when the source is a stamped position/vector message. |






<a name="is-common-Quaternion"></a>

### Quaternion
Quaternion rotation represented as (x, y, z, w).


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| x | [double](#double) |  |  |
| y | [double](#double) |  |  |
| z | [double](#double) |  |  |
| w | [double](#double) |  |  |






<a name="is-common-SamplingSettings"></a>

### SamplingSettings



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| frequency | [google.protobuf.FloatValue](#google-protobuf-FloatValue) |  | Sampling frequency in hertz. |
| delay | [google.protobuf.FloatValue](#google-protobuf-FloatValue) |  | Delay to be applied in the in the sampling proccess, normally used to synchronize different sources. |






<a name="is-common-Shape"></a>

### Shape



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| dims | [Shape.Dimension](#is-common-Shape-Dimension) | repeated |  |






<a name="is-common-Shape-Dimension"></a>

### Shape.Dimension



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| size | [int32](#int32) |  | Number of elements in this dimension. |
| name | [string](#string) |  | Dimension identifier. This can be used to indicate the order that the dimensions are placed in a tensor. For instance, in a tensor with two dimensions (matrix) the name can be something like &#34;row&#34; or &#34;collumn&#34; indicating if the memory layout is row or collumn major. |






<a name="is-common-Speed"></a>

### Speed



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| linear | [float](#float) |  |  |
| angular | [float](#float) |  |  |
| twist | [Twist](#is-common-Twist) |  | Full 3D velocity; scalar fields retain the legacy x/z projection. |
| header | [Header](#is-common-Header) |  |  |






<a name="is-common-SpeedWithCovariance"></a>

### SpeedWithCovariance



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| speed | [Speed](#is-common-Speed) |  |  |
| covariance | [double](#double) | repeated | Row-major 6x6 covariance matrix. |






<a name="is-common-SyncRequest"></a>

### SyncRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| entities | [string](#string) | repeated |  |
| sampling | [SamplingSettings](#is-common-SamplingSettings) |  |  |






<a name="is-common-Tensor"></a>

### Tensor



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| shape | [Shape](#is-common-Shape) |  | Shape of the tensor. Define how the tensor is represented in one of the value fields (floats, doubles, ints32, ints64). |
| type | [DataType](#is-common-DataType) |  | Type of the tensor values. |
| floats | [float](#float) | repeated |  |
| doubles | [double](#double) | repeated |  |
| ints32 | [int32](#int32) | repeated |  |
| ints64 | [int64](#int64) | repeated |  |






<a name="is-common-Transform"></a>

### Transform



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| translation | [Vector3](#is-common-Vector3) |  |  |
| rotation | [Quaternion](#is-common-Quaternion) |  |  |






<a name="is-common-TransformStamped"></a>

### TransformStamped



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| header | [Header](#is-common-Header) |  |  |
| child_frame_id | [string](#string) |  |  |
| transform | [Transform](#is-common-Transform) |  |  |






<a name="is-common-Twist"></a>

### Twist



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| linear | [Vector3](#is-common-Vector3) |  |  |
| angular | [Vector3](#is-common-Vector3) |  |  |






<a name="is-common-Vector3"></a>

### Vector3
Three-dimensional vector represented with ROS-compatible double precision.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| x | [double](#double) |  |  |
| y | [double](#double) |  |  |
| z | [double](#double) |  |  |





 


<a name="is-common-DataType"></a>

### DataType


| Name | Number | Description |
| ---- | ------ | ----------- |
| UNKNOWN_TYPE | 0 |  |
| FLOAT_TYPE | 1 |  |
| DOUBLE_TYPE | 2 |  |
| INT32_TYPE | 3 |  |
| INT64_TYPE | 4 |  |


 

 

 



<a name="is_msgs_image-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## is/msgs/image.proto



<a name="is-vision-BoundingPoly"></a>

### BoundingPoly
Sequence of vertices modelling a polygon.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| vertices | [Vertex](#is-vision-Vertex) | repeated | The polygon vertices. |






<a name="is-vision-ColorSpace"></a>

### ColorSpace



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| value | [ColorSpaces](#is-vision-ColorSpaces) |  | Color space value. |






<a name="is-vision-CompressedImage"></a>

### CompressedImage
Compressed ROS image with its original format descriptor and frame header.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| header | [is.common.Header](#is-common-Header) |  |  |
| format | [string](#string) |  |  |
| image | [Image](#is-vision-Image) |  |  |






<a name="is-vision-Image"></a>

### Image
Message representing an Image. The image content can be either sent embedded on this message
or referenced as an external resource.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| data | [bytes](#bytes) |  | Image content, represented as a stream of bytes in well known image [formats](#is.image.ImageFormat). |
| uri | [string](#string) |  | URI to external image source. |
| header | [is.common.Header](#is-common-Header) |  | Acquisition timestamp and camera frame identifier. Older producers may leave this field unset. |
| sequence | [uint64](#uint64) |  | Monotonic sequence number assigned by the producer for this camera. |
| timestamp_source | [TimestampSource](#is-vision-TimestampSource) |  | Describes how header.stamp was obtained. |






<a name="is-vision-ImageFormat"></a>

### ImageFormat



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| format | [ImageFormats](#is-vision-ImageFormats) |  | Image compression algorithm. |
| compression | [google.protobuf.FloatValue](#google-protobuf-FloatValue) |  | Image compression level. |






<a name="is-vision-ImageSettings"></a>

### ImageSettings



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| resolution | [Resolution](#is-vision-Resolution) |  | Image resolution (height, width). |
| format | [ImageFormat](#is-vision-ImageFormat) |  | Image compression details. e.g: PNG. |
| color_space | [ColorSpace](#is-vision-ColorSpace) |  | Color space. |
| region | [BoundingPoly](#is-vision-BoundingPoly) |  | Bounding poly defining the region of interest in the image. This region is usually represented as a rectangle modelled by the TopLeft and BottomRight vertices. |






<a name="is-vision-ObjectAnnotation"></a>

### ObjectAnnotation
Models an annotation on an object (in an image or in space).


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| label | [string](#string) |  | Label that identifies in human language the object in the annotated region. e.g: human, dog, computer, etc. |
| id | [int64](#int64) |  | Number that identifies the object in the annotated region, usually comes from an enumeration. |
| score | [float](#float) |  | Represents how sure the annotator thinks that an object of the specified type exists on the region. |
| region | [BoundingPoly](#is-vision-BoundingPoly) |  | Identifies the region in the image/space where the object is contained NOTE: When defined on an image the vertex coordinates are in the same scale (resolution) as the original image. |
| keypoints | [PointAnnotation](#is-vision-PointAnnotation) | repeated | Annotations of interesting points in the image. e.g: Hip, Nose, Eye. NOTE: When defined on an image the vertex coordinates are in the same scale (resolution) as the original image. |
| embedding | [float](#float) | repeated | L2-normalized person re-identification feature vector. |






<a name="is-vision-ObjectAnnotations"></a>

### ObjectAnnotations
Models many annotated objects. (List of objects and their respective annotations).
If resolution is present the annotations are assumed to be on an Image, otherwise
they are assumed to be in Space and a proper frame_id must be set.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| objects | [ObjectAnnotation](#is-vision-ObjectAnnotation) | repeated | List of objects and their respective annotations. |
| resolution | [Resolution](#is-vision-Resolution) |  | Original resolution of the image when annotation an image. |
| frame_id | [int64](#int64) |  | Id of the frame of reference used to localize the vertices when annotating objects in space. |






<a name="is-vision-PointAnnotation"></a>

### PointAnnotation
Models an annotation on a point (in an image or in space).


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [int64](#int64) |  | Id of the keypoint being annotated, usually comes from an enumeration, e.g: [HumanKeypoints](#is.vision.HumanKeypoints). |
| score | [float](#float) |  | Represents how sure the annotator thinks that a keypoint of the specified type exists on the given position. |
| position | [Vertex](#is-vision-Vertex) |  | Position of the keypoint. Represented by (x,y) on images and (x,y,z) on spaces. |






<a name="is-vision-RawImage"></a>

### RawImage
Uncompressed pixel buffer, preserving the sensor_msgs/Image memory layout.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| header | [is.common.Header](#is-common-Header) |  |  |
| resolution | [Resolution](#is-vision-Resolution) |  |  |
| encoding | [string](#string) |  | ROS image encoding string, for example rgb8, mono16, or 32FC1. |
| is_bigendian | [bool](#bool) |  |  |
| step | [uint32](#uint32) |  | Full row length in bytes, including any padding. |
| data | [bytes](#bytes) |  |  |






<a name="is-vision-Resolution"></a>

### Resolution
Models the resolution of an image, that is the number of pixels in an image.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| height | [uint32](#uint32) |  | Number of vertical pixels. |
| width | [uint32](#uint32) |  | Number of horizontal pixels. |






<a name="is-vision-Vertex"></a>

### Vertex
A vertex represents a point in the image (2D: x,y) or in space (3D: x,y,z).


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| x | [float](#float) |  | X coordinate. |
| y | [float](#float) |  | Y coordinate. |
| z | [float](#float) |  | Z coordinate. |





 


<a name="is-vision-ColorSpaces"></a>

### ColorSpaces
List of color spaces

| Name | Number | Description |
| ---- | ------ | ----------- |
| RGB | 0 | Red, Green, Blue. |
| GRAY | 1 | Grayscale. |
| YCbCr | 2 | Luma, Blue-Difference, Red-Difference. |
| HSV | 3 | Hue, Saturation, Value. |



<a name="is-vision-HumanKeypoints"></a>

### HumanKeypoints
Models keypoints present in the human body.

| Name | Number | Description |
| ---- | ------ | ----------- |
| UNKNOWN_HUMAN_KEYPOINT | 0 |  |
| HEAD | 1 |  |
| NOSE | 2 |  |
| NECK | 3 |  |
| RIGHT_SHOULDER | 4 |  |
| RIGHT_ELBOW | 5 |  |
| RIGHT_WRIST | 6 |  |
| LEFT_SHOULDER | 7 |  |
| LEFT_ELBOW | 8 |  |
| LEFT_WRIST | 9 |  |
| RIGHT_HIP | 10 |  |
| RIGHT_KNEE | 11 |  |
| RIGHT_ANKLE | 12 |  |
| LEFT_HIP | 13 |  |
| LEFT_KNEE | 14 |  |
| LEFT_ANKLE | 15 |  |
| RIGHT_EYE | 16 |  |
| LEFT_EYE | 17 |  |
| RIGHT_EAR | 18 |  |
| LEFT_EAR | 19 |  |
| CHEST | 20 |  |



<a name="is-vision-ImageFormats"></a>

### ImageFormats
List of image formats.

| Name | Number | Description |
| ---- | ------ | ----------- |
| PNG | 0 |  |
| JPEG | 1 |  |
| WebP | 2 |  |



<a name="is-vision-ObjectLabels"></a>

### ObjectLabels


| Name | Number | Description |
| ---- | ------ | ----------- |
| UNKNOWN_OBJECT | 0 |  |
| HUMAN_SKELETON | 1 |  |


<a name="is-vision-TimestampSource"></a>

### TimestampSource
Origin of an image acquisition timestamp.

| Name | Number | Description |
| ---- | ------ | ----------- |
| TIMESTAMP_SOURCE_UNSPECIFIED | 0 |  |
| TIMESTAMP_SOURCE_CAMERA | 1 |  |
| TIMESTAMP_SOURCE_GATEWAY_RECEIVE | 2 |  |


 

 

 



<a name="is_msgs_power-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## is/msgs/power.proto



<a name="is-common-PowerInfo"></a>

### PowerInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| voltage | [float](#float) |  | Battery voltage in volts |
| terminal_voltage | [float](#float) |  | Lower voltage limit |
| cell_voltage | [float](#float) | repeated | When battery contain cells, voltage of each one |
| charge | [float](#float) |  | Charge percentage on 0 to 1 range |
| capacity | [float](#float) |  | Capacity in Ah |
| type | [PowerInfo.BatteryType](#is-common-PowerInfo-BatteryType) |  | Battery type |
| status | [PowerInfo.BatteryStatus](#is-common-PowerInfo-BatteryStatus) |  | Battery status |
| uptime | [google.protobuf.Duration](#google-protobuf-Duration) |  |  |
| autonomy | [google.protobuf.Duration](#google-protobuf-Duration) |  | How long the battery will last at the current discharge rate |





 


<a name="is-common-PowerInfo-BatteryStatus"></a>

### PowerInfo.BatteryStatus


| Name | Number | Description |
| ---- | ------ | ----------- |
| UNKNOWN | 0 |  |
| CHARGING | 1 |  |
| DISCHARGING | 2 |  |
| CHARGED | 3 |  |
| NOT_CONNECTED | 4 |  |



<a name="is-common-PowerInfo-BatteryType"></a>

### PowerInfo.BatteryType


| Name | Number | Description |
| ---- | ------ | ----------- |
| PB | 0 |  |
| NICD | 1 |  |
| NIMH | 2 |  |
| LIPO | 3 |  |


 

 

 



<a name="is_msgs_robot-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## is/msgs/robot.proto



<a name="is-robot-BasicMoveTask"></a>

### BasicMoveTask



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| positions | [is.common.Position](#is-common-Position) | repeated | (Optional) List of positions indicating the desired path. |
| speeds | [is.common.Speed](#is-common-Speed) | repeated | (Optional) List of speeds to be executed at each respective position of a trajectory. If present, should have the same size as the positions field. |
| final_orientation | [is.common.Orientation](#is-common-Orientation) |  | (Optional) Desired orientation of the robot after finishing the task. |
| allowed_error | [float](#float) |  | (Required) Error value where the controller can consider that the point was reached successfully. |
| rate | [float](#float) |  | (Required) Controller loop frequency in hertz. |






<a name="is-robot-Imu"></a>

### Imu



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| header | [is.common.Header](#is-common-Header) |  |  |
| orientation | [is.common.Quaternion](#is-common-Quaternion) |  |  |
| orientation_covariance | [double](#double) | repeated |  |
| angular_velocity | [is.common.Vector3](#is-common-Vector3) |  |  |
| angular_velocity_covariance | [double](#double) | repeated |  |
| linear_acceleration | [is.common.Vector3](#is-common-Vector3) |  |  |
| linear_acceleration_covariance | [double](#double) | repeated |  |






<a name="is-robot-Odometry"></a>

### Odometry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| header | [is.common.Header](#is-common-Header) |  |  |
| child_frame_id | [string](#string) |  |  |
| pose | [is.common.PoseWithCovariance](#is-common-PoseWithCovariance) |  |  |
| twist | [is.common.SpeedWithCovariance](#is-common-SpeedWithCovariance) |  |  |






<a name="is-robot-PathRequest"></a>

### PathRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint64](#uint64) |  | Unique identifier of the request. |
| destination_pose | [is.common.Pose](#is-common-Pose) |  | Destination pose. |
| robot_gateway_id | [uint64](#uint64) |  | Robot Gateway ID. |
| rate | [float](#float) |  | Robot Task Rate. |
| allowed_error | [float](#float) |  | Robot Task Allowed Error. |






<a name="is-robot-PointCloud"></a>

### PointCloud
Binary point cloud preserving the sensor_msgs/PointCloud2 layout.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| header | [is.common.Header](#is-common-Header) |  |  |
| height | [uint32](#uint32) |  |  |
| width | [uint32](#uint32) |  |  |
| fields | [PointField](#is-robot-PointField) | repeated |  |
| is_bigendian | [bool](#bool) |  |  |
| point_step | [uint32](#uint32) |  |  |
| row_step | [uint32](#uint32) |  |  |
| data | [bytes](#bytes) |  |  |
| is_dense | [bool](#bool) |  |  |






<a name="is-robot-PointField"></a>

### PointField



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  |  |
| offset | [uint32](#uint32) |  |  |
| datatype | [PointFieldDataType](#is-robot-PointFieldDataType) |  |  |
| count | [uint32](#uint32) |  |  |






<a name="is-robot-RangeScan"></a>

### RangeScan



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| angles | [float](#float) | repeated |  |
| ranges | [float](#float) | repeated |  |
| header | [is.common.Header](#is-common-Header) |  |  |
| angle_min | [float](#float) |  |  |
| angle_max | [float](#float) |  |  |
| angle_increment | [float](#float) |  |  |
| time_increment | [float](#float) |  |  |
| scan_time | [float](#float) |  |  |
| range_min | [float](#float) |  |  |
| range_max | [float](#float) |  |  |
| intensities | [float](#float) | repeated |  |






<a name="is-robot-RobotConfig"></a>

### RobotConfig



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| speed | [is.common.Speed](#is-common-Speed) |  |  |






<a name="is-robot-RobotControllerProgress"></a>

### RobotControllerProgress



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint64](#uint64) |  | Unique identifier of the task. |
| current_speed | [is.common.Speed](#is-common-Speed) |  | Speed command sent to the robot in order to make the current pose equals to the desired one. |
| current_pose | [is.common.Pose](#is-common-Pose) |  | Pose where the robot actually is. |
| desired_pose | [is.common.Pose](#is-common-Pose) |  | Pose where the robot should be now. |
| error | [float](#float) |  | Robot positioning error for the current task. |
| completion | [float](#float) |  | Percentage indicating how much of the task has been completed yet. |
| sources | [string](#string) | repeated | Sources used to locate the robot. |
| begin | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  | Timestamp of when the task started. |
| end | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  | Timestamp of when the task finished. |






<a name="is-robot-RobotTaskReply"></a>

### RobotTaskReply



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint64](#uint64) |  | Unique identifier of the task. |






<a name="is-robot-RobotTaskRequest"></a>

### RobotTaskRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint64](#uint64) |  | (Optional) Task id, if none is provided one will be generated. |
| basic_move_task | [BasicMoveTask](#is-robot-BasicMoveTask) |  |  |







<a name="is-robot-PointFieldDataType"></a>

### PointFieldDataType


| Name | Number | Description |
| ---- | ------ | ----------- |
| POINT_FIELD_DATATYPE_UNSPECIFIED | 0 |  |
| POINT_FIELD_INT8 | 1 |  |
| POINT_FIELD_UINT8 | 2 |  |
| POINT_FIELD_INT16 | 3 |  |
| POINT_FIELD_UINT16 | 4 |  |
| POINT_FIELD_INT32 | 5 |  |
| POINT_FIELD_UINT32 | 6 |  |
| POINT_FIELD_FLOAT32 | 7 |  |
| POINT_FIELD_FLOAT64 | 8 |  |




<a name="is_msgs_ros-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## is/msgs/ros.proto



<a name="is-ros-ROSMessage"></a>

### ROSMessage
Dynamic fallback for ROS message types without a native is-msgs schema.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [string](#string) |  |  |
| content | [google.protobuf.Struct](#google-protobuf-Struct) |  |  |






<a name="is-ros-TFMessage"></a>

### TFMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| transforms | [is.common.TransformStamped](#is-common-TransformStamped) | repeated |  |





 

 

 

 



<a name="is_msgs_tests-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## is/msgs/tests.proto



<a name="is-tests-Bar"></a>

### Bar



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| myfoo | [Foo](#is-tests-Foo) |  |  |
| myfloat | [float](#float) |  |  |






<a name="is-tests-Foo"></a>

### Foo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| myint | [int32](#int32) |  |  |
| myfloat | [float](#float) |  |  |
| mydouble | [double](#double) |  |  |






<a name="is-tests-Repeats"></a>

### Repeats



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| foos | [Foo](#is-tests-Foo) | repeated |  |
| foo2 | [Foo](#is-tests-Foo) |  |  |
| int32s | [int32](#int32) | repeated |  |
| uint32s | [uint32](#uint32) | repeated |  |
| floats | [float](#float) | repeated |  |
| doubles | [double](#double) | repeated |  |
| int64s | [int64](#int64) | repeated |  |
| uint64s | [uint64](#uint64) | repeated |  |





 

 

 

 



<a name="is_msgs_validate-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## is/msgs/validate.proto



<a name="is-validate-AnyRules"></a>

### AnyRules
AnyRules describe constraints applied exclusively to the
`google.protobuf.Any` well-known type


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| required | [bool](#bool) | optional | Required specifies that this field must be set |
| in | [string](#string) | repeated | In specifies that this field&#39;s `type_url` must be equal to one of the specified values. |
| not_in | [string](#string) | repeated | NotIn specifies that this field&#39;s `type_url` must not be equal to any of the specified values. |






<a name="is-validate-BoolRules"></a>

### BoolRules
BoolRules describes the constraints applied to `bool` values


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| const | [bool](#bool) | optional | Const specifies that this field must be exactly the specified value |






<a name="is-validate-BytesRules"></a>

### BytesRules
BytesRules describe the constraints applied to `bytes` values


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| const | [bytes](#bytes) | optional | Const specifies that this field must be exactly the specified value |
| min_len | [uint64](#uint64) | optional | MinLen specifies that this field must be the specified number of bytes at a minimum |
| max_len | [uint64](#uint64) | optional | MaxLen specifies that this field must be the specified number of bytes at a maximum |
| pattern | [string](#string) | optional | Pattern specifes that this field must match against the specified regular expression (RE2 syntax). The included expression should elide any delimiters. |
| prefix | [bytes](#bytes) | optional | Prefix specifies that this field must have the specified bytes at the beginning of the string. |
| suffix | [bytes](#bytes) | optional | Suffix specifies that this field must have the specified bytes at the end of the string. |
| contains | [bytes](#bytes) | optional | Contains specifies that this field must have the specified bytes anywhere in the string. |
| in | [bytes](#bytes) | repeated | In specifies that this field must be equal to one of the specified values |
| not_in | [bytes](#bytes) | repeated | NotIn specifies that this field cannot be equal to one of the specified values |
| ip | [bool](#bool) | optional | Ip specifies that the field must be a valid IP (v4 or v6) address in byte format |
| ipv4 | [bool](#bool) | optional | Ipv4 specifies that the field must be a valid IPv4 address in byte format |
| ipv6 | [bool](#bool) | optional | Ipv6 specifies that the field must be a valid IPv6 address in byte format |






<a name="is-validate-DoubleRules"></a>

### DoubleRules
DoubleRules describes the constraints applied to `double` values


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| const | [double](#double) | optional | Const specifies that this field must be exactly the specified value |
| lt | [double](#double) | optional | Lt specifies that this field must be less than the specified value, exclusive |
| lte | [double](#double) | optional | Lte specifies that this field must be less than or equal to the specified value, inclusive |
| gt | [double](#double) | optional | Gt specifies that this field must be greater than the specified value, exclusive. If the value of Gt is larger than a specified Lt or Lte, the range is reversed. |
| gte | [double](#double) | optional | Gte specifies that this field must be greater than or equal to the specified value, inclusive. If the value of Gte is larger than a specified Lt or Lte, the range is reversed. |
| in | [double](#double) | repeated | In specifies that this field must be equal to one of the specified values |
| not_in | [double](#double) | repeated | NotIn specifies that this field cannot be equal to one of the specified values |






<a name="is-validate-DurationRules"></a>

### DurationRules
DurationRules describe the constraints applied exclusively to the
`google.protobuf.Duration` well-known type


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| required | [bool](#bool) | optional | Required specifies that this field must be set |
| const | [google.protobuf.Duration](#google-protobuf-Duration) | optional | Const specifies that this field must be exactly the specified value |
| lt | [google.protobuf.Duration](#google-protobuf-Duration) | optional | Lt specifies that this field must be less than the specified value, exclusive |
| lte | [google.protobuf.Duration](#google-protobuf-Duration) | optional | Lt specifies that this field must be less than the specified value, inclusive |
| gt | [google.protobuf.Duration](#google-protobuf-Duration) | optional | Gt specifies that this field must be greater than the specified value, exclusive |
| gte | [google.protobuf.Duration](#google-protobuf-Duration) | optional | Gte specifies that this field must be greater than the specified value, inclusive |
| in | [google.protobuf.Duration](#google-protobuf-Duration) | repeated | In specifies that this field must be equal to one of the specified values |
| not_in | [google.protobuf.Duration](#google-protobuf-Duration) | repeated | NotIn specifies that this field cannot be equal to one of the specified values |






<a name="is-validate-EnumRules"></a>

### EnumRules
EnumRules describe the constraints applied to enum values


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| const | [int32](#int32) | optional | Const specifies that this field must be exactly the specified value |
| defined_only | [bool](#bool) | optional | DefinedOnly specifies that this field must be only one of the defined values for this enum, failing on any undefined value. |
| in | [int32](#int32) | repeated | In specifies that this field must be equal to one of the specified values |
| not_in | [int32](#int32) | repeated | NotIn specifies that this field cannot be equal to one of the specified values |






<a name="is-validate-FieldRules"></a>

### FieldRules
FieldRules encapsulates the rules for each type of field. Depending on the
field, the correct set should be used to ensure proper validations.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| float | [FloatRules](#is-validate-FloatRules) | optional | Scalar Field Types |
| double | [DoubleRules](#is-validate-DoubleRules) | optional |  |
| int32 | [Int32Rules](#is-validate-Int32Rules) | optional |  |
| int64 | [Int64Rules](#is-validate-Int64Rules) | optional |  |
| uint32 | [UInt32Rules](#is-validate-UInt32Rules) | optional |  |
| uint64 | [UInt64Rules](#is-validate-UInt64Rules) | optional |  |
| sint32 | [SInt32Rules](#is-validate-SInt32Rules) | optional |  |
| sint64 | [SInt64Rules](#is-validate-SInt64Rules) | optional |  |
| fixed32 | [Fixed32Rules](#is-validate-Fixed32Rules) | optional |  |
| fixed64 | [Fixed64Rules](#is-validate-Fixed64Rules) | optional |  |
| sfixed32 | [SFixed32Rules](#is-validate-SFixed32Rules) | optional |  |
| sfixed64 | [SFixed64Rules](#is-validate-SFixed64Rules) | optional |  |
| bool | [BoolRules](#is-validate-BoolRules) | optional |  |
| string | [StringRules](#is-validate-StringRules) | optional |  |
| bytes | [BytesRules](#is-validate-BytesRules) | optional |  |
| enum | [EnumRules](#is-validate-EnumRules) | optional | Complex Field Types |
| message | [MessageRules](#is-validate-MessageRules) | optional |  |
| repeated | [RepeatedRules](#is-validate-RepeatedRules) | optional |  |
| map | [MapRules](#is-validate-MapRules) | optional |  |
| any | [AnyRules](#is-validate-AnyRules) | optional | Well-Known Field Types |
| duration | [DurationRules](#is-validate-DurationRules) | optional |  |
| timestamp | [TimestampRules](#is-validate-TimestampRules) | optional |  |






<a name="is-validate-Fixed32Rules"></a>

### Fixed32Rules
Fixed32Rules describes the constraints applied to `fixed32` values


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| const | [fixed32](#fixed32) | optional | Const specifies that this field must be exactly the specified value |
| lt | [fixed32](#fixed32) | optional | Lt specifies that this field must be less than the specified value, exclusive |
| lte | [fixed32](#fixed32) | optional | Lte specifies that this field must be less than or equal to the specified value, inclusive |
| gt | [fixed32](#fixed32) | optional | Gt specifies that this field must be greater than the specified value, exclusive. If the value of Gt is larger than a specified Lt or Lte, the range is reversed. |
| gte | [fixed32](#fixed32) | optional | Gte specifies that this field must be greater than or equal to the specified value, inclusive. If the value of Gte is larger than a specified Lt or Lte, the range is reversed. |
| in | [fixed32](#fixed32) | repeated | In specifies that this field must be equal to one of the specified values |
| not_in | [fixed32](#fixed32) | repeated | NotIn specifies that this field cannot be equal to one of the specified values |






<a name="is-validate-Fixed64Rules"></a>

### Fixed64Rules
Fixed64Rules describes the constraints applied to `fixed64` values


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| const | [fixed64](#fixed64) | optional | Const specifies that this field must be exactly the specified value |
| lt | [fixed64](#fixed64) | optional | Lt specifies that this field must be less than the specified value, exclusive |
| lte | [fixed64](#fixed64) | optional | Lte specifies that this field must be less than or equal to the specified value, inclusive |
| gt | [fixed64](#fixed64) | optional | Gt specifies that this field must be greater than the specified value, exclusive. If the value of Gt is larger than a specified Lt or Lte, the range is reversed. |
| gte | [fixed64](#fixed64) | optional | Gte specifies that this field must be greater than or equal to the specified value, inclusive. If the value of Gte is larger than a specified Lt or Lte, the range is reversed. |
| in | [fixed64](#fixed64) | repeated | In specifies that this field must be equal to one of the specified values |
| not_in | [fixed64](#fixed64) | repeated | NotIn specifies that this field cannot be equal to one of the specified values |






<a name="is-validate-FloatRules"></a>

### FloatRules
FloatRules describes the constraints applied to `float` values


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| const | [float](#float) | optional | Const specifies that this field must be exactly the specified value |
| lt | [float](#float) | optional | Lt specifies that this field must be less than the specified value, exclusive |
| lte | [float](#float) | optional | Lte specifies that this field must be less than or equal to the specified value, inclusive |
| gt | [float](#float) | optional | Gt specifies that this field must be greater than the specified value, exclusive. If the value of Gt is larger than a specified Lt or Lte, the range is reversed. |
| gte | [float](#float) | optional | Gte specifies that this field must be greater than or equal to the specified value, inclusive. If the value of Gte is larger than a specified Lt or Lte, the range is reversed. |
| in | [float](#float) | repeated | In specifies that this field must be equal to one of the specified values |
| not_in | [float](#float) | repeated | NotIn specifies that this field cannot be equal to one of the specified values |






<a name="is-validate-Int32Rules"></a>

### Int32Rules
Int32Rules describes the constraints applied to `int32` values


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| const | [int32](#int32) | optional | Const specifies that this field must be exactly the specified value |
| lt | [int32](#int32) | optional | Lt specifies that this field must be less than the specified value, exclusive |
| lte | [int32](#int32) | optional | Lte specifies that this field must be less than or equal to the specified value, inclusive |
| gt | [int32](#int32) | optional | Gt specifies that this field must be greater than the specified value, exclusive. If the value of Gt is larger than a specified Lt or Lte, the range is reversed. |
| gte | [int32](#int32) | optional | Gte specifies that this field must be greater than or equal to the specified value, inclusive. If the value of Gte is larger than a specified Lt or Lte, the range is reversed. |
| in | [int32](#int32) | repeated | In specifies that this field must be equal to one of the specified values |
| not_in | [int32](#int32) | repeated | NotIn specifies that this field cannot be equal to one of the specified values |






<a name="is-validate-Int64Rules"></a>

### Int64Rules
Int64Rules describes the constraints applied to `int64` values


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| const | [int64](#int64) | optional | Const specifies that this field must be exactly the specified value |
| lt | [int64](#int64) | optional | Lt specifies that this field must be less than the specified value, exclusive |
| lte | [int64](#int64) | optional | Lte specifies that this field must be less than or equal to the specified value, inclusive |
| gt | [int64](#int64) | optional | Gt specifies that this field must be greater than the specified value, exclusive. If the value of Gt is larger than a specified Lt or Lte, the range is reversed. |
| gte | [int64](#int64) | optional | Gte specifies that this field must be greater than or equal to the specified value, inclusive. If the value of Gte is larger than a specified Lt or Lte, the range is reversed. |
| in | [int64](#int64) | repeated | In specifies that this field must be equal to one of the specified values |
| not_in | [int64](#int64) | repeated | NotIn specifies that this field cannot be equal to one of the specified values |






<a name="is-validate-MapRules"></a>

### MapRules
MapRules describe the constraints applied to `map` values


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| min_pairs | [uint64](#uint64) | optional | MinPairs specifies that this field must have the specified number of KVs at a minimum |
| max_pairs | [uint64](#uint64) | optional | MaxPairs specifies that this field must have the specified number of KVs at a maximum |
| no_sparse | [bool](#bool) | optional | NoSparse specifies values in this field cannot be unset. This only applies to map&#39;s with message value types. |
| keys | [FieldRules](#is-validate-FieldRules) | optional | Keys specifies the constraints to be applied to each key in the field. |
| values | [FieldRules](#is-validate-FieldRules) | optional | Values specifies the constraints to be applied to the value of each key in the field. Message values will still have their validations evaluated unless skip is specified here. |






<a name="is-validate-MessageRules"></a>

### MessageRules
MessageRules describe the constraints applied to embedded message values.
For message-type fields, validation is performed recursively.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| skip | [bool](#bool) | optional | Skip specifies that the validation rules of this field should not be evaluated |
| required | [bool](#bool) | optional | Required specifies that this field must be set |






<a name="is-validate-RepeatedRules"></a>

### RepeatedRules
RepeatedRules describe the constraints applied to `repeated` values


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| min_items | [uint64](#uint64) | optional | MinItems specifies that this field must have the specified number of items at a minimum |
| max_items | [uint64](#uint64) | optional | MaxItems specifies that this field must have the specified number of items at a maximum |
| unique | [bool](#bool) | optional | Unique specifies that all elements in this field must be unique. This contraint is only applicable to scalar and enum types (messages are not supported). |
| items | [FieldRules](#is-validate-FieldRules) | optional | Items specifies the contraints to be applied to each item in the field. Repeated message fields will still execute validation against each item unless skip is specified here. |






<a name="is-validate-SFixed32Rules"></a>

### SFixed32Rules
SFixed32Rules describes the constraints applied to `sfixed32` values


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| const | [sfixed32](#sfixed32) | optional | Const specifies that this field must be exactly the specified value |
| lt | [sfixed32](#sfixed32) | optional | Lt specifies that this field must be less than the specified value, exclusive |
| lte | [sfixed32](#sfixed32) | optional | Lte specifies that this field must be less than or equal to the specified value, inclusive |
| gt | [sfixed32](#sfixed32) | optional | Gt specifies that this field must be greater than the specified value, exclusive. If the value of Gt is larger than a specified Lt or Lte, the range is reversed. |
| gte | [sfixed32](#sfixed32) | optional | Gte specifies that this field must be greater than or equal to the specified value, inclusive. If the value of Gte is larger than a specified Lt or Lte, the range is reversed. |
| in | [sfixed32](#sfixed32) | repeated | In specifies that this field must be equal to one of the specified values |
| not_in | [sfixed32](#sfixed32) | repeated | NotIn specifies that this field cannot be equal to one of the specified values |






<a name="is-validate-SFixed64Rules"></a>

### SFixed64Rules
SFixed64Rules describes the constraints applied to `sfixed64` values


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| const | [sfixed64](#sfixed64) | optional | Const specifies that this field must be exactly the specified value |
| lt | [sfixed64](#sfixed64) | optional | Lt specifies that this field must be less than the specified value, exclusive |
| lte | [sfixed64](#sfixed64) | optional | Lte specifies that this field must be less than or equal to the specified value, inclusive |
| gt | [sfixed64](#sfixed64) | optional | Gt specifies that this field must be greater than the specified value, exclusive. If the value of Gt is larger than a specified Lt or Lte, the range is reversed. |
| gte | [sfixed64](#sfixed64) | optional | Gte specifies that this field must be greater than or equal to the specified value, inclusive. If the value of Gte is larger than a specified Lt or Lte, the range is reversed. |
| in | [sfixed64](#sfixed64) | repeated | In specifies that this field must be equal to one of the specified values |
| not_in | [sfixed64](#sfixed64) | repeated | NotIn specifies that this field cannot be equal to one of the specified values |






<a name="is-validate-SInt32Rules"></a>

### SInt32Rules
SInt32Rules describes the constraints applied to `sint32` values


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| const | [sint32](#sint32) | optional | Const specifies that this field must be exactly the specified value |
| lt | [sint32](#sint32) | optional | Lt specifies that this field must be less than the specified value, exclusive |
| lte | [sint32](#sint32) | optional | Lte specifies that this field must be less than or equal to the specified value, inclusive |
| gt | [sint32](#sint32) | optional | Gt specifies that this field must be greater than the specified value, exclusive. If the value of Gt is larger than a specified Lt or Lte, the range is reversed. |
| gte | [sint32](#sint32) | optional | Gte specifies that this field must be greater than or equal to the specified value, inclusive. If the value of Gte is larger than a specified Lt or Lte, the range is reversed. |
| in | [sint32](#sint32) | repeated | In specifies that this field must be equal to one of the specified values |
| not_in | [sint32](#sint32) | repeated | NotIn specifies that this field cannot be equal to one of the specified values |






<a name="is-validate-SInt64Rules"></a>

### SInt64Rules
SInt64Rules describes the constraints applied to `sint64` values


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| const | [sint64](#sint64) | optional | Const specifies that this field must be exactly the specified value |
| lt | [sint64](#sint64) | optional | Lt specifies that this field must be less than the specified value, exclusive |
| lte | [sint64](#sint64) | optional | Lte specifies that this field must be less than or equal to the specified value, inclusive |
| gt | [sint64](#sint64) | optional | Gt specifies that this field must be greater than the specified value, exclusive. If the value of Gt is larger than a specified Lt or Lte, the range is reversed. |
| gte | [sint64](#sint64) | optional | Gte specifies that this field must be greater than or equal to the specified value, inclusive. If the value of Gte is larger than a specified Lt or Lte, the range is reversed. |
| in | [sint64](#sint64) | repeated | In specifies that this field must be equal to one of the specified values |
| not_in | [sint64](#sint64) | repeated | NotIn specifies that this field cannot be equal to one of the specified values |






<a name="is-validate-StringRules"></a>

### StringRules
StringRules describe the constraints applied to `string` values


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| const | [string](#string) | optional | Const specifies that this field must be exactly the specified value |
| min_len | [uint64](#uint64) | optional | MinLen specifies that this field must be the specified number of characters (Unicode code points) at a minimum. Note that the number of characters may differ from the number of bytes in the string. |
| max_len | [uint64](#uint64) | optional | MaxLen specifies that this field must be the specified number of characters (Unicode code points) at a maximum. Note that the number of characters may differ from the number of bytes in the string. |
| min_bytes | [uint64](#uint64) | optional | MinBytes specifies that this field must be the specified number of bytes at a minimum |
| max_bytes | [uint64](#uint64) | optional | MaxBytes specifies that this field must be the specified number of bytes at a maximum |
| pattern | [string](#string) | optional | Pattern specifes that this field must match against the specified regular expression (RE2 syntax). The included expression should elide any delimiters. |
| prefix | [string](#string) | optional | Prefix specifies that this field must have the specified substring at the beginning of the string. |
| suffix | [string](#string) | optional | Suffix specifies that this field must have the specified substring at the end of the string. |
| contains | [string](#string) | optional | Contains specifies that this field must have the specified substring anywhere in the string. |
| in | [string](#string) | repeated | In specifies that this field must be equal to one of the specified values |
| not_in | [string](#string) | repeated | NotIn specifies that this field cannot be equal to one of the specified values |
| email | [bool](#bool) | optional | Email specifies that the field must be a valid email address as defined by RFC 5322 |
| hostname | [bool](#bool) | optional | Hostname specifies that the field must be a valid hostname as defined by RFC 1034. This constraint does not support internationalized domain names (IDNs). |
| ip | [bool](#bool) | optional | Ip specifies that the field must be a valid IP (v4 or v6) address. Valid IPv6 addresses should not include surrounding square brackets. |
| ipv4 | [bool](#bool) | optional | Ipv4 specifies that the field must be a valid IPv4 address. |
| ipv6 | [bool](#bool) | optional | Ipv6 specifies that the field must be a valid IPv6 address. Valid IPv6 addresses should not include surrounding square brackets. |
| uri | [bool](#bool) | optional | Uri specifies that the field must be a valid, absolute URI as defined by RFC 3986 |
| uri_ref | [bool](#bool) | optional | UriRef specifies that the field must be a valid URI as defined by RFC 3986 and may be relative or absolute. |






<a name="is-validate-TimestampRules"></a>

### TimestampRules
TimestampRules describe the constraints applied exclusively to the
`google.protobuf.Timestamp` well-known type


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| required | [bool](#bool) | optional | Required specifies that this field must be set |
| const | [google.protobuf.Timestamp](#google-protobuf-Timestamp) | optional | Const specifies that this field must be exactly the specified value |
| lt | [google.protobuf.Timestamp](#google-protobuf-Timestamp) | optional | Lt specifies that this field must be less than the specified value, exclusive |
| lte | [google.protobuf.Timestamp](#google-protobuf-Timestamp) | optional | Lte specifies that this field must be less than the specified value, inclusive |
| gt | [google.protobuf.Timestamp](#google-protobuf-Timestamp) | optional | Gt specifies that this field must be greater than the specified value, exclusive |
| gte | [google.protobuf.Timestamp](#google-protobuf-Timestamp) | optional | Gte specifies that this field must be greater than the specified value, inclusive |
| lt_now | [bool](#bool) | optional | LtNow specifies that this must be less than the current time. LtNow can only be used with the Within rule. |
| gt_now | [bool](#bool) | optional | GtNow specifies that this must be greater than the current time. GtNow can only be used with the Within rule. |
| within | [google.protobuf.Duration](#google-protobuf-Duration) | optional | Within specifies that this field must be within this duration of the current time. This constraint can be used alone or with the LtNow and GtNow rules. |






<a name="is-validate-UInt32Rules"></a>

### UInt32Rules
UInt32Rules describes the constraints applied to `uint32` values


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| const | [uint32](#uint32) | optional | Const specifies that this field must be exactly the specified value |
| lt | [uint32](#uint32) | optional | Lt specifies that this field must be less than the specified value, exclusive |
| lte | [uint32](#uint32) | optional | Lte specifies that this field must be less than or equal to the specified value, inclusive |
| gt | [uint32](#uint32) | optional | Gt specifies that this field must be greater than the specified value, exclusive. If the value of Gt is larger than a specified Lt or Lte, the range is reversed. |
| gte | [uint32](#uint32) | optional | Gte specifies that this field must be greater than or equal to the specified value, inclusive. If the value of Gte is larger than a specified Lt or Lte, the range is reversed. |
| in | [uint32](#uint32) | repeated | In specifies that this field must be equal to one of the specified values |
| not_in | [uint32](#uint32) | repeated | NotIn specifies that this field cannot be equal to one of the specified values |






<a name="is-validate-UInt64Rules"></a>

### UInt64Rules
UInt64Rules describes the constraints applied to `uint64` values


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| const | [uint64](#uint64) | optional | Const specifies that this field must be exactly the specified value |
| lt | [uint64](#uint64) | optional | Lt specifies that this field must be less than the specified value, exclusive |
| lte | [uint64](#uint64) | optional | Lte specifies that this field must be less than or equal to the specified value, inclusive |
| gt | [uint64](#uint64) | optional | Gt specifies that this field must be greater than the specified value, exclusive. If the value of Gt is larger than a specified Lt or Lte, the range is reversed. |
| gte | [uint64](#uint64) | optional | Gte specifies that this field must be greater than or equal to the specified value, inclusive. If the value of Gte is larger than a specified Lt or Lte, the range is reversed. |
| in | [uint64](#uint64) | repeated | In specifies that this field must be equal to one of the specified values |
| not_in | [uint64](#uint64) | repeated | NotIn specifies that this field cannot be equal to one of the specified values |





 

 


<a name="is_msgs_validate-proto-extensions"></a>

### File-level Extensions
| Extension | Type | Base | Number | Description |
| --------- | ---- | ---- | ------ | ----------- |
| rules | FieldRules | .google.protobuf.FieldOptions | 919191 | Rules specify the validations to be performed on this field. By default, no validation is performed against a field. |
| disabled | bool | .google.protobuf.MessageOptions | 919191 | Disabled nullifies any validation rules for this message, including any message fields associated with it that do support validation. |
| required | bool | .google.protobuf.OneofOptions | 919191 | Required ensures that exactly one the field options in a oneof is set; validation fails if no fields in the oneof are set. |

 

 



## Scalar Value Types

| .proto Type | Notes | C++ | Java | Python | Go | C# | PHP | Ruby |
| ----------- | ----- | --- | ---- | ------ | -- | -- | --- | ---- |
| <a name="double" /> double |  | double | double | float | float64 | double | float | Float |
| <a name="float" /> float |  | float | float | float | float32 | float | float | Float |
| <a name="int32" /> int32 | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint32 instead. | int32 | int | int | int32 | int | integer | Bignum or Fixnum (as required) |
| <a name="int64" /> int64 | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint64 instead. | int64 | long | int/long | int64 | long | integer/string | Bignum |
| <a name="uint32" /> uint32 | Uses variable-length encoding. | uint32 | int | int/long | uint32 | uint | integer | Bignum or Fixnum (as required) |
| <a name="uint64" /> uint64 | Uses variable-length encoding. | uint64 | long | int/long | uint64 | ulong | integer/string | Bignum or Fixnum (as required) |
| <a name="sint32" /> sint32 | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int32s. | int32 | int | int | int32 | int | integer | Bignum or Fixnum (as required) |
| <a name="sint64" /> sint64 | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int64s. | int64 | long | int/long | int64 | long | integer/string | Bignum |
| <a name="fixed32" /> fixed32 | Always four bytes. More efficient than uint32 if values are often greater than 2^28. | uint32 | int | int | uint32 | uint | integer | Bignum or Fixnum (as required) |
| <a name="fixed64" /> fixed64 | Always eight bytes. More efficient than uint64 if values are often greater than 2^56. | uint64 | long | int/long | uint64 | ulong | integer/string | Bignum |
| <a name="sfixed32" /> sfixed32 | Always four bytes. | int32 | int | int | int32 | int | integer | Bignum or Fixnum (as required) |
| <a name="sfixed64" /> sfixed64 | Always eight bytes. | int64 | long | int/long | int64 | long | integer/string | Bignum |
| <a name="bool" /> bool |  | bool | boolean | boolean | bool | bool | boolean | TrueClass/FalseClass |
| <a name="string" /> string | A string must always contain UTF-8 encoded or 7-bit ASCII text. | string | String | str/unicode | string | string | string | String (UTF-8) |
| <a name="bytes" /> bytes | May contain any arbitrary sequence of bytes. | string | ByteString | str | []byte | ByteString | string | String (ASCII-8BIT) |
