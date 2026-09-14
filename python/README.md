# is-msgs-sea para Python

A distribuição se chama `is-msgs-sea`; o pacote de import continua sendo
`is_msgs`, portanto o código existente não precisa mudar.

```shell
uv remove is-msgs
uv add is-msgs-sea==1.3.0
```

Python 3.10 a 3.14 e Protobuf 5 a 7 são suportados. Não instale
`is-msgs` e `is-msgs-sea` juntos, pois ambos fornecem `is_msgs`.

## Compilando protos da aplicação

Instale o compilador opcional e invoque o módulo sem alterar o diretório do
projeto:

```shell
uv add 'is-msgs-sea[codegen]==1.3.0'
uv run python -m is_msgs.utils.build --output generated proto/my_service.proto
```

Os schemas da aplicação podem manter o import canônico:

```protobuf
import "is/msgs/common.proto";
```

O wheel instalado já contém `*_pb2.py` gerados, stubs de tipos e imports
transformados. A instalação nunca baixa o `protoc` nem gera código.

## Geração reproduzível no repositório

```shell
uv sync --extra codegen
uv run python scripts/generate_python.py
git diff --exit-code
```

Gere e valide uma versão com:

```shell
uv build
uv publish --dry-run dist/*
```

Após autorização explícita, publique esses artefatos exatos com `uv publish
dist/*`.
