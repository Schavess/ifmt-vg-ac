# Prática 17/11 · Qual modelo escolher? Validação cruzada, árvores e sobreajuste

AC • 4º TIA • 17/11/2026 • Aula 04 • apostila: cap. 9, 10, 13, 16 e 18 • parte do [PPI-molde Comparece MT](../../ppi_molde_comparece_mt)

**Pergunta:** entre as duas réguas, a linear, a Ridge, a árvore, o k-NN e a Random Forest, qual escolher para prever a abstenção, **sem gastar o teste**?

## Objetivo

Comparar modelos de forma justa com **validação cruzada** (mesmas dobras, mesma métrica, só no treino), ver o sobreajuste na curva da árvore, ajustar um hiperparâmetro com `GridSearchCV` e abrir o teste **uma única vez**, no fim. É a entrega do check-in de 24/11.

## Como abrir

**No Google Colab (recomendado)**
1. Abra o notebook pelo botão abaixo. Ele lê os dados do GitHub da disciplina, então precisa de internet.

   [![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Schavess/ifmt-vg-ac/blob/main/atividades/2026-11-17_Aula04_Validacao_Cruzada_Arvores/2026-11-17_Aula04_Validacao_Cruzada_Arvores_INICIAL.ipynb)

2. **Arquivo > Salvar uma cópia no Drive**, para não perder o que fizer.
3. Se a célula de leitura der erro, arraste o arquivo `dados/base_analitica.csv` para a aba **Arquivos** (ícone de pasta à esquerda) e rode a célula de novo.

**No computador do laboratório (sem internet)**
1. Copie esta pasta inteira (com a subpasta `dados`).
2. Abra `2026-11-17_Aula04_Validacao_Cruzada_Arvores_INICIAL.ipynb` no Jupyter ou no VS Code. As bibliotecas estão no `requirements.txt` da raiz do repositório.

## O que você vai fazer

| TODO | Tarefa | Apostila |
|---|---|---|
| 1 | `KFold` com 5 dobras | cap. 9 |
| 2 | Curva de complexidade da árvore | cap. 10 e 16 |
| 3 | Montar k-NN (com escala) e Random Forest | cap. 13 e 18 |
| 4 | `GridSearchCV` para o k do k-NN | cap. 13 |
| 5 | Ajustar o escolhido no treino e prever o teste uma vez | cap. 9 |

## Dados

`dados/base_analitica.csv`: a base do [PPI-molde](../../ppi_molde_comparece_mt), 141 linhas (uma por município de MT) e 15 colunas: abstenção no 1º turno para presidente em 2026 (y) e em 2022, crescimento do eleitorado, distância até Cuiabá e perfil do eleitorado.
Fontes: [TSE](https://dadosabertos.tse.jus.br) (perfil do eleitorado 2026 e resultados de 2022 e 2026) e coordenadas das sedes (IBGE). Ela é gerada pelo ETL da prática de 03/11. São dados públicos, sem nenhum dado pessoal.

## Saída esperada

A última célula (verificação) deve mostrar:

```
✅ cv tem 5 dobras embaralhadas
✅ curva da árvore: sem limite, erro zero no ajuste
✅ curva da árvore: melhor profundidade = 4
✅ 7 candidatos montados (nenhum None)
✅ regressão linear: MAE 1,33 na CV
✅ Random Forest: MAE 1,62 na CV
✅ GridSearch escolheu k = 5
✅ teste: MAE da linear = 1,23

8 de 8 verificações OK
```

Se aparecer ❌, o erro está no TODO daquela linha. Os números só batem com `random_state=42`.

## Critérios (o que o professor vai olhar)

1. **Protocolo justo:** todos os modelos com o mesmo `cv`, só no treino.
2. **Leitura da curva da árvore** (subajuste e sobreajuste).
3. **Escolha pela CV**, com média e desvio. O teste aparece uma vez, no fim.
4. **Respostas às 3 perguntas para discussão.**
5. **Todas as verificações OK** na última célula.

## Desafio extra (para quem terminar)

Faça um `GridSearchCV` para a Random Forest com `{'max_depth': [2, 3, 5, None], 'min_samples_leaf': [1, 3, 5]}`. Ela passa a linear?
