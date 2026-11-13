# Apostila do Aluno · Aprendizagem Computacional

📘 [`Apostila_Aprendizagem_Computacional_Aluno_v2.pdf`](Apostila_Aprendizagem_Computacional_Aluno_v2.pdf) (para ler) · [`.docx`](Apostila_Aprendizagem_Computacional_Aluno_v2.docx) (editável)

São 4 unidades e 24 capítulos, organizados como uma **corrente de perguntas**: cada capítulo responde a uma pergunta que o anterior deixou aberta. Todo capítulo segue o mesmo roteiro:
**De onde viemos → A ideia → Como funciona → No código → Armadilhas → No seu projeto → A pergunta que fica → Verifique**.

| Unidade | Pergunta | Capítulos |
|---|---|---|
| 1 | Tenho dados: o que eles dizem? | 1 a 4 |
| 2 | Meu primeiro modelo, provado com honestidade | 5 a 10 |
| 3 | Outras famílias de modelos | 11 a 16 |
| 4 | Sem y, e até a decisão | 17 a 24 |

Os exemplos de código ficam em **um notebook por unidade**, em [`notebooks/`](notebooks). Cada seção do notebook diz o capítulo a que corresponde.
Procure os `# TODO`: são as lacunas que você completa.

## Notebooks

| Notebook | Capítulos | Lacunas | Dados | Abrir |
|---|---|---|---|---|
| `AC_U1_Dados_INICIAL` | 1 a 4 | 3 | Pinguins (CSV em [`dados/`](dados); no Colab, baixa da internet) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Schavess/ifmt-vg-ac/blob/main/apostila/notebooks/AC_U1_Dados_INICIAL.ipynb) |
| `AC_U2_Primeiro_Modelo_Honesto_INICIAL` | 5 a 10 | 5 | Pinguins, diabetes e câncer de mama | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Schavess/ifmt-vg-ac/blob/main/apostila/notebooks/AC_U2_Primeiro_Modelo_Honesto_INICIAL.ipynb) |
| `AC_U3_Familias_de_Modelos_INICIAL` | 11 a 16 | 3 | Câncer de mama (já vem no scikit-learn) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Schavess/ifmt-vg-ac/blob/main/apostila/notebooks/AC_U3_Familias_de_Modelos_INICIAL.ipynb) |
| `AC_U4_Sem_Rotulo_e_Decisao_INICIAL` | 17 a 24 | 5 | Vinhos (já vem no scikit-learn) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Schavess/ifmt-vg-ac/blob/main/apostila/notebooks/AC_U4_Sem_Rotulo_e_Decisao_INICIAL.ipynb) |

O exemplo completo de projeto (cap. 24) é o [PPI-molde Comparece MT](../ppi_molde_comparece_mt).

## Mapa: capítulo → onde está no código

| Cap. | Assunto | Notebook · seção |
|---|---|---|
| 1–3 | Aprender com dados, vocabulário, CRISP-DM | U1 · 1 e 4 (ficha do problema) |
| 4 | Análise exploratória | U1 · 1 a 3 |
| 5 | Treino, teste e baseline (o experimento honesto) | U2 · Parte A |
| 6 | Preparação e vazamento | U2 · B1 |
| 7 | Distâncias e escala | U2 · B2 |
| 8 | Regressão | U2 · Parte C |
| 9 | Regressão logística, métricas e limiar | U2 · Parte D |
| 10 | Teoria: complexidade × generalização | U2 · Parte E |
| 11 | k-NN | U3 · 1 |
| 12 | Naive Bayes | U3 · 2 |
| 13 | Árvores de decisão | U3 · 3 |
| 14 | SVM | U3 · 4 |
| 15 | Redes neurais (MLP) | U3 · 5 |
| 16 | Ensembles e a comparação justa | U3 · 6 e 7 |
| 17 | PCA | U4 · 2 |
| 18 | O que é um bom grupo | U4 · 3 |
| 19 | K-Means | U4 · 4 |
| 20 | Misturas gaussianas | U4 · 5 |
| 21 | Fuzzy C-Means | U4 · 6 |
| 22 | SOM | U4 · 7 |
| 23 | Anomalias | U4 · 8 |
| 24 | Da previsão à decisão | U4 · 9; [PPI-molde](../ppi_molde_comparece_mt) |

## Onde os notebooks gravam arquivos

Os notebooks não gravam nada dentro desta pasta. Quando precisam guardar algum arquivo, usam `/content` no Colab ou `ac_saida`, dentro da sua pasta de usuário, no laboratório. O caminho aparece na saída.
