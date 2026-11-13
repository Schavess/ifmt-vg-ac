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

Os exemplos de código ficam em três notebooks, em [`notebooks/`](notebooks). Cada seção do notebook diz o capítulo a que corresponde.
Procure os `# TODO`: são as lacunas que você completa.

## Notebooks

| Notebook | Capítulos | Lacunas | Dados | Abrir |
|---|---|---|---|---|
| `AC_U1_Dados_ao_Pipeline_INICIAL` | 1 a 7, 17 e 23 | 7 | Pinguins (CSV em [`dados/`](dados); no Colab, baixa da internet) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Schavess/ifmt-vg-ac/blob/main/apostila/notebooks/AC_U1_Dados_ao_Pipeline_INICIAL.ipynb) |
| `AC_U2_Supervisionada_INICIAL` | 5 e 8 a 16 | 3 | Diabetes + câncer de mama (já vêm no scikit-learn) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Schavess/ifmt-vg-ac/blob/main/apostila/notebooks/AC_U2_Supervisionada_INICIAL.ipynb) |
| `AC_U3_Nao_Supervisionada_INICIAL` | 18 a 22 e 24 | 3 | Vinhos (já vem no scikit-learn) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Schavess/ifmt-vg-ac/blob/main/apostila/notebooks/AC_U3_Nao_Supervisionada_INICIAL.ipynb) |

O exemplo completo de projeto (cap. 24) é o [PPI-molde Comparece MT](../ppi_molde_comparece_mt).

## Mapa: capítulo → onde está no código

| Cap. | Assunto | Notebook · seção |
|---|---|---|
| 1–3 | Aprender com dados, vocabulário, CRISP-DM | U1 · abertura |
| 4 | Análise exploratória | U1 · 1 e 2 |
| 5 | Treino, teste e baseline (o experimento honesto) | U1 · 3 e 4; U2 · A1 |
| 6 | Preparação e vazamento | U1 · 3 e 5 |
| 7 | Distâncias e escala | U1 · 6 |
| 8 | Regressão | U2 · Parte A |
| 9 | Regressão logística e métricas | U2 · B2 |
| 10 | Teoria: complexidade × generalização | U2 · A e B3 |
| 11–16 | k-NN, Naive Bayes, árvores, SVM, redes neurais, ensembles | U2 · B4 e B5 |
| 17 | PCA | U1 · 8 |
| 18 | O que é um bom grupo | U3 · 2 |
| 19 | K-Means | U3 · 3 |
| 20 | Misturas gaussianas | U3 · 4 |
| 21 | Fuzzy C-Means | U3 · 5 |
| 22 | SOM | U3 · 6 |
| 23 | Anomalias | U1 · 9 |
| 24 | Da previsão à decisão | U3 · 7; [PPI-molde](../ppi_molde_comparece_mt) |

## Onde os notebooks gravam arquivos

Os notebooks não gravam nada dentro desta pasta. Quando precisam guardar algum arquivo, usam `/content` no Colab ou `ac_saida`, dentro da sua pasta de usuário, no laboratório. O caminho aparece na saída.
