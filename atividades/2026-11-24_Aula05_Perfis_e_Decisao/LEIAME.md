# Prática 24/11 · Da previsão à decisão: perfis de municípios e carteira sob orçamento

AC • 4º TIA • 24/11/2026 • Aula 05 • apostila: cap. 6, 7, 19, 20 e 24 • parte do [PPI-molde Comparece MT](../../ppi_molde_comparece_mt)

**Pergunta:** como transformar a previsão em decisão: onde investir uma ação de mobilização com orçamento limitado?

## Objetivo

Prever todos os municípios sem otimismo (`cross_val_predict`), descrever o território com PCA e K-Means (sem usar y) e escolher a carteira de municípios com o problema da mochila, comparando com regras simples numa checagem retrospectiva. É a entrega do check-in de 24/11: previsões exportadas e decisão v0.

## Como abrir

**No Google Colab (recomendado)**
1. Abra o notebook pelo botão abaixo. Ele lê os dados do GitHub da disciplina, então precisa de internet.

   [![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Schavess/ifmt-vg-ac/blob/main/atividades/2026-11-24_Aula05_Perfis_e_Decisao/2026-11-24_Aula05_Perfis_e_Decisao_INICIAL.ipynb)

2. **Arquivo > Salvar uma cópia no Drive**, para não perder o que fizer.
3. Se a célula de leitura der erro, arraste o arquivo `dados/base_analitica.csv` para a aba **Arquivos** (ícone de pasta à esquerda) e rode a célula de novo.

**No computador do laboratório (sem internet)**
1. Copie esta pasta inteira (com a subpasta `dados`).
2. Abra `2026-11-24_Aula05_Perfis_e_Decisao_INICIAL.ipynb` no Jupyter ou no VS Code. As bibliotecas estão no `requirements.txt` da raiz do repositório.

## O que você vai fazer

| TODO | Tarefa | Apostila |
|---|---|---|
| 1 | Previsões fora da amostra e `previsoes.csv` | cap. 24 |
| 2 | Padronizar e projetar com PCA | cap. 6 e 7 |
| 3 | Cotovelo e silhueta para escolher o k | cap. 19 e 20 |
| 4 | Benefício previsto de cada município | cap. 24 |
| 5 | Mochila × "maior % prevista primeiro" | cap. 24 |

## Dados

`dados/base_analitica.csv`: a base do [PPI-molde](../../ppi_molde_comparece_mt), 141 linhas (uma por município de MT) e 15 colunas: abstenção no 1º turno para presidente em 2026 (y) e em 2022, crescimento do eleitorado, distância até Cuiabá e perfil do eleitorado.
Fontes: [TSE](https://dadosabertos.tse.jus.br) (perfil do eleitorado 2026 e resultados de 2022 e 2026) e coordenadas das sedes (IBGE). Ela é gerada pelo ETL da prática de 03/11. São dados públicos, sem nenhum dado pessoal.

## Saída esperada

A última célula (verificação) deve mostrar:

```
✅ previsões fora da amostra: MAE 1,28
✅ previsoes.csv salvo com 141 linhas
✅ PCA: 2 eixos explicam 0,67 da variação
✅ silhueta escolheu k = 3
✅ benefício previsto em 130 municípios
✅ mochila: 29 municípios dentro do orçamento
✅ "maior % prevista primeiro": 37 municípios

7 de 7 verificações OK
```

Se aparecer ❌, o erro está no TODO daquela linha. Os números só batem com `random_state=42`.

## Critérios (o que o professor vai olhar)

1. **Previsões fora da amostra**, e não do modelo ajustado na base toda.
2. **Perfis sem y**, com a silhueta lida com cuidado.
3. **Hipóteses da decisão declaradas** e a leitura da checagem retrospectiva.
4. **Respostas às 3 perguntas para discussão.**
5. **Todas as verificações OK** na última célula.

## Desafio extra (para quem terminar)

Refaça a mochila com um cenário conservador (previsão − 1,28 p.p.). Quantos municípios saem da carteira?
