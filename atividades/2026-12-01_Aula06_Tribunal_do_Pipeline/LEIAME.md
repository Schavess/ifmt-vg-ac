# Prática: Tribunal do Pipeline: auditar e consertar um experimento

AC • 4º TIA • 01/12/2026 • Aula 06 • apostila: cap. 2, 5, 9, 12, 13 e 24

**Pergunta:** um colega diz que o k-NN dele "acerta mais de 80% dos municípios" de abstenção alta. O resultado se sustenta?

## Objetivo

Encontrar os **5 erros** de um experimento que roda sem erro (ID como feature, vazamento do alvo, escala antes do split, hiperparâmetro escolhido no teste, só acurácia e sem baseline), consertar um por um e medir quanto o resultado "encolhe". No fim, aplicar a mesma auditoria ao **notebook do grupo**, como preparação para a banca da PPI.

## Como abrir

**No Google Colab (recomendado)**
1. Abra o notebook pelo botão abaixo. Ele lê os dados do GitHub da disciplina, então precisa de internet.

   [![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Schavess/ifmt-vg-ac/blob/main/atividades/2026-12-01_Aula06_Tribunal_do_Pipeline/2026-12-01_Aula06_Tribunal_do_Pipeline_INICIAL.ipynb)

2. **Arquivo > Salvar uma cópia no Drive**, para não perder o que fizer.
3. Se a célula de leitura der erro, arraste o arquivo `dados/municipios_mt_votos.csv` para a aba **Arquivos** (ícone de pasta à esquerda) e rode a célula de novo.

**No computador do laboratório (sem internet)**
1. Copie esta pasta inteira (com a subpasta `dados`).
2. Abra `2026-12-01_Aula06_Tribunal_do_Pipeline_INICIAL.ipynb` no Jupyter ou no VS Code. As bibliotecas estão no `requirements.txt` da raiz do repositório.
3. O notebook só lê arquivos: não grava nada.

## O que você vai fazer

| TODO | Tarefa | Apostila |
|---|---|---|
| 1 | X só com as 4 colunas de perfil | cap. 2, 5 |
| 2 | Separar primeiro, com `stratify=y` | cap. 9 |
| 3 | `make_pipeline(StandardScaler(), KNeighborsClassifier())` | cap. 5 |
| 4 | `GridSearchCV` no treino para escolher o k | cap. 9, 13 |
| 5 | Baseline e acurácia, precisão, recall e F1 no teste, uma vez | cap. 9, 12 |

## Dados

`dados/municipios_mt_votos.csv`: 142 linhas (uma por município de MT), 14 colunas: perfil do eleitorado, abstenção e votos brancos e nulos do 1º turno para presidente.
Fonte: TSE, [perfil do eleitorado 2026](https://dadosabertos.tse.jus.br/dataset/eleitorado-2026) e [resultados do 1º turno de 04/10/2026](https://dadosabertos.tse.jus.br/dataset/resultados-2026), agregados por município. São dados públicos, sem nenhum dado pessoal.

## Saída esperada

```
Conclusão do colega: k-NN com k=9 acerta 83% dos municípios!

k escolhido pela CV: 5 | F1 médio na CV: 0.56
Baseline           acurácia 0.69 | precisão 0.00 | recall 0.00 | F1 0.00
k-NN consertado    acurácia 0.78 | precisão 0.67 | recall 0.55 | F1 0.60

Colega (com os 5 erros): acurácia 0.83 com k=9
Consertado:              acurácia 0.78 com k=5 | recall 0.55 | baseline 0.69
```

A última célula (verificação) deve mostrar:

```
✅ X só com as 4 colunas de perfil
✅ teste estratificado: 36 municípios, 11 "alta"
✅ escala dentro do Pipeline
✅ k escolhido pela CV no treino = 5
✅ baseline com recall 0 no teste
✅ o resultado honesto é menor que o do colega

6 de 6 verificações OK
```

Se aparecer ❌, o erro está no TODO daquela linha. Os números só batem com `random_state=42`.

## Critérios (o que o professor vai olhar)

1. **Os 5 erros listados** numa célula de texto, cada um com a explicação de por que infla o resultado.
2. **Experimento consertado** com 6 de 6 na verificação.
3. **Tabela de auditoria preenchida no notebook do grupo**, com evidência em cada linha.

## Desafio extra (para quem terminar)

Rode o experimento do colega consertando **só** o erro 2 (tirar `PCT_COMPARECIMENTO`) e veja quanto a acurácia cai. Qual dos erros "inflava" mais o resultado?
