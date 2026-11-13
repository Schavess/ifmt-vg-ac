# Prática 01/12 · Tribunal do Pipeline: auditar e consertar um experimento

AC • 4º TIA • 01/12/2026 • Aula 06 • apostila: cap. 2, 5, 6, 9, 11 e 24 • parte do [PPI-molde Comparece MT](../../ppi_molde_comparece_mt)

**Pergunta:** o experimento do Grupo Réu tem R² de 1. Quais crimes de método explicam esse número, e qual é o resultado honesto?

## Objetivo

Auditar um experimento com erros comuns (vazamento, escala antes do split, escolha pelo teste, ausência de baseline), consertá-lo passo a passo e ensaiar as 7 perguntas da banca. Depois, passar o notebook do grupo pela mesma lista.

## Como abrir

**No Google Colab (recomendado)**
1. Abra o notebook pelo botão abaixo. Ele lê os dados do GitHub da disciplina, então precisa de internet.

   [![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Schavess/ifmt-vg-ac/blob/main/atividades/2026-12-01_Aula06_Tribunal_do_Pipeline/2026-12-01_Aula06_Tribunal_do_Pipeline_INICIAL.ipynb)

2. **Arquivo > Salvar uma cópia no Drive**, para não perder o que fizer.
3. Se a célula de leitura der erro, arraste o arquivo `dados/base_analitica.csv` para a aba **Arquivos** (ícone de pasta à esquerda) e rode a célula de novo.

**No computador do laboratório (sem internet)**
1. Copie esta pasta inteira (com a subpasta `dados`).
2. Abra `2026-12-01_Aula06_Tribunal_do_Pipeline_INICIAL.ipynb` no Jupyter ou no VS Code. As bibliotecas estão no `requirements.txt` da raiz do repositório.

## O que você vai fazer

| TODO | Tarefa | Apostila |
|---|---|---|
| 1 | Marcar os crimes do réu no catálogo | cap. 2, 5 e 6 |
| 2 | Tirar de X o que causa vazamento | cap. 6 |
| 3 | Split reprodutível, antes de tudo | cap. 5 |
| 4 | Comparar candidatos e réguas com validação cruzada | cap. 5, 9 e 11 |
| 5 | Escolher pela CV e abrir o teste uma vez | cap. 5 e 24 |

## Dados

`dados/base_analitica.csv`: a base do [PPI-molde](../../ppi_molde_comparece_mt), 141 linhas (uma por município de MT) e 15 colunas: abstenção no 1º turno para presidente em 2026 (y) e em 2022, crescimento do eleitorado, distância até Cuiabá e perfil do eleitorado.
Fontes: [TSE](https://dadosabertos.tse.jus.br) (perfil do eleitorado 2026 e resultados de 2022 e 2026) e coordenadas das sedes (IBGE). Ela é gerada pelo ETL da prática de 03/11. São dados públicos, sem nenhum dado pessoal.

## Saída esperada

A última célula (verificação) deve mostrar:

```
✅ veredito: os 5 crimes certos, sem acusação falsa
✅ X sem as contagens de 2026 (7 variáveis)
✅ split reprodutível: 112 no treino e 29 no teste
✅ CV: linear com MAE 1,33
✅ CV: persistência com MAE 1,78
✅ escolha pela CV: Linear
✅ teste: MAE 1,23 do escolhido

7 de 7 verificações OK
```

Se aparecer ❌, o erro está no TODO daquela linha. Os números só batem com `random_state=42`.

## Critérios (o que o professor vai olhar)

1. **Veredito correto**, sem acusações falsas.
2. **Experimento consertado** chegando ao mesmo resultado do PPI-molde.
3. **Ensaio da banca** feito em dupla.
4. **Checklist final aplicado ao notebook do grupo.**
5. **Todas as verificações OK** na última célula.

## Desafio extra (para quem terminar)

Rode o réu só com o crime A consertado (sem as colunas de 2026). O R² dele cai para quanto? E se consertar só o B?
