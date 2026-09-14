# Convenções dos campos ROS

- `Header.stamp` é um timestamp Unix dividido em segundos e nanossegundos;
  `frame_id` é copiado literalmente.
- Posições lineares, translações, velocidades, acelerações, distâncias e nuvens
  de pontos usam as convenções SI do ROS (normalmente metros e metros por segundo).
- Ângulos e velocidades angulares usam radianos e radianos por segundo.
- Quaternions usam `(x, y, z, w)` sem normalização pela biblioteca.
- Covariâncias de pose e velocidade são arrays row-major 6×6 (36 doubles).
  Covariâncias de IMU são arrays row-major 3×3 (9 doubles).
- `RawImage.data` é o buffer de imagem ROS original em ordem de linhas. `step`
  inclui o preenchimento das linhas e `is_bigendian` é preservado.
- `Image.data` contém bytes JPEG, PNG ou WebP codificados, nunca base64.
- `PointCloud.data` e cada offset/tipo/quantidade de PointField preservam
  exatamente o layout de `sensor_msgs/PointCloud2`.
- NaN e infinito são valores de sensor válidos e não são sanitizados.
