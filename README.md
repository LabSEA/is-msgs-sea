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
Para compilar esta biblioteca, execute primeiro o script de preparação das dependências
e depois o script de build.
```shell
./bootstrap.sh # obtém as dependências de build
./build.sh # compila a biblioteca
```
##### CONAN PACKAGE
Um artefato Conan está disponível em nosso laboratório. **Entre em contato com os
mantenedores para obter acesso ao servidor Conan; ele não é público.**

##### USAGE

```c++
#include <is/msgs/common.pb.h>

is::common::Tensor tensor;
```

## *Javascript / NodeJS*
Para usar protocol buffers com JavaScript, você precisa do compilador *protoc*; baixe um
[binário pré-compilado no GitHub](https://github.com/google/protobuf/releases).

Instale as dependências de build e compile os schemas `.proto` para arquivos `.js`:
```shell
npm install # obtém as dependências de build
npm run generate # gera os arquivos js
```

Para usar no lado do servidor (Node.js), importe e use os arquivos gerados:
```js
const common = require("./is/msgs/common_pb.js");

let tensor = new common.Tensor();
tensor.setDoublesList([1, 2, 3]);
console.log(tensor.toObject());
// ...
```

Para usar no navegador, empacote os arquivos com browserify:
```shell
npm run browserify 
```

Depois, inclua o bundle gerado no navegador:
```html
<script src="is_msgs.js"></script>
<script>
  var tensor = new proto.is.msgs.common.Tensor();
  tensor.setDoublesList([1, 2, 3]);
  console.log(tensor.toObject());
</script>
// ...
```

## *Python*

A documentação do pacote Python está em [python/README.md](python/README.md).

The modern Python distribution is `is-msgs-sea==1.3.0`; imports remain
`is_msgs`. It supports Python 3.10–3.14 and Protobuf 5–7. See the
[migration guide](MIGRATION.md) and [compatibility policy](COMPATIBILITY.md).

```shell
uv add is-msgs-sea
```

## Publicando novas versões

Primeiro, atualize a versão no arquivo `.version`, seguindo o padrão `^[0-9]+\.[0-9]+\.[0-9]+$`.

#### Etapas após a publicação

Após publicar `is_msgs` em qualquer linguagem, a documentação dos protobufs em
`docs/README.md` será atualizada automaticamente. Faça commit e push dessas alterações
e crie uma tag Git para a nova versão:

```shell
git tag v$(cat .version)
git push origin v$(cat .version)
```

### Python

Para publicar uma nova versão Python, consulte [python/README.md](python/README.md).

### C++

> Under construction

## Acknowledgements

A modernização, a revisão de compatibilidade, o trabalho de segurança de tipos, os testes
e o empacotamento no PyPI das séries 1.2 e 1.3 foram realizados com assistência do
OpenAI Codex.
