# Especificação do GitFlow (`code/SPECS-git.md`)
> Diretrizes de ramificação, commits e governança de versões para todo o repositório.

## Estrutura de Branches (GitFlow)

| Branch | Propósito | Regras |
|---|---|---|
| `main` | Versões de entrega / Release final | Nunca commitar diretamente. Apenas recebe merges revisados de `develop` ou `release/*`. |
| `develop` | Branch principal de integração | Todos os experimentos e seções do artigo convergem aqui. Deve sempre estar funcional. |
| `feature/<nome>` | Novos modelos ou seções | Criada a partir de `develop`. Ex: `feature/explicit-graph`, `feature/experimentos-convergencia`. |
| `release/<versao>` | Preparação para entrega final | Criada a partir de `develop` para ajustes finos antes de ir para `main`. |
| `hotfix/<nome>` | Correção urgente | Criada a partir de `main` para correções imediatas de última hora. |

---

## Fluxo de Trabalho Prático

### 1. Iniciar uma nova tarefa
```bash
git checkout develop
git pull origin develop
git checkout -b feature/minha-tarefa
```

### 2. Trabalhar e salvar progresso
```bash
git add .
git commit -m "feat(code): implementar camada densa com suporte a retropropagacao"
```

### 3. Integrar com a branch develop
```bash
git checkout develop
git merge --no-ff feature/minha-tarefa
git branch -d feature/minha-tarefa
```
