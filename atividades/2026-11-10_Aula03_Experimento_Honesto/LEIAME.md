# Prática 10/11 · Experimento honesto: o modelo vence as duas réguas?

AC • 4º TIA • 10/11/2026 • Aula 03 • apostila: cap. 5, 9 e 11 • parte do [PPI-molde Comparece MT](../../ppi_molde_comparece_mt)

**Pergunta:** a regressão linear erra menos que as duas réguas, prever a média e repetir 2022? E as 3 variáveis novas da base fazem diferença?

## Objetivo

Fazer o primeiro experimento honesto do PPI-molde: teste separado antes de tudo e guardado, validação tirada do treino, dois baselines e uma regressão linear dentro de `Pipeline`, numa tabela com a métrica justificada. É a entrega da sprint review de 17/11.

## Como abrir

**No Google Colab (recomendado)**
1. Abra o notebook pelo botão abaixo. Ele lê os dados do GitHub da disciplina, então precisa de internet.

   [![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Schavess/ifmt-vg-ac/blob/main/atividades/2026-11-10_Aula03_Experimento_Honesto/2026-11-10_Aula03_Experimento_Honesto_INICIAL.ipynb)

2. **Arquivo > Salvar uma cópia no Drive**, para não perder o que fizer.
3. Se a célula de leitura der erro, arraste o arquivo `dados/base_analitica.csv` para a aba **Arquivos** (ícone de pasta à esquerda) e rode a célula de novo.

**No computador do laboratório (sem internet)**
1. Copie esta pasta inteira (com a subpasta `dados`).
2. Abra `2026-11-10_Aula03_Experimento_Honesto_INICIAL.ipynb` no Jupyter ou no VS Code. As bibliotecas estão no `requirements.txt` da raiz do repositório.

## O que você vai fazer

| TODO | Tarefa | Apostila |
|---|---|---|
| 1 | Separar o teste (20%) antes de tudo | cap. 9 |
| 2 | Separar ajuste e validação dentro do treino | cap. 9 |
| 3 | Baseline da média (`DummyRegressor`) | cap. 9 e 11 |
| 4 | Completar o `fit` do baseline de persistência | cap. 9 |
| 5 | Regressão linear dentro de `Pipeline` | cap. 5 e 11 |

## Dados

`dados/base_analitica.csv`: a base do [PPI-molde](../../ppi_molde_comparece_mt), 141 linhas (uma por município de MT) e 15 colunas: abstenção no 1º turno para presidente em 2026 (y) e em 2022, crescimento do eleitorado, distância até Cuiabá e perfil do eleitorado.
Fontes: [TSE](https://dadosabertos.tse.jus.br) (perfil do eleitorado 2026 e resultados de 2022 e 2026) e coordenadas das sedes (IBGE). Ela é gerada pelo ETL da prática de 03/11. São dados públicos, sem nenhum dado pessoal.

## Saída esperada

A última célula (verificação) deve mostrar:

```
✅ teste separado: 112 no treino e 29 no teste
✅ validação tirada do treino: 84 no ajuste e 28 na validação
✅ baseline da média: MAE 2,42 na validação
✅ persistência: deslocamento -2,31 p.p.
✅ persistência: MAE 2,13 na validação
✅ linear dentro de Pipeline com escala
✅ linear (7 variáveis): MAE 1,52 na validação

7 de 7 verificações OK
```

Se aparecer ❌, o erro está no TODO daquela linha. Os números só batem com `random_state=42`.

## Critérios (o que o professor vai olhar)

1. **O teste não aparece** em nenhuma conta da prática.
2. **Escala dentro do `Pipeline`.**
3. **Tabela baseline × modelo** com a leitura da comparação 4 × 7 variáveis.
4. **Respostas às 2 perguntas para discussão.**
5. **Todas as verificações OK** na última célula.

## Desafio extra (para quem terminar)

Troque o MAE pelo RMSE na tabela. A ordem dos modelos muda? Qual município pesa mais no RMSE da linear?
