# Prática 27/10 · O problema: onde o eleitor de Mato Grosso deixa de votar?

AC • 4º TIA • 27/10/2026 • Aula 01 • apostila: cap. 1 a 4 • parte do [PPI-molde Comparece MT](../../ppi_molde_comparece_mt)

**Pergunta:** onde o eleitor de Mato Grosso deixa de votar, e como transformar isso numa pergunta que um modelo possa responder **antes** da eleição?

## Objetivo

Entender o problema do PPI-molde antes de qualquer modelo: de onde vem o y, qual é a unidade de análise, o que o mapa e a eleição anterior sugerem. No fim, preencher a **ficha do problema**, que é a entrega do check-in zero (03/11).

## Como abrir

**No Google Colab (recomendado)**
1. Abra o notebook pelo botão abaixo. Ele lê os dados do GitHub da disciplina, então precisa de internet.

   [![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Schavess/ifmt-vg-ac/blob/main/atividades/2026-10-27_Aula01_O_Problema/2026-10-27_Aula01_O_Problema_INICIAL.ipynb)

2. **Arquivo > Salvar uma cópia no Drive**, para não perder o que fizer.
3. Se a célula de leitura der erro, arraste o arquivo `dados/base_analitica.csv` para a aba **Arquivos** (ícone de pasta à esquerda) e rode a célula de novo.

**No computador do laboratório (sem internet)**
1. Copie esta pasta inteira (com a subpasta `dados`).
2. Abra `2026-10-27_Aula01_O_Problema_INICIAL.ipynb` no Jupyter ou no VS Code. As bibliotecas estão no `requirements.txt` da raiz do repositório.

## O que você vai fazer

| TODO | Tarefa | Apostila |
|---|---|---|
| 1 | Recalcular y a partir das contagens | cap. 2 e 3 |
| 2 | Média simples × média ponderada (abstenção do estado) | cap. 4 |
| 3 | Os 10 municípios com maior abstenção | cap. 4 |
| 4 | Mapa da abstenção | cap. 4 |
| 5 | Correlação entre 2022 e 2026 | cap. 4 |
| 6 | Ficha do problema: decisor, decisão, pergunta, unidade, y e X | cap. 1 a 3 |

## Dados

`dados/base_analitica.csv`: a base do [PPI-molde](../../ppi_molde_comparece_mt), 141 linhas (uma por município de MT) e 15 colunas: abstenção no 1º turno para presidente em 2026 (y) e em 2022, crescimento do eleitorado, distância até Cuiabá e perfil do eleitorado.
Fontes: [TSE](https://dadosabertos.tse.jus.br) (perfil do eleitorado 2026 e resultados de 2022 e 2026) e coordenadas das sedes (IBGE). Ela é gerada pelo ETL da prática de 03/11. São dados públicos, sem nenhum dado pessoal.

## Saída esperada

A última célula (verificação) deve mostrar:

```
✅ y recalculado bate com a coluna
✅ média simples 23,45% e do estado 22,20%
✅ maior abstenção: Nova Nazaré
✅ correlação 2022 × 2026 = 0,77
✅ ficha: y é a coluna ABSTENCAO_PCT
✅ ficha: X só com colunas da base, sem contagens de 2026 nem y
✅ ficha: decisor, decisão, pergunta e unidade preenchidos

7 de 7 verificações OK
```

Se aparecer ❌, o erro está no TODO daquela linha. Os números só batem com `random_state=42`.

## Critérios (o que o professor vai olhar)

1. **Ficha completa**, com X só de variáveis conhecidas antes da eleição.
2. **Leitura correta** das duas médias (simples e do estado).
3. **Respostas às 2 perguntas para discussão** com as suas palavras.
4. **Todas as verificações OK** na última célula.

## Desafio extra (para quem terminar)

Faça um histograma da **variação** da abstenção (2026 − 2022) por município. Em que região do mapa ela caiu menos?
