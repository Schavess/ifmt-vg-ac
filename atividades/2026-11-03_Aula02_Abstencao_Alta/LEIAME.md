# Prática: abstenção alta em MT, o primeiro classificador

AC • 4º TIA • 03/11/2026 • Aula 02 • apostila: cap. 2, 4, 5, 9 e 12

**Pergunta:** a partir do perfil do eleitorado, dá para apontar quais municípios de Mato Grosso tiveram **abstenção alta** (25% ou mais) no 1º turno de 2026?

## Objetivo

Fazer um experimento de classificação completo e honesto, do zero:
**alvo (y) e features (X) → treino/teste → baseline → modelo → matriz de confusão → limiar de decisão**.
No fim, você deve saber explicar por que uma acurácia de 69% pode não valer nada.

## Como abrir

**No Google Colab (recomendado)**
1. Abra o notebook pelo botão abaixo. Ele lê os dados do GitHub da disciplina, então precisa de internet.

   [![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Schavess/ifmt-vg-ac/blob/main/atividades/2026-11-03_Aula02_Abstencao_Alta/2026-11-03_Aula02_Abstencao_Alta_INICIAL.ipynb)

2. **Arquivo > Salvar uma cópia no Drive**, para não perder o que fizer.
3. Se a célula 1 der erro de leitura, arraste o arquivo `dados/municipios_mt_abstencao.csv` para a aba **Arquivos** (ícone de pasta à esquerda) e rode a célula de novo.

**No computador do laboratório (sem internet)**
1. Copie esta pasta inteira (com a subpasta `dados`).
2. Abra `2026-11-03_Aula02_Abstencao_Alta_INICIAL.ipynb` no Jupyter ou no VS Code. As bibliotecas estão no `requirements.txt` da raiz do repositório.
3. O notebook só lê arquivos: não grava nada.

## O que você vai fazer

| TODO | Tarefa | Apostila |
|---|---|---|
| 1 | Montar `y` (1 = abstenção ≥ 25%) e `X` (4 colunas de perfil) | cap. 2 e 5 |
| 2 | Separar treino e teste: `test_size=0.25`, `stratify=y`, `random_state=42` | cap. 9 |
| 3 | Baseline: `DummyClassifier(strategy='most_frequent')` | cap. 9 |
| 4 | `make_pipeline(StandardScaler(), LogisticRegression())` | cap. 5 e 12 |
| 5 | Probabilidade com `predict_proba` e limiar 0,3 | cap. 12 |

As partes 1, 2 e 7 (carregar, olhar e matriz de confusão) já vêm prontas.

## Dados

`dados/municipios_mt_abstencao.csv`: 142 linhas (uma por município de MT), 10 colunas.
Fonte: TSE, [perfil do eleitorado 2026](https://dadosabertos.tse.jus.br/dataset/eleitorado-2026) e [resultados do 1º turno de 04/10/2026](https://dadosabertos.tse.jus.br/dataset/resultados-2026), agregados por município. São dados públicos, sem nenhum dado pessoal.
É a mesma base do projeto-molde da PPI ([`ppi_molde_comparece_mt`](../../ppi_molde_comparece_mt)), que usa **regressão**. Aqui transformamos o mesmo problema em **classificação**.

## Saída esperada

Quando tudo estiver certo, a tabela de métricas fica assim:

```
Baseline (mais comum)  acurácia 0.69 | precisão 0.00 | recall 0.00
Regressão logística    acurácia 0.75 | precisão 0.62 | recall 0.45
Logística (limiar 0,3) acurácia 0.72 | precisão 0.53 | recall 0.73
```

E a última célula (verificação) mostra:

```
✅ X tem 142 linhas e as 4 colunas de perfil
✅ y tem 44 municípios com abstenção alta
✅ teste tem 36 municípios, 11 deles "alta"
✅ baseline: acurácia 0,69 e recall 0,00
✅ logística (0,5): acurácia 0,75 e recall 0,45
✅ logística (0,3): recall 0,73 e precisão 0,53

6 de 6 verificações OK
```

Se aparecer ❌, o erro está no TODO daquela linha. Os números só batem com `random_state=42` e `stratify=y`.

## Critérios (o que o professor vai olhar)

1. **Experimento honesto:** o split vem antes de qualquer ajuste, e `QT_ABSTENCOES`/`ABSTENCAO_PCT` não estão no X (seriam vazamento: são a própria resposta).
2. **Baseline presente** e comparado com o modelo.
3. **Leitura da matriz de confusão:** saber dizer, com os números, quantos municípios "alta" ficaram sem campanha (FN).
4. **Respostas às 3 perguntas para discussão** com as suas palavras, numa célula de texto embaixo de cada uma.
5. **6 de 6 na verificação.**

## Desafio extra (para quem terminar)

Troque `LogisticRegression()` por `KNeighborsClassifier(n_neighbors=5)` (de `sklearn.neighbors`) e compare as métricas.
Depois, tire o `StandardScaler` do pipeline do k-NN. O que acontece, e por quê? (cap. 6 e 13)
