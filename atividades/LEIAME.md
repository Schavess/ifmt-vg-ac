# Práticas semanais

Uma pasta por prática de laboratório, com a data e o tema no nome. **As práticas constroem, um pedaço por semana, o [PPI-molde Comparece MT](../ppi_molde_comparece_mt)**, na mesma ordem das entregas da PPI: o que vocês fazem na prática é o que o grupo faz no projeto na semana seguinte. **Práticas extras podem entrar a qualquer semana**, sempre neste mesmo formato.

| Data | Pasta | Prática | Apostila |
|---|---|---|---|
| 27/10 | [`2026-10-27_Aula01_O_Problema`](2026-10-27_Aula01_O_Problema) | O problema: onde o eleitor de MT deixa de votar? (pergunta, unidade, y, X e a ficha do problema) | cap. 1 a 4 |
| 03/11 | [`2026-11-03_Aula02_ETL_Base_Analitica`](2026-11-03_Aula02_ETL_Base_Analitica) | Da fonte à base analítica: o ETL (TSE → `base_analitica.csv`, dicionário e EDA) | cap. 3, 4, 6 e 7 |
| 10/11 | [`2026-11-10_Aula03_Experimento_Honesto`](2026-11-10_Aula03_Experimento_Honesto) | Experimento honesto: split, dois baselines e regressão linear em `Pipeline` | cap. 5, 6 e 8 |
| 17/11 | [`2026-11-17_Aula04_Validacao_Cruzada_Arvores`](2026-11-17_Aula04_Validacao_Cruzada_Arvores) | Qual modelo escolher? Validação cruzada, árvores, sobreajuste e `GridSearchCV` | cap. 5, 10, 11, 13 e 16 |
| 24/11 | [`2026-11-24_Aula05_Perfis_e_Decisao`](2026-11-24_Aula05_Perfis_e_Decisao) | Da previsão à decisão: PCA, K-Means e a carteira sob orçamento (mochila) | cap. 7, 17 a 19 e 24 |
| 01/12 | [`2026-12-01_Aula06_Tribunal_do_Pipeline`](2026-12-01_Aula06_Tribunal_do_Pipeline) | Tribunal do Pipeline: auditar e consertar um experimento (ensaio da banca) | cap. 2, 5, 6, 9, 11 e 24 |
| … | *práticas extras* | *podem entrar a qualquer semana, no mesmo formato* | |

## O que vem em cada prática

```
atividades/AAAA-MM-DD_AulaNN_Tema/
├── LEIAME.md                        ← leia primeiro: pergunta, objetivo, critérios e saída esperada
├── AAAA-MM-DD_AulaNN_Tema_INICIAL.ipynb   ← o notebook com # TODO que você completa
└── dados/                           ← CSV pequeno, quando a prática precisa (dados públicos)
```

**Como fazer:**
1. Leia o `LEIAME.md`.
2. Abra o notebook no Colab, pelo botão do LEIAME, e salve uma cópia no Drive.
3. Complete os `# TODO` de cima para baixo.
4. Rode a **última célula, de verificação**. Ela mostra ✅ ou ❌ para cada item e deve terminar em "N de N verificações OK".

> 🔄 **Saiu prática nova?** Baixe o ZIP de novo ou rode `git pull`. Antes, salve os seus notebooks em outro lugar (ou no Drive).
