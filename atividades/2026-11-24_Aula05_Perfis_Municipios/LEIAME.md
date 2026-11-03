# Prática: perfis de municípios de MT com K-Means

AC • 4º TIA • 24/11/2026 • Aula 05 • apostila: cap. 6, 7, 19, 20 e 24

**Pergunta:** os 142 municípios de MT se dividem em poucos **tipos** de eleitorado, que pediriam ações diferentes?

## Objetivo

Fazer um agrupamento completo **sem y**: padronizar, enxergar com PCA, escolher o k com cotovelo e silhueta, descrever cada grupo e checar se os grupos dizem algo sobre colunas que **não** entraram no agrupamento (abstenção e brancos e nulos).

## Como abrir

**No Google Colab (recomendado)**
1. Abra o notebook pelo botão abaixo. Ele lê os dados do GitHub da disciplina, então precisa de internet.

   [![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Schavess/ifmt-vg-ac/blob/main/atividades/2026-11-24_Aula05_Perfis_Municipios/2026-11-24_Aula05_Perfis_Municipios_INICIAL.ipynb)

2. **Arquivo > Salvar uma cópia no Drive**, para não perder o que fizer.
3. Se a célula de leitura der erro, arraste o arquivo `dados/municipios_mt_votos.csv` para a aba **Arquivos** (ícone de pasta à esquerda) e rode a célula de novo.

**No computador do laboratório (sem internet)**
1. Copie esta pasta inteira (com a subpasta `dados`).
2. Abra `2026-11-24_Aula05_Perfis_Municipios_INICIAL.ipynb` no Jupyter ou no VS Code. As bibliotecas estão no `requirements.txt` da raiz do repositório.
3. O notebook só lê arquivos: não grava nada.

## O que você vai fazer

| TODO | Tarefa | Apostila |
|---|---|---|
| 1 | X = 4 colunas de perfil e `StandardScaler().fit_transform` | cap. 6, 19 |
| 2 | `PCA(n_components=2)` e o gráfico 2D | cap. 7 |
| 3 | K-Means de k = 2 a 8: inércia e silhueta | cap. 19, 20 |
| 4 | K-Means final com k = 3 e a coluna `GRUPO` | cap. 20, 24 |
| 5 | Média de abstenção e de brancos e nulos por grupo | cap. 19 |

## Dados

`dados/municipios_mt_votos.csv`: 142 linhas (uma por município de MT), 14 colunas: perfil do eleitorado, abstenção e votos brancos e nulos do 1º turno para presidente.
Fonte: TSE, [perfil do eleitorado 2026](https://dadosabertos.tse.jus.br/dataset/eleitorado-2026) e [resultados do 1º turno de 04/10/2026](https://dadosabertos.tse.jus.br/dataset/resultados-2026), agregados por município. São dados públicos, sem nenhum dado pessoal.

## Saída esperada

```
variância explicada por componente: [0.451 0.379]
as 2 juntas guardam 83% da variação

   inércia  silhueta
k
2   397.34      0.27
3   278.60      0.30
4   239.72      0.23
...
8   155.80      0.23

grupo 0: Poconé, Peixoto De Azevedo, Colniza, Aripuanã               (61 municípios)
grupo 1: Jaciara, Chapada Dos Guimarães, Santo Antônio Do Leverger, Nova Xavantina   (50)
grupo 2: Cuiabá, Várzea Grande, Rondonópolis, Sinop                  (31)

       ABSTENCAO_PCT  PCT_BRANCOS_NULOS
GRUPO
0              24.50               2.71
1              22.59               3.07
2              22.84               2.72
```

A última célula (verificação) deve mostrar:

```
✅ Z padronizado: 142 × 4, médias 0 e desvios 1
✅ PCA: as 2 componentes guardam 83% da variação
✅ silhueta máxima em k = 3 (0,30)
✅ grupos com 31, 50 e 61 municípios
✅ tabela por grupo tem abstenção e brancos/nulos

5 de 5 verificações OK
```

Se aparecer ❌, o erro está no TODO daquela linha. Os números só batem com `random_state=42`.

## Critérios (o que o professor vai olhar)

1. **Padronização antes do K-Means**, e saber explicar por quê.
2. **Escolha do k justificada** com a silhueta e o cotovelo.
3. **Um nome para cada grupo**, apoiado no perfil médio.
4. **Leitura do "rótulo guardado"**: o que muda na decisão para cada grupo.
5. **5 de 5 na verificação.**

## Desafio extra (para quem terminar)

Troque o K-Means por `AgglomerativeClustering(n_clusters=3)` (de `sklearn.cluster`) e compare com `pd.crosstab(municipios['GRUPO'], novos_rotulos)`. Os dois métodos concordam?
