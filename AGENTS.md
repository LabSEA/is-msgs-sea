# Orientações para trabalhar neste repositório

## Estrutura e fontes de verdade

- Este projeto distribui schemas Protocol Buffers do framework `is::` em Python
  (`is-msgs-sea`, import `is_msgs`) e C++ (`is-msgs`, CMake/Conan).
- Edite schemas em `src/is/msgs/*.proto`. A lista compartilhada de schemas fica
  em `src/schema_manifest.txt`; atualize-a ao adicionar um arquivo.
- `python/is_msgs/*.proto`, `*_pb2.py` e `*_pb2.pyi` são artefatos gerados.
  Regenere-os com `scripts/generate_python.py`, sem editá-los manualmente.
- Utilitários C++ ficam em `src/is/utils`; o compilador de protos da aplicação
  fica em `python/is_msgs/utils/build.py`.
- `.version` é a fonte única da versão Python, Conan e CMake, no formato
  `MAJOR.MINOR.PATCH`. O `package.json` é histórico e não participa da release.

## Compatibilidade

- Preserve nomes, números e tipos dos campos e valores de enums existentes.
  Siga `COMPATIBILITY.md`; remoções exigem uma major e revisão de migração.
- O baseline do checker é a tag upstream `v1.1.18`. Não substitua esse baseline
  permanentemente pela versão atual para fazer uma verificação passar.
- Execute também o checker com `--latest-release`, que protege os campos
  adicionados após o baseline histórico. A seleção usa tags estáveis alcançáveis
  e compara uma tag de release limpa com a versão anterior, sem comparar consigo mesma.
- Preserve os imports públicos `is_msgs` e os caminhos canônicos
  `is/msgs/*.proto`, inclusive em protos de aplicações consumidoras.
- Python suporta 3.10–3.14 e Protobuf `>=5.29,<8`; o gerador usa
  `grpcio-tools==1.69.0`. Para geração local, use Python 3.12 ou 3.13.
- A receita C++ usa C++11 e Protobuf 3.20.0. O número da release do pacote é
  compartilhado entre linguagens; versões dos runtimes Protobuf são independentes.
- Preserve unidades, covariâncias e buffers conforme `docs/ROS_FIELDS.md`.
- JavaScript está sem suporte; não apresente os scripts Node como validados.

## Validação Python

Em um ambiente virtual com Python 3.12 ou 3.13:

```sh
python -m pip install -e '.[dev,codegen]'
pytest
ruff check python scripts conanfile.py package.py test_package/conanfile.py
basedpyright python/tests/unit/test_is_msgs.py
python scripts/check_descriptor_compatibility.py
python scripts/check_descriptor_compatibility.py --latest-release
python scripts/generate_python.py
```

O checker requer a tag `v1.1.18` do repositório upstream, obtida pela CI.
Verifique que a geração não muda os artefatos versionados. Use o extra
`codegen` na validação para executar os testes de compilação sem skips.

## Validação C++ e release

- Valide a receita Conan e a versão resolvida de `.version`. Em um ambiente
  com dependências disponíveis, compile com Conan 2/CMake 3.15–3.31 e execute
  CTest. As dependências antigas da receita não suportam CMake 4 sem ajustes.
- `bootstrap.sh` prepara ferramentas fixadas em `scripts/cpp-tools.txt` dentro
  de `.venv-cpp` e detecta um perfil no cache local `.conan2`. Não instala
  pacotes do sistema nem altera o cache Conan global. `build.sh` usa esses caminhos.
- A CI cobre CMake/CTest e consumidores instalados nas variantes estática e
  compartilhada, além de `conan create` com `test_package` nas duas variantes.
- Verifique também um consumidor da instalação CMake: os headers devem manter
  `is/msgs` e `is/utils`, e `find_package(is-msgs <versão> CONFIG REQUIRED)` deve
  encontrar os metadados da versão.
- Para consumidores com dependências compartilhadas no cache Conan, ative o
  `conanrun.sh` gerado antes da compilação e da execução dos testes.
- As conversões OpenCV aceitam matrizes 2D com um canal e tensores row-major
  com buffer do tamanho exato. Entradas inválidas retornam resultados vazios.
  Views deixam de ser válidas quando o tensor é destruído ou seu buffer muda.
- Ao preparar uma release, atualize `.version`, `CHANGELOG.md` e os exemplos
  de `PUBLISHING.md`; documente mudanças de schemas nos arquivos de `docs`.
- Gere wheel e sdist com `python -m build`, valide com `twine check --strict`
  e teste o wheel fora do checkout em um ambiente virtual limpo.
- O workflow de publicação reutiliza os artefatos da validação. A tag Git
  deve ser `v` seguido da versão de `.version`.
- Informe quais verificações foram executadas e eventuais limitações. Preserve
  alterações locais existentes e não inclua artefatos de build nos commits.
