# PPI-molde · Comparece MT

**Previsão de abstenção eleitoral e priorização de mobilização sob orçamento em Mato Grosso.**
Projeto de exemplo da PPI GovTech (AC · 4º TIA · 2026/2). Ele também serve de **modelo de repositório**: organizem o do grupo assim.

## O que a solução faz
1. **Monta a base** a partir das fontes oficiais (TSE e IBGE), com um ETL em código.
2. **Prevê** a abstenção de cada um dos 141 municípios de MT com o que se sabe **antes** da eleição: abstenção de 2022, crescimento do eleitorado, distância até Cuiabá e perfil do eleitorado. Regressão linear, dois baselines e validação cruzada.
3. **Agrupa** os municípios em 3 perfis (K-Means), para descrever o território.
4. **Decide** onde investir uma ação de mobilização com orçamento limitado (problema da mochila 0/1).
5. **Mostra** tudo num dashboard web com controle de orçamento.

No teste, o modelo erra **1,23 p.p.**, contra 1,96 p.p. de repetir 2022 (corrigido) e 2,13 p.p. de prever a média, com R² de 0,77. Na checagem retrospectiva, a carteira ótima traz mais eleitores que as regras simples em quase todos os orçamentos.

> **v2 (09/11/2026).** A v1 usava só as 4 variáveis de perfil, tinha R² de 0,09 no teste, e a otimização perdia para as regras simples porque amplificava o erro da previsão. A v2 acrescentou a abstenção de 2022, o crescimento do eleitorado e a distância. A lição: o problema estava nos dados, não no algoritmo.

## Uma prática por semana
Cada pedaço do molde é construído numa prática de laboratório, na mesma ordem das entregas da PPI:

| Prática | O que constrói | Entrega da PPI |
|---|---|---|
| [27/10 · O problema](../atividades/2026-10-27_Aula01_O_Problema) | pergunta, unidade, y, X e a ficha do problema | 03/11 · escopo fechado |
| [03/11 · O ETL](../atividades/2026-11-03_Aula02_ETL_Base_Analitica) | `base_analitica.csv` a partir do TSE, dicionário e EDA | 10/11 · base v0 |
| [10/11 · Experimento honesto](../atividades/2026-11-10_Aula03_Experimento_Honesto) | split, dois baselines e regressão linear em `Pipeline` | 17/11 · experimento honesto |
| [17/11 · Validação cruzada e árvores](../atividades/2026-11-17_Aula04_Validacao_Cruzada_Arvores) | comparação justa, sobreajuste, `GridSearchCV`, teste uma vez | 24/11 · modelo escolhido |
| [24/11 · Perfis e decisão](../atividades/2026-11-24_Aula05_Perfis_e_Decisao) | previsões fora da amostra, K-Means e mochila | 24/11 e 01/12 · decisão e MVP |
| [01/12 · Tribunal do Pipeline](../atividades/2026-12-01_Aula06_Tribunal_do_Pipeline) | auditoria de vazamento e ensaio da banca | banca |

## Estrutura
```
ppi_molde_comparece_mt/
├── README.md                       ← este arquivo
├── etl/etl_comparece_mt.py         ← ETL: fontes oficiais → base analítica
├── dados/base_analitica.csv        ← saída do ETL: 1 linha por município
└── notebooks/
    ├── PPI_Molde_Comparece_MT_INICIAL.ipynb   ← o fluxo completo, com 6 lacunas TODO
    └── PPI_TEMPLATE_GRUPO.ipynb               ← esqueleto para o projeto do grupo
```

## Como rodar

| Onde | Como |
|---|---|
| **Colab** | [![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Schavess/ifmt-vg-ac/blob/main/ppi_molde_comparece_mt/notebooks/PPI_Molde_Comparece_MT_INICIAL.ipynb). Depois, *Ambiente de execução → Executar tudo*. A base é lida do GitHub da disciplina. |
| **Laboratório** | `python -m pip install --user pandas scikit-learn matplotlib` e abra o notebook no Jupyter ou no VS Code. Ele lê `dados/base_analitica.csv` sem precisar de internet. |

**Refazer a base a partir das fontes:** `python etl/etl_comparece_mt.py`, na pasta do projeto, ou `REFAZER_BASE = True` na primeira célula do notebook. Os ZIP do TSE são grandes (o do perfil tem cerca de 400 MB), mas o ETL lê só o trecho de MT de cada um, direto do servidor: são poucos MB.

**Arquivos gerados** (`previsoes.csv`, `ranking_decisao.csv` e `dashboard_comparece_mt.html`) vão para `/content/comparece_mt` no Colab, de onde são baixados automaticamente, ou para `ac_saida/comparece_mt`, dentro da sua pasta de usuário, no laboratório. O caminho aparece na primeira célula. Nada é gravado dentro do repositório.

**Dashboard:** dê dois cliques no `dashboard_comparece_mt.html` gerado. Para publicar o do grupo, use o GitHub Pages.

## Fontes
- TSE, Perfil do eleitorado 2026 (geração 14/07/2026): https://dadosabertos.tse.jus.br/dataset/eleitorado-2026
- TSE, Resultados 2026, 1º turno de 04/10/2026, e Resultados 2022, 1º turno de 02/10/2022: https://dadosabertos.tse.jus.br
- Coordenadas das sedes municipais (IBGE), pelo repositório https://github.com/kelvins/municipios-brasileiros

Boa Esperança do Norte não aparece nos resultados de 2022 (foi instalado depois) e fica fora da base, por não ter abstenção anterior.

No projeto de vocês, o **ETL tem que estar em código no repositório**, para qualquer um reconstruir a base a partir das fontes oficiais.

## Hipóteses declaradas
Meta de 20% de abstenção; a ação recupera 30% do excesso previsto; custo de R$ 10 mil + R$ 1,50 por eleitor apto. **São valores didáticos, não oficiais.**
