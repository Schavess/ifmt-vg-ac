# 🏛️ PPI GovTech: sprints até o MVP

**AC · 4º TIA · 2026/2.** Em 4 semanas (03/11 a 01/12), cada grupo sai do papel e chega a um **MVP que funciona com dados reais**: uma base mínima, um modelo melhor que o baseline e uma tela de decisão.
Toda terça o grupo mostra **algo que roda** (arquivo, código, tela), e não só um documento.

O projeto de referência é o [PPI-molde Comparece MT](../ppi_molde_comparece_mt): cada passo abaixo tem um equivalente lá, e as [práticas semanais](../atividades) constroem o molde um pedaço por vez, sempre uma semana antes de o grupo precisar daquele pedaço.

---

## 🎯 O que conta como MVP

É o menor produto que permite a um gestor tomar uma decisão com dados reais. Não precisa ser bonito, mas precisa **rodar do zero na máquina de outra pessoa**.

**Piso obrigatório, em qualquer formato:**

1. **Base analítica** em CSV, com fonte pública citada, uma linha por unidade de análise (município, unidade de saúde, mês…) e cerca de 100 linhas ou mais.
2. **Pergunta, X e y**, cada um escrito em uma frase.
3. **Baseline** (`DummyClassifier`/`DummyRegressor` ou uma regra simples) e pelo menos **1 modelo** avaliado com o mesmo protocolo.
4. **Uma métrica justificada** e uma tabela "baseline × modelo".
5. **Uma saída de decisão:** ranking, lista priorizada ou alocação. É aí que entra a Otimização.
6. **Reprodutível:** repositório com README dizendo como rodar.

**Formatos aceitos (o grupo escolhe um):**

| Formato | Quando escolher | Pronto quando… |
|---|---|---|
| Notebook de fluxo completo | Grupo forte em Python, sem tempo para interface | Roda no Colab de ponta a ponta, do download ao ranking, com markdown explicando cada etapa |
| Dashboard Power BI | Grupo que já domina Power BI | Lê o `previsoes.csv` exportado pelo notebook e tem 2 telas (situação atual e priorização), com filtros |
| Web simples (Streamlit ou HTML) | Alguém confortável com front ou Streamlit | Abre no navegador, mostra KPIs, mapa ou tabela e o ranking, e deixa mudar um parâmetro (por exemplo, o orçamento) |

Nos três casos, **o notebook é o motor e o dashboard é a vitrine**. O modelo nunca é treinado dentro do Power BI.

---

## 📅 Calendário

| Terça | Sprint | Entrega do grupo | Prática da noite ([`atividades`](../atividades)) |
|---|---|---|---|
| **03/11** | 1 | **Check-in zero (Parcial II):** escopo fechado | O ETL: da fonte à base analítica |
| **10/11** | 1 | **Check-in 1:** base analítica v0 ⚠️ *ponto sem volta* | Experimento honesto: split, baselines e `Pipeline` |
| **17/11** | 1 → 2 | **Sprint review 1:** primeiro experimento honesto | Validação cruzada, árvores e sobreajuste |
| **24/11** | 2 | **Check-in 3:** modelo escolhido e decisão v0 | Perfis e decisão: K-Means e mochila |
| **01/12** | 2 | **Sprint review 2 e congelamento do MVP** | Tribunal do Pipeline (ensaio da banca) |
| 01 a 08/12 | — | **Banca** | |

> ⚠️ **10/11 é o ponto sem volta:** o grupo que não tiver a base v0 nessa data troca de fonte (veja os [planos B](#-riscos-e-planos-b)), para não perder a Sprint 2.

---

## ✅ Checklist de cada terça

O grupo só avança quando a entrega anterior está pronta. Cada uma é conferida em 2 minutos.

### Sprint 1: do problema ao baseline

**03/11 · Check-in zero**
- [ ] Pergunta analítica em uma frase, com a decisão e quem decide
- [ ] Unidade de análise definida (o que é uma linha?)
- [ ] y e X candidatos escritos
- [ ] Pelo menos uma fonte pública baixada, com link e data do download

**10/11 · Check-in 1: base analítica v0**
- [ ] Script ou notebook de ETL que gera `base_analitica.csv` a partir dos arquivos brutos
- [ ] Dicionário mínimo (variável, tipo, fonte, papel: X, y, ID ou descarte)
- [ ] EDA mínima: distribuição de y, nulos por coluna e 3 gráficos de relação com y
- [ ] Repositório público criado, com README

**17/11 · Sprint review 1: primeiro experimento honesto**
- [ ] Split treino/teste feito antes de qualquer ajuste, com `random_state=42`
- [ ] Baseline e 1 modelo dentro de `Pipeline`
- [ ] Tabela de métricas baseline × modelo, com a métrica justificada
- [ ] Demo de 5 min respondendo às 6 perguntas

### Sprint 2: do modelo ao MVP

**24/11 · Check-in 3: modelo escolhido e decisão v0**
- [ ] 2 ou 3 modelos comparados com validação cruzada só no treino; teste usado uma vez
- [ ] Previsões exportadas em `previsoes.csv` (ID, previsão e variáveis de contexto)
- [ ] Saída de decisão v0: ranking ou alocação sob uma restrição (orçamento, equipes, capacidade)
- [ ] Rascunho da tela: wireframe ou primeira versão no Power BI, Streamlit ou HTML

**01/12 · Sprint review 2 e congelamento**
- [ ] MVP roda do zero seguindo o README, testado por outro grupo
- [ ] Tela com KPIs, ranking e pelo menos um filtro ou parâmetro
- [ ] Seções de Metodologia e Resultados do artigo SBC escritas, com a tabela de métricas
- [ ] Ensaio do pitch, com a parte de AC em até 2 minutos

---

## ⏱️ O rito de cada terça (18:50–22:25)

| Bloco | Duração | O que acontece |
|---|---|---|
| Mini-aula | 40 min | Uma unidade da apostila, aplicada ao PPI-molde e à prática da semana |
| Stand-up | 20 min | 2 min por grupo: o que fizemos, o que faremos e o que nos trava. **Mostrando um artefato na tela**: só falar não vale |
| Oficina | 90 min | Trabalho nos grupos, com o professor circulando |
| Revisão cruzada | 30 min | O par de grupos troca o notebook e um tenta rodar o do outro |
| Fechamento | 10 min | Cada grupo atualiza o quadro de tarefas e escreve a meta da próxima terça |

**Entre as terças:** até **domingo, 23h59**, o grupo faz um commit no repositório e atualiza o quadro (GitHub Projects ou Trello).
**No fim de cada sprint (17/11 e 01/12):** o stand-up vira *sprint review*, com demo de 5 minutos e perguntas da turma e do professor.

---

## 👥 Papéis no grupo e revisão entre pares

Cada integrante assume um papel na Sprint 1 e troca na Sprint 2. Assim todos passam por dados e por modelo, e a banca vai cobrar isso.

| Papel | Responde por | Na terça, mostra |
|---|---|---|
| Dono dos dados | ETL, dicionário, `base_analitica.csv` | A base e os nulos |
| Dono do modelo | Split, baseline, Pipeline, métricas | A tabela baseline × modelo |
| Dono da decisão | Ranking ou otimização e dashboard | A tela ou a lista priorizada |
| Escriba e facilitador | README, quadro de tarefas, artigo, tempo do stand-up | O stand-up |

Em grupos de 5 ou 6, dados e modelo ganham um segundo integrante.

**Pares de revisão:** os grupos são pareados (A↔B, C↔D…) e o par se mantém nas duas sprints. Na revisão cruzada, o grupo revisor tenta rodar o notebook do outro **sem ajuda** e anota:
1. Rodou do zero? Se não, em que célula parou.
2. Encontrei vazamento ou ID usado como feature?
3. Uma sugestão concreta.

Uma boa revisão conta como participação do grupo revisor.

---

## 🚦 Semáforo semanal

Serve para o grupo ver onde está, não é nota. As perguntas são sempre as mesmas, e são as que a banca vai fazer.

| Pergunta | 🔴 Vermelho | 🟡 Amarelo | 🟢 Verde |
|---|---|---|---|
| 1. Qual é o y? | Não sabe | Sabe, mas a coluna não existe na base | Coluna na base, distribuição mostrada |
| 2. Qual é o baseline? | Nenhum | Citado, não rodado | Rodado e na tabela de métricas |
| 3. Por que essa métrica? | "Acurácia, porque sim" | Métrica certa, sem justificar | Ligada ao custo do erro na decisão pública |
| 4. Onde foi feito o split? | Depois do pré-processamento | Antes, sem `random_state` | Antes de tudo, fixo, teste usado uma vez |
| 5. Há vazamento? | ID ou informação do futuro em X | Não verificou | Verificou, e está tudo dentro de `Pipeline` |
| 6. A conclusão tem evidência? | Afirmação sem número | Número sem comparação | Comparação com baseline e limitações ditas |
| 7. Roda do zero? | Não | Roda com ajuda do autor | O par rodou sozinho pelo README |

Grupo com 3 ou mais itens em vermelho numa terça recebe atendimento prioritário na oficina seguinte.

---

## 🛟 Riscos e planos B

| Risco | Sinal | Plano B |
|---|---|---|
| A fonte não existe ou não baixa | Em 10/11 não há CSV bruto | Trocar para uma base já tabulada no mesmo tema: IBGE/SIDRA, TSE, DATASUS/TabNet, INPE, dados.gov.br. A pergunta se mantém; a fonte muda |
| Base pequena demais | Menos de cerca de 100 linhas | Unidade de análise mais fina (município × ano em vez de município) ou região maior (MT → Centro-Oeste) |
| Não há y rotulado | Ninguém consegue dizer qual é a coluna y | Tarefa não supervisionada (agrupamento, como na prática de 24/11) e decisão sobre os grupos; ou y criado por regra a partir de um limiar oficial |
| O modelo não bate o baseline | Métrica igual ou pior que a do Dummy | É um resultado válido. Reportar com honestidade, testar 1 ou 2 features novas e manter o ranking com o modelo como evidência |
| A otimização virou "enfeite" | Não há recurso limitado | Versão mínima: escolher os k municípios que maximizam o benefício previsto com orçamento B (mochila, como no PPI-molde) |
| Grupo desequilibrado | Uma pessoa faz tudo | Rodízio de papéis e commit individual visível no repositório |

---

## ❓ Perguntas que sempre aparecem

<details><summary><b>Precisa de deep learning?</b></summary>

Não. Um modelo simples bem validado vale mais na banca que um complexo sem baseline.
</details>

<details><summary><b>Nosso modelo deu 99% de acurácia!</b></summary>

Desconfie: quase sempre é vazamento ou classe desbalanceada. Compare com o Dummy e veja o recall da classe rara. A prática de 01/12 ([Tribunal do Pipeline](../atividades/2026-12-01_Aula06_Tribunal_do_Pipeline)) mostra como isso acontece.
</details>

<details><summary><b>Não achamos dado do nosso município</b></summary>

Suba um nível (UF ou região) ou mude a unidade de análise. A pergunta pode continuar a mesma.
</details>

<details><summary><b>O Power BI não treina o modelo?</b></summary>

Não. O notebook treina e exporta `previsoes.csv`; o Power BI só mostra.
</details>

<details><summary><b>Quantos modelos temos que testar?</b></summary>

O baseline e mais 2 ou 3, com o mesmo protocolo, mudando uma coisa por vez.
</details>

<details><summary><b>Otimização é de outra disciplina, não?</b></summary>

É, mas a entrada dela é a saída do modelo: previsão mais restrição dão a decisão.
</details>

---

## 📁 Como organizar o repositório do grupo

Use o [PPI-molde](../ppi_molde_comparece_mt) como modelo, e o [`PPI_TEMPLATE_GRUPO.ipynb`](../ppi_molde_comparece_mt/notebooks/PPI_TEMPLATE_GRUPO.ipynb) como ponto de partida:

```
nome-do-projeto/
├── README.md            ← pergunta, fontes, como rodar
├── dados/
│   ├── brutos/          ← o que foi baixado (ou o link, se for grande)
│   └── base_analitica.csv
├── notebooks/
│   ├── 01_etl.ipynb     ← dos brutos à base analítica
│   └── 02_modelo.ipynb  ← split, baseline, modelos, previsões, decisão
└── saida/               ← previsoes.csv, ranking, dashboard
```

O regulamento e o plano oficial da PPI ficam com a coordenação e com o professor.
