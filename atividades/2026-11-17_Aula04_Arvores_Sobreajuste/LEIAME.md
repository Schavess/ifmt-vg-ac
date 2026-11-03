# Prática: árvores de decisão e sobreajuste: votos brancos e nulos em MT

AC • 4º TIA • 17/11/2026 • Aula 04 • apostila: cap. 9, 10, 11, 16 e 18

**Pergunta:** o perfil do eleitorado ajuda a prever o **percentual de votos brancos e nulos** de cada município de MT? E o que acontece quando a árvore fica funda demais?

## Objetivo

Ver, com números, a diferença entre **erro no treino** e **erro na validação**: a árvore sem limite decora o treino (erro zero) e erra mais em dados novos. Escolher a complexidade pela validação cruzada, ler uma árvore pequena e interpretar a importância das variáveis com cuidado.

## Como abrir

**No Google Colab (recomendado)**
1. Abra o notebook pelo botão abaixo. Ele lê os dados do GitHub da disciplina, então precisa de internet.

   [![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Schavess/ifmt-vg-ac/blob/main/atividades/2026-11-17_Aula04_Arvores_Sobreajuste/2026-11-17_Aula04_Arvores_Sobreajuste_INICIAL.ipynb)

2. **Arquivo > Salvar uma cópia no Drive**, para não perder o que fizer.
3. Se a célula de leitura der erro, arraste o arquivo `dados/municipios_mt_votos.csv` para a aba **Arquivos** (ícone de pasta à esquerda) e rode a célula de novo.

**No computador do laboratório (sem internet)**
1. Copie esta pasta inteira (com a subpasta `dados`).
2. Abra `2026-11-17_Aula04_Arvores_Sobreajuste_INICIAL.ipynb` no Jupyter ou no VS Code. As bibliotecas estão no `requirements.txt` da raiz do repositório.
3. O notebook só lê arquivos: não grava nada.

## O que você vai fazer

| TODO | Tarefa | Apostila |
|---|---|---|
| 1 | y = `PCT_BRANCOS_NULOS`, X = 4 colunas de perfil, `train_test_split` sem `stratify` | cap. 9, 11 |
| 2 | Baseline (`DummyRegressor`) e regressão linear com `mae_cv` | cap. 9, 11 |
| 3 | Árvore com profundidade de 1 a "sem limite": curva treino × validação | cap. 10, 16 |
| 4 | `RandomForestRegressor(300 árvores, min_samples_leaf=3)` e importâncias | cap. 18 |
| 5 | Escolher a árvore de profundidade 1 e prever o teste uma vez | cap. 9 |

## Dados

`dados/municipios_mt_votos.csv`: 142 linhas (uma por município de MT), 14 colunas: perfil do eleitorado, abstenção e votos brancos e nulos do 1º turno para presidente.
Fonte: TSE, [perfil do eleitorado 2026](https://dadosabertos.tse.jus.br/dataset/eleitorado-2026) e [resultados do 1º turno de 04/10/2026](https://dadosabertos.tse.jus.br/dataset/resultados-2026), agregados por município. São dados públicos, sem nenhum dado pessoal.

## Saída esperada

```
profundidade  MAE treino  MAE validação
           1       0.350          0.371
           2       0.322          0.423
           3       0.285          0.420
           4       0.236          0.463
           5       0.183          0.467
           6       0.127          0.467
           8       0.035          0.489
          10       0.005          0.481
        None       0.000          0.511

                     MAE treino  MAE validação
Árvore (prof. 1)          0.350          0.371
Regressão linear          0.360          0.379
Random Forest             0.225          0.391
Baseline (média)          0.418          0.417
Árvore (sem limite)       0.000          0.511

TESTE · árvore (prof. 1): MAE 0.426 | baseline: MAE 0.452
```

A última célula (verificação) deve mostrar:

```
✅ treino com 106 e teste com 36 municípios
✅ baseline: MAE na validação 0,417
✅ linear: MAE na validação 0,379
✅ árvore sem limite: MAE no treino 0,000 e na validação 0,511
✅ Random Forest: MAE na validação 0,391
✅ teste: a árvore de prof. 1 erra menos que o baseline

6 de 6 verificações OK
```

Se aparecer ❌, o erro está no TODO daquela linha. Os números só batem com `random_state=42`.

## Critérios (o que o professor vai olhar)

1. **Sem vazamento:** as contagens de brancos e nulos fora do X.
2. **Leitura da curva:** saber apontar onde começa o sobreajuste e por quê.
3. **Leitura da árvore de profundidade 2:** escrever uma das regras em português ("se… então…").
4. **Importância interpretada com cuidado** (não é causa).
5. **6 de 6 na verificação.**

## Desafio extra (para quem terminar)

Use `GridSearchCV` na árvore com `{'max_depth': [1, 2, 3, 4], 'min_samples_leaf': [1, 5, 10, 20]}` e `scoring='neg_mean_absolute_error'`. Folhas maiores ajudam a árvore mais funda?
