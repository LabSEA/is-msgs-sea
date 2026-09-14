from is_msgs.camera_pb2 import CameraCalibration, CameraConfig
from is_msgs.common_pb2 import (
    Header,
    Orientation,
    Pose,
    Position,
    Quaternion,
    Speed,
    TransformStamped,
    Twist,
    Vector3,
)
from is_msgs.image_pb2 import (
    TIMESTAMP_SOURCE_GATEWAY_RECEIVE,
    CompressedImage,
    Image,
    RawImage,
)
from is_msgs.power_pb2 import PowerInfo
from is_msgs.robot_pb2 import Imu, Odometry, PointCloud, RangeScan
from is_msgs.ros_pb2 import ROSMessage, TFMessage


def test_all_public_modules_import():
    assert CameraConfig.DESCRIPTOR.full_name == "is.vision.CameraConfig"
    assert CameraCalibration.DESCRIPTOR.full_name == "is.vision.CameraCalibration"
    assert PowerInfo.DESCRIPTOR.full_name == "is.common.PowerInfo"
    assert ROSMessage.DESCRIPTOR.full_name == "is.ros.ROSMessage"


def test_legacy_geometry_fields_and_numbers_are_preserved():
    assert Position.DESCRIPTOR.fields_by_name["x"].number == 1
    assert Position.DESCRIPTOR.fields_by_name["y"].number == 2
    assert Position.DESCRIPTOR.fields_by_name["z"].number == 3
    assert Orientation.DESCRIPTOR.fields_by_name["yaw"].number == 1
    assert Pose.DESCRIPTOR.fields_by_name["position"].number == 1
    assert Speed.DESCRIPTOR.fields_by_name["linear"].number == 1
    assert RangeScan.DESCRIPTOR.fields_by_name["angles"].number == 1
    assert RangeScan.DESCRIPTOR.fields_by_name["ranges"].number == 2


def test_legacy_position_binary_fixture_is_unchanged():
    # is.common.Position(x=1, y=2, z=3) serialized by is-msgs 1.1.18.
    fixture = bytes.fromhex("0d0000803f15000000401d00004040")
    position = Position.FromString(fixture)

    assert (position.x, position.y, position.z) == (1.0, 2.0, 3.0)
    assert not position.HasField("precise")
    assert position.SerializeToString(deterministic=True) == fixture


def test_precise_geometry_round_trip():
    pose = Pose(
        position=Position(
            x=1.5,
            y=2.5,
            z=3.5,
            precise=Vector3(x=1.5, y=2.5, z=3.5),
        ),
        orientation=Orientation(
            yaw=0.1,
            pitch=0.2,
            roll=0.3,
            quaternion=Quaternion(x=0.0, y=0.0, z=0.1, w=0.99),
        ),
        header=Header(frame_id="map"),
    )
    decoded = Pose.FromString(pose.SerializeToString())
    assert decoded == pose
    assert decoded.position.precise.x == 1.5
    assert decoded.orientation.quaternion.w == 0.99


def test_sensor_payloads_preserve_binary_buffers():
    raw = RawImage(encoding="rgb8", step=6, data=b"\x00\x01\x02\x03\x04\x05")
    compressed = CompressedImage(format="jpeg", image=Image(data=b"\xff\xd8\xff\xd9"))
    cloud = PointCloud(height=1, width=1, point_step=16, row_step=16, data=bytes(range(16)))

    assert RawImage.FromString(raw.SerializeToString()) == raw
    assert CompressedImage.FromString(compressed.SerializeToString()) == compressed
    assert PointCloud.FromString(cloud.SerializeToString()).data == bytes(range(16))


def test_image_capture_metadata_is_additive_and_round_trips():
    legacy_fixture = Image(data=b"legacy").SerializeToString(deterministic=True)
    stamped = Image(
        data=b"jpeg",
        header=Header(frame_id="camera-5"),
        sequence=42,
        timestamp_source=TIMESTAMP_SOURCE_GATEWAY_RECEIVE,
    )
    stamped.header.stamp.FromNanoseconds(1_700_000_000_123_456_789)

    assert Image.FromString(legacy_fixture).data == b"legacy"
    decoded = Image.FromString(stamped.SerializeToString())
    assert decoded.sequence == 42
    assert decoded.header.frame_id == "camera-5"
    assert decoded.header.stamp.ToNanoseconds() == 1_700_000_000_123_456_789
    assert decoded.timestamp_source == TIMESTAMP_SOURCE_GATEWAY_RECEIVE


def test_robotics_messages_and_tf_round_trip():
    imu = Imu(orientation=Quaternion(w=1.0), angular_velocity=Vector3(z=0.5))
    odometry = Odometry(child_frame_id="base_link")
    transform = TransformStamped(child_frame_id="camera")
    tf_message = TFMessage(transforms=[transform])
    speed = Speed(twist=Twist(linear=Vector3(x=1.0)))

    assert Imu.FromString(imu.SerializeToString()) == imu
    assert Odometry.FromString(odometry.SerializeToString()) == odometry
    assert TFMessage.FromString(tf_message.SerializeToString()) == tf_message
    assert speed.twist.linear.x == 1.0
