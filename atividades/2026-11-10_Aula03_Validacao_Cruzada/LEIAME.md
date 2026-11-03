# Prática: qual modelo acha melhor os municípios de abstenção alta? Validação cruzada

AC • 4º TIA • 10/11/2026 • Aula 03 • apostila: cap. 9, 12, 13, 16 e 18

**Pergunta:** entre baseline, logística, k-NN, árvore e Random Forest, qual escolher para apontar os municípios de MT com abstenção de 25% ou mais, **sem gastar o teste**?

## Objetivo

Comparar modelos de forma justa com **validação cruzada** (mesmos folds, mesmas métricas, só no treino), ajustar um hiperparâmetro com `GridSearchCV` e abrir o teste **uma única vez**, no fim.
Continua a prática de 03/11: mesmo y, mesmo X, mesmo split.

## Como abrir

**No Google Colab (recomendado)**
1. Abra o notebook pelo botão abaixo. Ele lê os dados do GitHub da disciplina, então precisa de internet.

   [![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Schavess/ifmt-vg-ac/blob/main/atividades/2026-11-10_Aula03_Validacao_Cruzada/2026-11-10_Aula03_Validacao_Cruzada_INICIAL.ipynb)

2. **Arquivo > Salvar uma cópia no Drive**, para não perder o que fizer.
3. Se a célula de leitura der erro, arraste o arquivo `dados/municipios_mt_votos.csv` para a aba **Arquivos** (ícone de pasta à esquerda) e rode a célula de novo.

**No computador do laboratório (sem internet)**
1. Copie esta pasta inteira (com a subpasta `dados`).
2. Abra `2026-11-10_Aula03_Validacao_Cruzada_INICIAL.ipynb` no Jupyter ou no VS Code. As bibliotecas estão no `requirements.txt` da raiz do repositório.
3. O notebook só lê arquivos: não grava nada.

## O que você vai fazer

| TODO | Tarefa | Apostila |
|---|---|---|
| 1 | `StratifiedKFold(n_splits=5, shuffle=True, random_state=SEMENTE)` | cap. 9 |
| 2 | Montar k-NN (com escala), árvore (`max_depth=3`) e Random Forest (200 árvores) | cap. 13, 16, 18 |
| 3 | `cross_validate` para cada candidato (acurácia, recall, F1) | cap. 9, 18 |
| 4 | `GridSearchCV` para o k do k-NN | cap. 13 |
| 5 | Ajustar a logística com pesos no treino e prever o teste uma vez | cap. 9, 12 |

## Dados

`dados/municipios_mt_votos.csv`: 142 linhas (uma por município de MT), 14 colunas: perfil do eleitorado, abstenção e votos brancos e nulos do 1º turno para presidente.
Fonte: TSE, [perfil do eleitorado 2026](https://dadosabertos.tse.jus.br/dataset/eleitorado-2026) e [resultados do 1º turno de 04/10/2026](https://dadosabertos.tse.jus.br/dataset/resultados-2026), agregados por município. São dados públicos, sem nenhum dado pessoal.

## Saída esperada

```
semente 0: recall no teste = 0.55   ...   semente 8: recall no teste = 0.09
menor 0.09 | maior 0.55

                    acurácia  recall  recall (desvio)    F1
Logística (pesos)       0.71    0.79             0.06  0.63
k-NN (k=5)              0.77    0.46             0.14  0.56
Random Forest           0.76    0.43             0.13  0.53
Logística               0.75    0.40             0.08  0.49
Árvore (prof. 3)        0.71    0.30             0.21  0.35
Baseline                0.69    0.00             0.00  0.00

melhor k: 5 | F1 médio na CV: 0.56

TESTE · logística com pesos: acurácia 0.69 | precisão 0.50 | recall 0.73 | F1 0.59
8 de 11 municípios "alta" encontrados, 8 alarmes falsos
```

A última célula (verificação) deve mostrar:

```
✅ cv tem 5 folds estratificados
✅ 5 candidatos montados (nenhum None)
✅ k-NN (k=5): F1 médio 0,56 na CV
✅ Random Forest: F1 médio 0,53 na CV
✅ GridSearch escolheu k = 5
✅ teste: recall da logística com pesos = 0,73

6 de 6 verificações OK
```

Se aparecer ❌, o erro está no TODO daquela linha. Os números só batem com `random_state=42`.

## Critérios (o que o professor vai olhar)

1. **Protocolo justo:** todos os modelos avaliados com o mesmo `cv`, só no treino.
2. **Escolha pela CV**, não pelo teste. O teste aparece uma vez, no fim.
3. **Média e desvio** relatados juntos, e a leitura do desvio da árvore na pergunta da parte 6.
4. **Respostas às 2 perguntas para discussão** com as suas palavras.
5. **6 de 6 na verificação.**

## Desafio extra (para quem terminar)

Faça um `GridSearchCV` para o Random Forest com `{'max_depth': [2, 3, 5, None], 'min_samples_leaf': [1, 3, 5]}` e `scoring='f1'`. Ele passa a logística com pesos na validação cruzada?
