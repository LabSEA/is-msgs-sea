# Preparação e publicação de releases

O pacote Python deste projeto se chama `is-msgs-sea` e é publicado automaticamente no PyPI pelo GitHub Actions.

O pacote C++ se chama `is-msgs`. Python, Conan e CMake leem a mesma versão de
`.version`; a release preparada neste checkout é `1.3.2`. O número da versão
do pacote é independente da dependência Protobuf de cada linguagem.

## Como funciona

O workflow está em:

```text
.github/workflows/publish.yml
```

Ele é acionado quando uma tag no formato `v*` é enviada para o GitHub. O workflow:

1. executa a validação reutilizável de testes, geração e compatibilidade;
2. gera os arquivos `.whl` e `.tar.gz`, valida com Twine e testa o wheel em um ambiente limpo;
3. verifica se a tag corresponde à versão definida em `.version`;
4. obtém esses mesmos artefatos validados, sem recompilar;
5. publica os arquivos no PyPI usando Trusted Publishing/OIDC.

Não é necessário criar um GitHub Release manualmente.

## Publicar uma nova versão

Primeiro, atualize o arquivo `.version`. Por exemplo:

```text
1.3.2
```

Revise as alterações e atualize o changelog e a documentação. Em um ambiente
virtual com Python 3.12 ou 3.13, valide antes de criar o commit:

```bash
python -m pip install -e '.[dev,codegen]'
pytest
ruff check python scripts conanfile.py package.py test_package/conanfile.py
basedpyright python/tests/unit/test_is_msgs.py
python scripts/check_descriptor_compatibility.py
python scripts/check_descriptor_compatibility.py --latest-release
python scripts/generate_python.py
git diff -- python/is_msgs
python -m build
twine check --strict dist/is_msgs_sea-1.3.2*
```

O checker requer a tag upstream `v1.1.18`, obtida pela CI. A geração não deve
alterar os artefatos versionados. Teste o wheel também fora do checkout, em
um ambiente virtual limpo, como faz o workflow de validação.

A CI executa a suíte também com o extra `codegen`, além da matriz de runtimes.
O segundo checker seleciona uma tag estável alcançável no histórico; na própria
tag da release limpa ele seleciona a anterior. Use checkout com tags e histórico
completos para essas verificações.

Inclua todas as alterações revisadas no commit, inclusive novos testes,
scripts e `AGENTS.md`. Confira o conteúdo preparado e envie a branch principal:

```bash
git add -A
git diff --cached --stat
git commit -m "release: v1.3.2"
git push origin main
```

Crie e envie uma tag com exatamente a mesma versão:

```bash
git tag v1.3.2
git push origin v1.3.2
```

O envio da tag iniciará automaticamente o workflow de publicação.

## Pacote C++ / Conan

O Conan resolve a versão diretamente de `.version`, inclusive ao exportar a
receita. O CMake usa esse mesmo valor em `project(VERSION ...)` e instala
`is-msgsConfigVersion.cmake` para consumidores que exigem uma versão:

```cmake
find_package(is-msgs 1.3.2 CONFIG REQUIRED)
target_link_libraries(my_app PRIVATE is-msgs::is-msgs)
```

Em um ambiente com Conan 2, CMake 3.15–3.31, compilador e dependências
disponíveis, valide e crie o pacote local. As dependências antigas da receita
usam compatibilidade removida pelo CMake 4:

```bash
conan inspect . --format=json
conan create . --user=is --channel=stable -b missing -o 'is-msgs/*:build_tests=True'
```

O pacote será `is-msgs/1.3.2@is/stable`. O Protobuf C++ continua em 3.20.0.
O workflow PyPI não publica pacotes Conan; a distribuição C++ depende do
servidor privado do laboratório.

Para consumidores com bibliotecas compartilhadas no cache Conan, ative o
`conanrun.sh` gerado antes de compilar e executar os testes, para que o linker
e o processo encontrem essas dependências.

A CI cobre builds CMake estáticos e compartilhados, a suíte nativa com OpenCV,
a instalação CMake e o consumidor em `test_package`. Um job separado executa
`conan create` e o mesmo consumidor para as duas opções de linkage. O cache
Conan reduz o custo de recompilar dependências; a primeira execução pode demorar.

## Atualização das dependências C++ em uma release posterior

A 1.3.2 preserva Protobuf 3.20.0, fmt 5.3.0 e Boost 1.80.0. A atualização
de dependências deve começar após essa release, em uma branch própria:

1. registrar os artefatos e fixtures binárias da 1.3.2 como referência;
2. atualizar primeiro fmt e Boost, uma dependência por vez, mantendo os testes
   de build estático, compartilhado e consumo CMake/Conan;
3. atualizar juntos o compilador e o runtime Protobuf C++, revisando as APIs
   usadas em `io.cpp`, geração CMake e validação de mensagens;
4. avaliar o requisito de linguagem/compilador das versões escolhidas antes
   de alterar o mínimo C++11 documentado;
5. testar CMake 4 com as dependências novas e retirar o limite `<4` somente
   depois de a matriz nativa passar;
6. repetir as comparações de descritores com o upstream e a última release,
   além de fixtures trocadas entre Python e C++, antes de versionar/publicar.

## Configuração do Trusted Publisher

O projeto no PyPI deve possuir um Trusted Publisher configurado com estes dados:

```text
Owner: LabSEA
Repository name: is-msgs-sea
Workflow name: publish.yml
Environment name: pypi
```

No GitHub, o ambiente `pypi` deve existir em:

```text
Settings > Environments > pypi
```

O workflow utiliza a permissão `id-token: write` para autenticar no PyPI sem armazenar um token permanente como secret.

## Verificar a publicação

Depois que o workflow terminar, verifique:

- a execução em `Actions > Publish to PyPI`;
- a versão em <https://pypi.org/project/is-msgs-sea/>;
- a instalação em um ambiente limpo:

```bash
python -m pip install is-msgs-sea==1.3.2
```

Substitua `1.3.2` pela versão publicada.

## Atenção às versões

Uma versão já publicada não pode ser substituída no PyPI. Portanto, depois de publicar `1.3.2`, não tente publicar novamente a mesma versão com arquivos diferentes. Crie uma nova versão, como `1.3.3`.

O workflow usa `skip-existing: true` para que uma reexecução não falhe quando os mesmos arquivos já estiverem publicados. Isso não substitui arquivos existentes; apenas permite que a execução prossiga.
