# Política de compatibilidade

`is-msgs-sea` segue regras de evolução aditiva do Protobuf:

- nomes e números de campos existentes, tipos escalares/de mensagem, nomes de
  enums e números de enums não são alterados;
- tags e nomes removidos devem ser declarados como `reserved` em uma versão
  futura;
- novos campos devem usar novos números de tag, e leitores antigos devem
  ignorá-los;
- os bytes Protobuf serializados, e não a saída JSON, definem a
  compatibilidade do wire;
- as versões Python suportam Python 3.10–3.14 com Protobuf 5–7.

A CI compara a superfície atual dos descritores com a tag `v1.1.18`.
O arquivo `validate.proto` permaneceu intencionalmente inalterado na 1.2.0,
pois suas extensões fazem parte dessa superfície.
