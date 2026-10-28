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
Também compara com a release estável mais recente alcançável no histórico,
usando `--latest-release`, para proteger as adições posteriores. Na validação
de uma tag de release limpa, essa tag é excluída para evitar uma comparação
consigo mesma; durante o desenvolvimento, a release já ancestral é protegida.
O arquivo `validate.proto` permaneceu intencionalmente inalterado na 1.2.0,
pois suas extensões fazem parte dessa superfície.

O checker também protege extensões (inclusive validate.rules), presença,
oneofs por nome, mapas, defaults, packing efetivo, reservas, serviços e as
opções de arquivo que alteram APIs geradas. Ele rejeita remoções mesmo quando
reservadas; remoções pertencem a uma major com revisão de migração. Reservas
podem ser ampliadas. Opções customizadas de validação exigem revisão semântica
separada: mudar uma regra não é uma mudança de formato binário.

A lista de schemas de Python e C++ é `src/schema_manifest.txt`. Ao adicionar um
schema, atualize esse manifesto; a geração falha se houver drift. A geração só
substitui artefatos após sucesso do protoc e usa replace atômico por arquivo;
ela não é uma transação de todo o diretório sob interrupção do sistema.

Para comparar outra referência Git local, use
`python scripts/check_descriptor_compatibility.py --baseline-ref <ref>`.
O default continua sendo a tag upstream `v1.1.18`, buscada pela CI.
