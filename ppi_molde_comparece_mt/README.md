# PPI-molde · Comparece MT

**Previsão de abstenção eleitoral e priorização de mobilização sob orçamento em Mato Grosso.**
Projeto de exemplo da PPI GovTech (AC · 4º TIA · 2026/2). Ele também serve de **modelo de repositório**: organizem o do grupo assim.

## O que a solução faz
1. **Prevê** a abstenção de cada um dos 142 municípios de MT a partir do perfil do eleitorado (TSE), com regressão linear, baseline e validação cruzada.
2. **Agrupa** os municípios em 3 perfis (K-Means), para descrever o território.
3. **Decide** onde investir uma ação de mobilização com orçamento limitado (problema da mochila 0/1).
4. **Mostra** tudo num dashboard web com controle de orçamento.

O modelo erra **2,14 p.p.** no teste, contra 2,29 p.p. do baseline. É um ganho modesto, e a checagem retrospectiva mostra que a otimização é sensível a esse erro. Isso também faz parte do resultado.

## Estrutura
```
ppi_molde_comparece_mt/
├── README.md                       ← este arquivo
├── dados/base_analitica.csv        ← saída do ETL: 1 linha por município
└── notebooks/
    ├── PPI_Molde_Comparece_MT_INICIAL.ipynb   ← o fluxo completo, com 5 lacunas TODO
    └── PPI_TEMPLATE_GRUPO.ipynb               ← esqueleto para o projeto do grupo
```

## Como rodar

| Onde | Como |
|---|---|
| **Colab** | [![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Schavess/ifmt-vg-ac/blob/main/ppi_molde_comparece_mt/notebooks/PPI_Molde_Comparece_MT_INICIAL.ipynb). Depois, *Ambiente de execução → Executar tudo*. A base é lida do GitHub da disciplina. |
| **Laboratório** | `python -m pip install --user pandas scikit-learn matplotlib` e abra o notebook no Jupyter ou no VS Code. Ele lê `dados/base_analitica.csv` sem precisar de internet. |

**Arquivos gerados** (`previsoes.csv`, `ranking_decisao.csv` e `dashboard_comparece_mt.html`) vão para `/content/comparece_mt` no Colab, de onde são baixados automaticamente, ou para `ac_saida/comparece_mt`, dentro da sua pasta de usuário, no laboratório. O caminho aparece na primeira célula. Nada é gravado dentro do repositório.

**Dashboard:** dê dois cliques no `dashboard_comparece_mt.html` gerado. Para publicar o do grupo, use o GitHub Pages.

## Fontes
- TSE, Perfil do eleitorado 2026 (geração 14/07/2026): https://dadosabertos.tse.jus.br/dataset/eleitorado-2026
- TSE, Resultados 2026, 1º turno de 04/10/2026: https://dadosabertos.tse.jus.br/dataset/resultados-2026

No projeto de vocês, o **ETL tem que estar em código no repositório**, para qualquer um reconstruir a base a partir das fontes oficiais.

## Hipóteses declaradas
Meta de 20% de abstenção; a ação recupera 30% do excesso previsto; custo de R$ 10 mil + R$ 1,50 por eleitor apto. **São valores didáticos, não oficiais.**
