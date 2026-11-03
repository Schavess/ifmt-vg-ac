# Apostila do Aluno · Aprendizagem Computacional

📘 [`Apostila_Aprendizagem_Computacional_Aluno.pdf`](Apostila_Aprendizagem_Computacional_Aluno.pdf) (para ler) · [`.docx`](Apostila_Aprendizagem_Computacional_Aluno.docx) (editável)

São 3 unidades e 24 capítulos. Todo capítulo segue o mesmo roteiro:
**De onde viemos → A ideia → Como funciona → No código → Armadilhas → No seu projeto → Verifique**.

Os exemplos de código ficam em **um notebook por unidade**, em [`notebooks/`](notebooks). Cada seção do notebook diz o capítulo a que corresponde.
Procure os `# TODO`: são as lacunas que você completa.

## Notebooks

| Notebook | Capítulos | Lacunas | Dados | Abrir |
|---|---|---|---|---|
| `AC_U1_Dados_ao_Pipeline_INICIAL` | 1 a 8 | 7 | Pinguins (CSV em [`dados/`](dados); no Colab, baixa da internet) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Schavess/ifmt-vg-ac/blob/main/apostila/notebooks/AC_U1_Dados_ao_Pipeline_INICIAL.ipynb) |
| `AC_U2_Supervisionada_INICIAL` | 9 a 18 | 3 | Diabetes + câncer de mama (já vêm no scikit-learn) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Schavess/ifmt-vg-ac/blob/main/apostila/notebooks/AC_U2_Supervisionada_INICIAL.ipynb) |
| `AC_U3_Nao_Supervisionada_INICIAL` | 19 a 24 | 3 | Vinhos (já vem no scikit-learn) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Schavess/ifmt-vg-ac/blob/main/apostila/notebooks/AC_U3_Nao_Supervisionada_INICIAL.ipynb) |
| `AC_Extra_Redes_Neurais_INICIAL` | 15 | 3 | XOR + dígitos manuscritos (offline) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Schavess/ifmt-vg-ac/blob/main/apostila/notebooks/AC_Extra_Redes_Neurais_INICIAL.ipynb) |
| `AC_Extra_Visao_Computacional_INICIAL` | 15 | 4 | Imagens do scikit-image + dígitos; fotos de placas baixadas da internet (22 MB) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Schavess/ifmt-vg-ac/blob/main/apostila/notebooks/AC_Extra_Visao_Computacional_INICIAL.ipynb) |

O exemplo completo de projeto (cap. 24) é o [PPI-molde Comparece MT](../ppi_molde_comparece_mt).

## Mapa: capítulo → onde está no código

| Cap. | Assunto | Notebook · seção |
|---|---|---|
| 1–3 | Aprender com dados, vocabulário, CRISP-DM | U1 · abertura |
| 4 | Análise exploratória | U1 · 1 e 2 |
| 5 | Preparação e vazamento | U1 · 3 e 5 |
| 6 | Distâncias e escala | U1 · 6 |
| 7 | PCA | U1 · 8 |
| 8 | Anomalias | U1 · 9 |
| 9 | Treino, teste e baseline | U1 · 3 e 4; U2 · A1 |
| 10 | Teoria: complexidade × generalização | U2 · A e B3; Extra Redes Neurais · 5 |
| 11 | Regressão | U2 · Parte A |
| 12 | Regressão logística e métricas | U2 · B2 |
| 13–18 | k-NN, Naive Bayes, redes neurais, árvores, SVM, ensembles | U2 · B4 e B5 |
| 15 | Redes neurais e imagens | Extra Redes Neurais; Extra Visão Computacional |
| 19 | O que é um bom grupo | U3 · 2 |
| 20 | K-Means | U3 · 3 |
| 21 | Misturas gaussianas | U3 · 4 |
| 22 | Fuzzy C-Means | U3 · 5 |
| 23 | SOM | U3 · 6 |
| 24 | Da previsão à decisão | U3 · 7; [PPI-molde](../ppi_molde_comparece_mt) |

## Onde os notebooks gravam arquivos

Só o notebook de Visão Computacional grava alguma coisa (as fotos baixadas). Ele grava em `/content/visao_placas` no Colab ou em `ac_saida/visao_placas`, dentro da sua pasta de usuário, no laboratório. O caminho aparece na saída. Nada é gravado dentro desta pasta.
