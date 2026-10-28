#include <is/msgs/camera.pb.h>
#include <is/msgs/image.pb.h>
#include <is/msgs/robot.pb.h>
#include <is/msgs/ros.pb.h>
#include <is/utils/io.hpp>
#include <is/utils/timestamp.hpp>
#include <is/utils/validate.hpp>

#include <chrono>
#include <stdexcept>

int main() {
  // Same pre-1.2 wire fixture exercised by the Python runtime matrix.
  const std::string fixture("\x0d\x00\x00\x80\x3f\x15\x00\x00\x00\x40\x1d\x00\x00\x40\x40", 15);
  is::common::Position legacy;
  if (!legacy.ParseFromString(fixture) || legacy.x() != 1 || legacy.y() != 2 ||
      legacy.z() != 3 || legacy.SerializeAsString() != fixture) return 5;

  is::common::Position original;
  original.set_x(1.5f);
  original.mutable_precise()->set_y(2.5);
  is::save("consumer.json", original);
  is::common::Position restored;
  is::load("consumer.json", &restored);
  if (restored.SerializeAsString() != original.SerializeAsString()) return 1;

  is::vision::Image image;
  image.set_sequence(12);
  image.set_timestamp_source(is::vision::TIMESTAMP_SOURCE_CAMERA);
  *image.mutable_header()->mutable_stamp() =
      is::to_timestamp(std::chrono::system_clock::now());
  if (image.header().stamp().seconds() == 0) return 2;

  is::robot::Imu imu;
  imu.mutable_orientation()->set_w(1.0);
  is::ros::TFMessage transforms;
  transforms.add_transforms()->set_child_frame_id("sensor");
  if (imu.orientation().w() != 1.0 || transforms.transforms_size() != 1) return 3;

  is::vision::CameraSetting setting;
  setting.set_ratio(2.0f);
  try {
    is::validate_message(setting);
  } catch (const std::runtime_error&) {
    return 0;
  }
  return 4;
}
