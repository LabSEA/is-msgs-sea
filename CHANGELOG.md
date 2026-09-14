# Registro de alterações

## 1.3.0

- Added acquisition `header`, monotonic `sequence`, and `timestamp_source` to
  `is.vision.Image` without changing the existing `data` and `uri` fields.
- Added explicit camera and gateway-receive timestamp source values for
  synchronized computer-vision pipelines.
- Verified descriptor compatibility with every message and enum from 1.1.18.

## 1.2.0

- Renamed the Python distribution to `is-msgs-sea` while preserving `is_msgs`
  imports.
- Added typed, reproducibly generated Python modules for Python 3.10–3.14 and
  Protobuf 5–7.
- Added ROS-compatible headers, precise vectors/quaternions, transforms,
  covariance-bearing pose/speed, raw/compressed images, complete scans, IMU,
  odometry, binary point clouds, `ROSMessage`, and TF schemas.
- Kept every pre-1.2 field and enum wire-compatible with 1.1.18.
- Replaced install-time compiler downloads with an explicit `codegen` extra.
- Updated the project repository and LabSEA contact metadata.
- Acknowledged OpenAI Codex assistance with modernization, compatibility review,
  type-safety work, testing, and PyPI packaging.
