# Prática 03/11 · Da fonte à base analítica: o ETL do PPI-molde

AC • 4º TIA • 03/11/2026 • Aula 02 • apostila: cap. 3, 4, 6 e 7 • parte do [PPI-molde Comparece MT](../../ppi_molde_comparece_mt)

**Pergunta:** como sair dos arquivos brutos do TSE para uma base analítica com uma linha por município, de forma que qualquer pessoa chegue aos mesmos números?

## Objetivo

Construir em código o ETL do PPI-molde: ler o perfil do eleitorado e os resultados de 2022 e 2026 direto dos ZIP do TSE, somar por município, juntar as fontes pela chave, calcular a distância até Cuiabá, validar e salvar `base_analitica.csv`. É a entrega do check-in 1 (10/11): base v0, dicionário e EDA mínima.

## Como abrir

**No Google Colab (obrigatório nesta prática: os dados vêm da internet)**
1. Abra o notebook pelo botão abaixo.

   [![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Schavess/ifmt-vg-ac/blob/main/atividades/2026-11-03_Aula02_ETL_Base_Analitica/2026-11-03_Aula02_ETL_Base_Analitica_INICIAL.ipynb)

2. **Arquivo > Salvar uma cópia no Drive**, para não perder o que fizer.
3. A célula de extração lê os arquivos direto do TSE e leva cerca de um minuto.

## O que você vai fazer

| TODO | Tarefa | Apostila |
|---|---|---|
| 1 | Percentuais do perfil por município | cap. 3 e 4 |
| 2 | Filtrar presidente, 1º turno, MT | cap. 3 |
| 3 | Somar as zonas e calcular a abstenção | cap. 3 |
| 4 | Juntar as fontes pela chave, 1 para 1 | cap. 6 |
| 5 | Distância até Cuiabá (haversine) | cap. 7 |
| 6 | Retirar o município sem histórico, validar e salvar | cap. 6 |

## Dados

Nenhum arquivo nesta pasta: o notebook lê, direto dos servidores, o perfil do eleitorado 2026 e os resultados de 2022 e 2026 do [TSE](https://dadosabertos.tse.jus.br), e as coordenadas das sedes municipais (IBGE, via [kelvins/municipios-brasileiros](https://github.com/kelvins/municipios-brasileiros)). São dados públicos, sem nenhum dado pessoal.
A base gerada vai para `/content/aula02/base_analitica.csv` no Colab. Ela deve ser idêntica à do [PPI-molde](../../ppi_molde_comparece_mt/dados/base_analitica.csv).

## Saída esperada

A última célula (verificação) deve mostrar:

```
✅ perfil: 142 municípios com os percentuais
✅ resultados: 142 municípios em 2026 e 141 em 2022
✅ abstenção média em 2026: 23,45%
✅ abstenção média em 2022: 25,94%
✅ maior distância até Cuiabá: 831 km
✅ Boa Esperança do Norte retirada; 141 municípios
✅ base_analitica.csv salva com 15 colunas

7 de 7 verificações OK
```

Se aparecer ❌, o erro está no TODO daquela linha. Os números só batem com `random_state=42`.

## Critérios (o que o professor vai olhar)

1. **Base idêntica à do PPI-molde** (141 municípios, mesmas médias).
2. **Junções com `validate='1:1'`** e checagens com `assert`.
3. **Decisão sobre o município sem histórico** escrita com as suas palavras.
4. **Respostas às 2 perguntas para discussão.**
5. **Todas as verificações OK** na última célula.

## Desafio extra (para quem terminar)

Acrescente uma coluna com a **variação** da abstenção (2026 − 2022). Ela pode entrar em X? Por quê?
