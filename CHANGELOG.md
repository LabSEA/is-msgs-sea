# Registro de alterações

## 1.3.2

- Executa testes com codegen na CI e compara descritores com a última release
  estável alcançável, além do baseline histórico.
- Adiciona CI C++ para builds estáticos e compartilhados, CTest, instalação
  CMake e consumo de pacotes Conan com `test_package`.
- Corrige a propagação pública de Protobuf e a dependência Boost.Filesystem
  nos metadados Conan; evita conflito entre target agregado e componente.
- Substitui o bootstrap global por ferramentas fixadas em ambiente virtual
  e cache Conan locais, com validação correta da versão do CMake.
- Valida dimensões, tipos, canais e tamanhos de buffers nas conversões OpenCV,
  incluindo views, cópias e matrizes não contíguas nos testes.
- Aceita os targets OpenCV/GTest fornecidos por instalações nativas e Conan.
- Amplia o checker para extensões, presença, mapas, oneofs, reservas, serviços
  e opções de arquivo; aceita reordenações semanticamente equivalentes.
- Gera Python em staging antes de substituir artefatos, remove arquivos stale
  após sucesso e transforma imports com comentários, whitespace, public e weak.
- Compartilha a lista explícita de schemas com CMake, incluindo ros.proto em C++.
- Preserva caminhos is/msgs e is/utils na instalação CMake e resolve fmt em
  downstreams. Não atualiza a linha Protobuf C++.
- Faz a publicação depender da validação e reutiliza os mesmos artefatos testados.
- Documenta JavaScript como não suportado, preservando os arquivos históricos.
- Unifica a versão Python, Conan e CMake em `.version` e instala metadados
  para consultas de versão com `find_package(is-msgs 1.3.2 CONFIG REQUIRED)`.
- Limita a exportação de fontes Conan aos arquivos necessários para compilar,
  evitando incluir o histórico Git, caches e distribuições Python antigas.
- Adiciona `AGENTS.md` com convenções de desenvolvimento e validação de releases.

## 1.3.1

- Regenera os módulos de imagem com a versão fixada do gerador Protobuf.

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
