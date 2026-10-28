# is-msgs-sea

Repositório que contém todas as definições padrão de mensagens protobuf do framework *is::*.
As definições `.proto` são usadas para gerar código em outras linguagens. Para usar o
código gerado, conheça as convenções da linguagem escolhida:
  - [C++](https://developers.google.com/protocol-buffers/docs/reference/cpp-generated)
  - [Javascript/ NodeJS](https://developers.google.com/protocol-buffers/docs/reference/javascript-generated)
  - [Python](https://developers.google.com/protocol-buffers/docs/reference/python-generated)

A documentação das mensagens e de seus campos está na [pasta docs](docs/README.md).

## *C++*
##### COMPILANDO A PARTIR DO CÓDIGO-FONTE
Instale previamente Python 3.10+, um compilador C++, Make e as ferramentas de
compilação exigidas pelas dependências. O bootstrap prepara Conan e CMake
com versões fixadas em um ambiente virtual local, sem instalar pacotes globais:
```shell
./bootstrap.sh # prepara .venv-cpp e um perfil Conan em .conan2
./build.sh # compila a biblioteca
```

Use `IS_MSGS_PYTHON=/caminho/python ./bootstrap.sh` para escolher o Python.
`./bootstrap.sh --help` mostra opções de caminhos alternativos. Para usar esses
caminhos, ative o ambiente criado e defina `CONAN_HOME` antes de executar o build.
##### CONAN PACKAGE
Um artefato Conan está disponível em nosso laboratório. **Entre em contato com os
mantenedores para obter acesso ao servidor Conan; ele não é público.**

##### USAGE

```c++
#include <is/msgs/common.pb.h>

is::common::Tensor tensor;
```

As conversões em `is/utils/cv.hpp` aceitam matrizes 2D com um canal. Dimensões,
tipos ou buffers incompatíveis produzem uma matriz/tensor vazio. A função
`to_mat` copia os dados; `to_mat_view` compartilha o buffer, que precisa continuar
vivo e sem realocação enquanto a view for usada.

## *Javascript / NodeJS*
O suporte JavaScript é histórico e **não é suportado nesta versão**. Não há
geração ou publicação Node nos workflows atuais, nem testes JavaScript. O `package.json`
foi preservado para referência, mas seus comandos usam caminhos antigos e não
constituem uma receita de build validada. A retomada exige um gerador moderno,
lockfile e testes de serialização; a remoção deve ocorrer somente em uma major
futura, após aviso de migração.

## *Python*

A documentação do pacote Python está em [python/README.md](python/README.md).

The modern Python distribution is `is-msgs-sea`; imports remain
`is_msgs`. It supports Python 3.10–3.14 and Protobuf 5–7. See the
[migration guide](MIGRATION.md) and [compatibility policy](COMPATIBILITY.md).

```shell
uv add is-msgs-sea
```

## Publicando novas versões

Primeiro, atualize a versão no arquivo `.version`, seguindo o padrão `^[0-9]+\.[0-9]+\.[0-9]+$`.
Python, Conan e CMake usam esse arquivo como fonte única da versão do pacote.

#### Etapas após a publicação

Revise `docs/README.md` e `docs/ROS_FIELDS.md` quando os schemas mudarem: os
workflows atuais não regeneram a documentação automaticamente. Faça commit e
push das alterações e crie uma tag Git para a nova versão:

```shell
git tag v$(cat .version)
git push origin v$(cat .version)
```

### Python

Para publicar uma nova versão Python, consulte [python/README.md](python/README.md).

### C++

O Conan e o CMake usam a mesma versão do Python. Consulte [PUBLISHING.md](PUBLISHING.md)
para validar e criar o pacote C++ e consumir a instalação com `find_package`.

## Acknowledgements

A modernização, a revisão de compatibilidade, o trabalho de segurança de tipos, os testes
e o empacotamento no PyPI das séries 1.2 e 1.3 foram realizados com assistência do
OpenAI Codex.
