# Publicação no PyPI

O pacote Python deste projeto se chama `is-msgs-sea` e é publicado automaticamente no PyPI pelo GitHub Actions.

## Como funciona

O workflow está em:

```text
.github/workflows/publish.yml
```

Ele é acionado quando uma tag no formato `v*` é enviada para o GitHub. O workflow:

1. verifica se a tag corresponde à versão definida em `.version`;
2. gera os arquivos `.whl` e `.tar.gz`;
3. valida os pacotes com o Twine;
4. publica os arquivos no PyPI usando Trusted Publishing/OIDC.

Não é necessário criar um GitHub Release manualmente.

## Publicar uma nova versão

Primeiro, atualize o arquivo `.version`. Por exemplo:

```text
1.3.1
```

Revise as alterações, atualize a documentação quando necessário e execute os testes. Depois faça o commit e envie a branch principal:

```bash
git add .version README.md CHANGELOG.md
git commit -m "release: v1.3.1"
git push origin main
```

Crie e envie uma tag com exatamente a mesma versão:

```bash
git tag v1.3.1
git push origin v1.3.1
```

O envio da tag iniciará automaticamente o workflow de publicação.

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
python -m pip install is-msgs-sea==1.3.1
```

Substitua `1.3.1` pela versão publicada.

## Atenção às versões

Uma versão já publicada não pode ser substituída no PyPI. Portanto, depois de publicar `1.3.1`, não tente publicar novamente a mesma versão com arquivos diferentes. Crie uma nova versão, como `1.3.2`.

O workflow usa `skip-existing: true` para que uma reexecução não falhe quando os mesmos arquivos já estiverem publicados. Isso não substitui arquivos existentes; apenas permite que a execução prossiga.
