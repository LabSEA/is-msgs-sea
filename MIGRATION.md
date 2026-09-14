# Migrando do is-msgs 1.1.18

1. Remova `is-msgs` e instale `is-msgs-sea==1.3.0`. As duas distribuições usam
   o mesmo pacote `is_msgs` e não podem coexistir.
2. Mantenha imports existentes, como `from is_msgs.common_pb2 import Pose`.
3. Consumidores existentes de Pose, Speed, Position, Orientation e RangeScan
   podem adotar gradualmente os campos aditivos.
4. Mapeie `sensor_msgs/Image` para `is.vision.RawImage`. `is.vision.Image`
   representa explicitamente bytes JPEG/PNG/WebP já comprimidos ou uma URI.
5. Use `is.vision.CompressedImage` para `sensor_msgs/CompressedImage` e
   preserve sua string de formato ROS.
6. Preserve `PointCloud.data` como o buffer de bytes original do PointCloud2;
   não o expanda para listas de ponto flutuante ou base64.
7. Produtores de imagens devem preencher `Image.header.stamp`, `sequence` e
   `timestamp_source`. Leitores de versões antigas ignoram esses campos com
   segurança.

Consulte [convenções de campos ROS](docs/ROS_FIELDS.md) para unidades e layouts.
