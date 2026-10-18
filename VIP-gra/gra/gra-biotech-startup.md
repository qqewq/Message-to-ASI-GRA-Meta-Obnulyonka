# GRA-BioPharma: верифицируемый ИИ для поиска лекарств

# GRA-BioPharma: Verifiable AI for Drug Discovery

## Аннотация / Abstract

### Русский

GRA-BioPharma — это концептуальная мультиагентная архитектура для приоритизации биологических мишеней и планирования ранних этапов drug discovery. Она не заменяет биологические исследования, химический синтез, лабораторные эксперименты или клинические испытания. Её задача — помочь исследователям выбрать, какие гипотезы следует проверить в первую очередь при ограниченном бюджете.

GRA объединяет несколько типов информации:

- литературные и экспериментальные данные;
- генетические доказательства;
- согласованность биологических путей;
- противоречия;
- риски безопасности;
- стоимость проверки;
- публикационный hype.

В синтетическом benchmark использовались 5 000 кандидатных мишеней и бюджет в 100 экспериментов на один прогон. На 300 Monte Carlo-прогонах GRA находила в среднем 10.13 истинно релевантных мишеней. Simple evidence baseline находил 2.64, а literature-only baseline — 0.12.

Таким образом, в рамках этой модели GRA находила примерно в 3.8 раза больше релевантных мишеней, чем simple evidence, и примерно в 84 раза больше, чем literature-only. GRA превосходила simple evidence в 99.3% прогонов, а literature-only — в 100% прогонов.

Эти результаты подтверждают работоспособность архитектуры в заданной синтетической среде. Они не доказывают, что GRA уже способна находить реальные лекарства, предсказывать клиническую эффективность или заменять лабораторную и медицинскую экспертизу.

### English

GRA-BioPharma is a conceptual multi-agent architecture for biological-target prioritization and early-stage drug discovery planning. It does not replace biology, chemical synthesis, laboratory experiments, or clinical trials. Its purpose is to help researchers decide which hypotheses should be tested first when resources are limited.

GRA combines several types of information:

- literature and experimental evidence;
- genetic support;
- biological pathway coherence;
- contradictions;
- safety risks;
- validation cost;
- publication hype.

The synthetic benchmark contained 5,000 candidate targets and a budget of 100 experiments per run. Across 300 Monte Carlo runs, GRA identified an average of 10.13 truly relevant targets. The simple evidence baseline identified 2.64, while the literature-only baseline identified 0.12.

Within this model, GRA therefore identified approximately 3.8 times more relevant targets than the simple evidence baseline and approximately 84 times more than the literature-only baseline. GRA outperformed simple evidence in 99.3% of runs and literature-only in 100% of runs.

These results demonstrate that the architecture works under the specified synthetic conditions. They do not prove that GRA can already discover real drugs, predict clinical efficacy, or replace laboratory and medical expertise.

***

## 1. Исследовательская проблема / The Research Problem

### Русский

В drug discovery невозможно проверить все потенциальные мишени. Команда может иметь тысячи гипотез, но ограниченное количество экспериментов, времени и денег.

Высокая популярность мишени не гарантирует её научной ценности. У неё могут быть:

- противоречивые результаты;
- слабая экспериментальная база;
- отсутствие генетической поддержки;
- неубедительный биологический механизм;
- повышенный риск токсичности;
- высокая стоимость валидации;
- публикационный или инвестиционный hype.

Поэтому главная задача состоит не в том, чтобы найти наиболее обсуждаемую мишень. Необходимо определить, какая гипотеза заслуживает следующего эксперимента.

### English

Drug discovery cannot test every possible target. A research team may face thousands of hypotheses while having only a limited number of experiments, time, and funding.

A target’s popularity does not guarantee scientific value. It may be affected by:

- contradictory findings;
- weak experimental support;
- limited genetic evidence;
- an unconvincing biological mechanism;
- substantial toxicity risk;
- high validation cost;
- publication or investment hype.

The central task is therefore not to select the most frequently discussed target. It is to determine which hypothesis deserves the next experiment.

***

## 2. Архитектура GRA / The GRA Architecture

### Русский

GRA — это слой управления исследовательским поиском. Она не выдаёт окончательную истину, а формирует объяснимый и проверяемый порядок приоритетов.

Рабочий цикл можно представить так:

\[
\text{данные}
\rightarrow
\text{гипотезы}
\rightarrow
\text{критика}
\rightarrow
\text{ранжирование}
\rightarrow
\text{эксперимент}
\rightarrow
\text{обновление знаний}.
\]

Итог GRA следует понимать не как утверждение:

> Эта мишень точно сработает.

А как вывод:

> При имеющихся данных и ограниченном бюджете эту мишень разумно проверить раньше других.

Поэтому:

\[
\text{вывод GRA}
\neq
\text{биологическая истина},
\]

а:

\[
\text{вывод GRA}
=
\text{приоритизированный план проверки гипотез}.
\]

### English

GRA is a governance layer for research search. It does not produce final truth; it creates an explainable and testable priority order.

Its workflow can be represented as:

\[
\text{data}
\rightarrow
\text{hypotheses}
\rightarrow
\text{critique}
\rightarrow
\text{ranking}
\rightarrow
\text{experiment}
\rightarrow
\text{knowledge update}.
\]

The output should not be interpreted as:

> This target will definitely work.

It should be interpreted as:

> Given the available evidence and the limited budget, this target deserves testing before the alternatives.

Therefore:

\[
\text{GRA output}
\neq
\text{biological truth},
\]

but:

\[
\text{GRA output}
=
\text{a prioritized plan for testing hypotheses}.
\]

***

## 3. Представление кандидатной мишени / Target Representation

### Русский

Каждая мишень \(T_i\) описывается набором наблюдаемых признаков:

\[
X_i =
\left(
L_i,
E_i,
G_i,
P_i,
C_i,
R_i,
V_i,
H_i
\right).
\]

| Обозначение | Значение |
|---|---|
| \(L_i\) | поддержка в научной литературе |
| \(E_i\) | экспериментальная поддержка |
| \(G_i\) | генетические доказательства |
| \(P_i\) | правдоподобие биологического пути |
| \(C_i\) | уровень противоречий |
| \(R_i\) | риск безопасности |
| \(V_i\) | стоимость и сложность проверки |
| \(H_i\) | публикационный hype или popularity bias |

Скрытая истинная релевантность мишени обозначается:

\[
Y_i \in \{0,1\}.
\]

Если \(Y_i=1\), мишень считается релевантной в рамках искусственного benchmark. В реальных исследованиях это значение неизвестно и может быть оценено только через последовательную проверку гипотез.

### English

Each target \(T_i\) is described by a set of observable features:

\[
X_i =
\left(
L_i,
E_i,
G_i,
P_i,
C_i,
R_i,
V_i,
H_i
\right).
\]

| Symbol | Meaning |
|---|---|
| \(L_i\) | literature support |
| \(E_i\) | experimental support |
| \(G_i\) | genetic evidence |
| \(P_i\) | biological pathway plausibility |
| \(C_i\) | contradiction level |
| \(R_i\) | safety risk |
| \(V_i\) | validation cost and complexity |
| \(H_i\) | publication hype or popularity bias |

The hidden true relevance of a target is represented as:

\[
Y_i \in \{0,1\}.
\]

When \(Y_i=1\), the target is considered relevant within the synthetic benchmark. In real research, this value is unknown and can be estimated only through sequential hypothesis testing.

***

## 4. Скоринг и штраф за противоречия / Scoring and Contradiction Penalties

### Русский

В GRA литературная популярность рассматривается только как один из сигналов. Она не должна автоматически определять приоритет мишени.

Итоговый рейтинг benchmark рассчитывался по формуле:

\[
S_{\text{GRA}}(T_i)
=
0.70E_{\text{GRA}}(T_i)
-
0.30R_{\text{GRA}}(T_i)
+
0.05V_{\text{GRA}}(T_i).
\]

Компонента доказательств:

\[
E_{\text{GRA}}(T_i)
=
0.15\tilde L^{\text{corr}}_i
+
0.20E_i
+
0.20G_i
+
0.35P_i.
\]

Литературная поддержка корректировалась на hype:

\[
\tilde L^{\text{corr}}_i
=
\max
\left(
0,
\log(1+L_i)-1.2H_i
\right).
\]

Компонента риска включала противоречия, безопасность и стоимость проверки:

\[
R_{\text{GRA}}(T_i)
=
0.55C_i
+
0.35R_i
+
0.20\tilde V_i.
\]

В результате мишень с большим количеством публикаций могла получить низкий приоритет, если её популярность сопровождалась противоречиями, повышенным риском или дорогой валидацией.

Общий принцип:

\[
\text{публикационная популярность}
\neq
\text{истинная релевантность}.
\]

### English

Within GRA, literature popularity is treated as only one signal. It does not automatically determine target priority.

The benchmark score was calculated as:

\[
S_{\text{GRA}}(T_i)
=
0.70E_{\text{GRA}}(T_i)
-
0.30R_{\text{GRA}}(T_i)
+
0.05V_{\text{GRA}}(T_i).
\]

The evidence component was:

\[
E_{\text{GRA}}(T_i)
=
0.15\tilde L^{\text{corr}}_i
+
0.20E_i
+
0.20G_i
+
0.35P_i.
\]

Literature support was corrected for hype:

\[
\tilde L^{\text{corr}}_i
=
\max
\left(
0,
\log(1+L_i)-1.2H_i
\right).
\]

The risk component included contradictions, safety, and validation cost:

\[
R_{\text{GRA}}(T_i)
=
0.55C_i
+
0.35R_i
+
0.20\tilde V_i.
\]

Consequently, a target with many publications could receive a low priority if its popularity was accompanied by contradictions, safety concerns, or expensive validation.

The general principle is:

\[
\text{publication popularity}
\neq
\text{true relevance}.
\]

***

## 5. Синтетический benchmark / The Synthetic Benchmark

### Русский

Для проверки GRA был создан искусственный исследовательский мир. Его задача состояла в том, чтобы оценить, насколько хорошо разные стратегии выбирают релевантные мишени при одинаковом бюджете.

Benchmark включал:

- 5 000 кандидатных мишеней в каждом прогоне;
- примерно 10% истинно релевантных мишеней;
- бюджет в 100 экспериментов;
- популярные, но неправильные мишени;
- небезопасные популярные мишени;
- противоречивые данные;
- публикационный hype;
- различную стоимость проверки;
- 300 независимых Monte Carlo-прогонов.

Сравнивались три метода:

| Метод | Принцип |
|---|---|
| Literature-only | Ориентация преимущественно на публикационную популярность |
| Simple evidence | Использование базовых литературных, экспериментальных и генетических сигналов |
| GRA | Учет доказательств, механизма, противоречий, безопасности, стоимости и hype |

### English

A synthetic research environment was created to evaluate GRA. The goal was to measure how well different strategies identify relevant targets under the same budget.

The benchmark included:

- 5,000 candidate targets per run;
- approximately 10% truly relevant targets;
- a budget of 100 experiments;
- popular but incorrect targets;
- popular unsafe targets;
- contradictory evidence;
- publication hype;
- different validation costs;
- 300 independent Monte Carlo runs.

Three methods were compared:

| Method | Principle |
|---|---|
| Literature-only | Primarily follows publication popularity |
| Simple evidence | Uses basic literature, experimental, and genetic signals |
| GRA | Combines evidence, mechanism, contradictions, safety, cost, and hype correction |

***

## 6. Результаты / Results

### Русский

| Метод | Релевантные мишени | Precision | Бесполезные эксперименты |
|---|---:|---:|---:|
| Literature-only | 0.12 | 0.0012 | 99.88 |
| Simple evidence | 2.64 | 0.0264 | 97.36 |
| GRA | 10.13 | 0.1013 | 89.87 |

При одинаковом бюджете GRA находила в среднем 10.13 релевантных мишеней. Simple evidence находил 2.64, а literature-only — 0.12.

Относительное преимущество над simple evidence:

\[
\frac{10.13}{2.64}
\approx 3.84.
\]

Относительное преимущество над literature-only:

\[
\frac{10.13}{0.12}
\approx 84.4.
\]

Следовательно, GRA обеспечила примерно 3.8-кратное преимущество над simple evidence и примерно 84-кратное преимущество над literature-only в рамках данного benchmark.

Однако сравнение с \(0.12\) следует интерпретировать осторожно: при очень малом базовом значении относительный коэффициент становится большим. Поэтому важны и абсолютные показатели.

### English

| Method | Relevant targets | Precision | Wasted experiments |
|---|---:|---:|---:|
| Literature-only | 0.12 | 0.0012 | 99.88 |
| Simple evidence | 2.64 | 0.0264 | 97.36 |
| GRA | 10.13 | 0.1013 | 89.87 |

Under the same budget, GRA identified an average of 10.13 relevant targets. Simple evidence identified 2.64, while literature-only identified 0.12.

The improvement over simple evidence was:

\[
\frac{10.13}{2.64}
\approx 3.84.
\]

The improvement over literature-only was:

\[
\frac{10.13}{0.12}
\approx 84.4.
\]

Thus, within this benchmark, GRA achieved approximately a 3.8-fold improvement over simple evidence and an approximately 84-fold improvement over literature-only.

The comparison with \(0.12\) should be interpreted cautiously because relative ratios become very large when the baseline is extremely small. The absolute values are therefore also important.

***

## 7. Статистический анализ / Statistical Analysis

### Русский

На 300 парных прогонах GRA превосходила:

- literature-only в 100% случаев;
- simple evidence в 99.3% случаев.

Использовался односторонний paired Wilcoxon signed-rank test:

\[
H_0:
\text{GRA не превосходит baseline},
\]

\[
H_1:
\text{GRA находит больше релевантных мишеней}.
\]

| Сравнение | Среднее GRA | Среднее baseline | Разница | Win rate | \(p\)-value |
|---|---:|---:|---:|---:|---:|
| GRA vs literature-only | 10.13 | 0.12 | +10.01 | 100.0% | \(2.2\times10^{-51}\) |
| GRA vs simple evidence | 10.13 | 2.64 | +7.49 | 99.3% | \(4.9\times10^{-51}\) |

Полученные значения показывают устойчивое преимущество GRA внутри выбранной симуляции. Но статистическая значимость не устраняет ограничений самой модели. Она говорит о стабильности результата в benchmark, а не о доказанной эффективности в реальной фармакологии.

### English

Across 300 paired runs, GRA outperformed:

- literature-only in 100% of runs;
- simple evidence in 99.3% of runs.

A one-sided paired Wilcoxon signed-rank test was used:

\[
H_0:
\text{GRA does not outperform the baseline},
\]

\[
H_1:
\text{GRA identifies more relevant targets}.
\]

| Comparison | GRA mean | Baseline mean | Difference | Win rate | \(p\)-value |
|---|---:|---:|---:|---:|---:|
| GRA vs literature-only | 10.13 | 0.12 | +10.01 | 100.0% | \(2.2\times10^{-51}\) |
| GRA vs simple evidence | 10.13 | 2.64 | +7.49 | 99.3% | \(4.9\times10^{-51}\) |

These values indicate a stable advantage for GRA within the selected simulation. Statistical significance, however, does not remove the limitations of the model. It demonstrates robustness within the benchmark, not proven effectiveness in real pharmacology.

***

## 8. Верификационный цикл / The Verification Loop

### Русский

Рейтинг сам по себе не является научным результатом. Его функция — определить следующий наиболее информативный шаг.

Для каждой мишени GRA должна формировать:

- проверяемое предсказание;
- минимальный информативный эксперимент;
- критерий подтверждения;
- критерий опровержения;
- оценку ожидаемого информационного выигрыша;
- уровень уверенности;
- список допущений и альтернативных объяснений.

Цикл имеет вид:

\[
H
\xrightarrow{\text{GRA}}
P(H)
\xrightarrow{\text{эксперимент}}
E_{\text{new}}
\xrightarrow{\text{обновление}}
\Psi_{t+1}.
\]

Здесь \(H\) — гипотеза, \(P(H)\) — предсказание, \(E_{\text{new}}\) — результат эксперимента, а \(\Psi_{t+1}\) — обновлённое состояние исследовательской программы.

После эксперимента приоритет мишени должен пересчитываться. Положительный результат может повысить её рейтинг, отрицательный — снизить, а неоднозначный результат — привести к дополнительной проверке.

### English

A ranking is not a scientific result by itself. Its purpose is to identify the next most informative step.

For each target, GRA should generate:

- a testable prediction;
- the cheapest meaningful experiment;
- a confirmation criterion;
- a falsification criterion;
- an estimate of expected information gain;
- a confidence level;
- assumptions and alternative explanations.

The loop is:

\[
H
\xrightarrow{\text{GRA}}
P(H)
\xrightarrow{\text{experiment}}
E_{\text{new}}
\xrightarrow{\text{update}}
\Psi_{t+1}.
\]

Here, \(H\) is the hypothesis, \(P(H)\) is the prediction, \(E_{\text{new}}\) is the experimental result, and \(\Psi_{t+1}\) is the updated state of the research program.

After each experiment, the target priority should be recalculated. A positive result may increase its ranking, a negative result may reduce it, and an ambiguous result may require additional testing.

***

## 9. GRA-чекпоинты / GRA Checkpoints

### Русский

GRA-чекпоинт — это сохранённое состояние анализа, которое позволяет восстановить не только итоговый рейтинг, но и ход рассуждения.

Он может содержать:

- идентификатор мишени;
- дату и версию анализа;
- использованные источники;
- положительные доказательства;
- отрицательные и противоречивые результаты;
- оценку механизма;
- риски;
- стоимость следующего эксперимента;
- критерии успеха и остановки;
- итоговый рейтинг;
- уровень уверенности;
- исходные допущения.

Такой формат делает решение проверяемым. Если появляется новая информация, исследователь может понять, какие данные изменились и почему изменился приоритет.

\[
\text{чекпоинт}
=
\text{данные}
+
\text{допущения}
+
\text{логика}
+
\text{рейтинг}
+
\text{следующий эксперимент}.
\]

### English

A GRA checkpoint is a saved state of the analysis. It preserves not only the final ranking but also the reasoning behind it.

A checkpoint may contain:

- target identifier;
- analysis date and version;
- data sources;
- supporting evidence;
- negative and contradictory findings;
- mechanism assessment;
- risks;
- cost of the next experiment;
- success and stopping criteria;
- final ranking;
- confidence level;
- original assumptions.

This makes the decision auditable. When new evidence appears, researchers can determine which inputs changed and why the target priority changed.

\[
\text{checkpoint}
=
\text{data}
+
\text{assumptions}
+
\text{reasoning}
+
\text{ranking}
+
\text{next experiment}.
\]

***

## 10. Ограничения / Limitations

### Русский

Главное ограничение состоит в том, что benchmark является синтетическим. В нём заранее заданы правила, согласно которым противоречия, hype, безопасность и стоимость влияют на истинную релевантность.

Поэтому GRA выиграла, поскольку использовала признаки, которые были информативными в созданной среде. Это не означает, что те же веса и правила будут оптимальными для любой реальной биомедицинской задачи.

В реальных исследованиях:

- противоречия могут отражать разные клеточные типы или условия эксперимента;
- дорогая проверка иногда оправдана высоким потенциальным выигрышем;
- риск может зависеть от дозировки и химической структуры;
- отрицательные результаты могут быть вызваны техническими причинами;
- слабая начальная доказательная база иногда предшествует важному открытию;
- литературное несогласие может указывать на контекстную зависимость механизма.

Поэтому текущий результат нельзя интерпретировать как доказательство превосходства GRA над фармацевтическими компаниями, биологами, химиками, клиницистами или существующими drug-discovery платформами.

### English

The main limitation is that the benchmark is synthetic. Its rules explicitly define contradictions, hype, safety, and validation cost as factors affecting true relevance.

GRA therefore performed well because it used features that were informative in the constructed environment. This does not mean that the same weights and rules will be optimal for every real biomedical problem.

In real research:

- contradictions may reflect different cell types or experimental conditions;
- an expensive validation step may be justified by high potential value;
- risk may depend on dosage and chemical structure;
- negative results may be caused by technical problems;
- weak early evidence may precede an important discovery;
- disagreement in the literature may indicate context-dependent biology.

The current result therefore cannot be interpreted as proof that GRA outperforms pharmaceutical companies, biologists, chemists, clinicians, or existing drug-discovery platforms.

***

## 11. Следующие этапы проверки / Next Evaluation Steps

### Русский

Для дальнейшей проверки GRA необходимо оценить не только средний результат, но и устойчивость архитектуры.

Полезны следующие эксперименты:

- изменить веса компонентов скоринга;
- поочерёдно отключить отдельные признаки;
- сравнить GRA со случайным выбором и более сильными моделями;
- изменить долю истинно релевантных мишеней;
- увеличить уровень шума;
- варьировать бюджет;
- изменить количество кандидатов;
- проверить разные типы публикационного bias;
- оценить калибровку уверенности;
- протестировать стратегию на исторических данных.

Особенно важен ablation study. Если убрать коррекцию hype, оценку риска или штраф за противоречия, а результат резко ухудшится, это позволит определить реальный вклад каждого компонента.

Также необходимо проверить, насколько хорошо GRA работает при изменении самого устройства синтетической среды. Если архитектура сохраняет преимущество только при одном наборе заранее заданных правил, её обобщающая способность будет ограниченной.

### English

Further evaluation should examine not only the mean performance but also the robustness of the architecture.

Useful experiments include:

- changing the scoring weights;
- removing individual features one at a time;
- comparing GRA with random selection and stronger models;
- varying the proportion of truly relevant targets;
- increasing the noise level;
- changing the experimental budget;
- changing the number of candidates;
- testing different forms of publication bias;
- evaluating confidence calibration;
- testing the strategy on historical data.

An ablation study is particularly important. If removing hype correction, risk assessment, or contradiction penalties causes a large performance decline, the contribution of each component can be measured.

The architecture should also be tested under different synthetic data-generating rules. If GRA performs well only under one predefined set of assumptions, its generalization capacity will be limited.

***

## 12. Практическое применение / Practical Application

### Русский

Потенциальный прикладной формат — **GRA Target Dossier**, то есть аналитическое досье по мишени или исследовательской программе.

Такой отчёт может содержать:

- описание мишени;
- карту доказательств;
- оценку независимости источников;
- экспериментальную и генетическую поддержку;
- анализ биологического механизма;
- противоречия;
- потенциальные риски;
- признаки hype;
- стоимость следующего эксперимента;
- критерии подтверждения;
- критерии остановки;
- нерешённые вопросы;
- объяснение итогового рейтинга.

Отчёт не должен обещать, что мишень станет лекарством. Его назначение — помочь принять более обоснованное решение перед дорогостоящим экспериментом.

Основная ценность GRA заключается в снижении неопределённости:

\[
\text{GRA-досье}
\rightarrow
\text{лучшее понимание гипотезы}
\rightarrow
\text{более информативный эксперимент}.
\]

### English

A potential applied format is the **GRA Target Dossier**, an analytical report on a target or research program.

The report could contain:

- a target overview;
- an evidence map;
- source-independence analysis;
- experimental and genetic support;
- biological-mechanism assessment;
- contradictions;
- potential risks;
- hype indicators;
- estimated cost of the next experiment;
- confirmation criteria;
- stopping criteria;
- unresolved questions;
- an explanation of the final ranking.

The report should not promise that the target will become a drug. Its purpose is to support a better decision before an expensive experiment is performed.

The main value of GRA is uncertainty reduction:

\[
\text{GRA dossier}
\rightarrow
\text{better understanding of the hypothesis}
\rightarrow
\text{more informative experiment}.
\]

***

## Заключение / Conclusion

### Русский

GRA-BioPharma продемонстрировала в синтетическом benchmark, что многокритериальная архитектура с учётом доказательств, механизма, противоречий, безопасности, стоимости и hype может существенно улучшить выбор мишеней.

При бюджете в 100 экспериментов GRA находила в среднем 10.13 релевантных мишеней против 2.64 у simple evidence и 0.12 у literature-only. Результат был устойчивым на 300 Monte Carlo-прогонах.

Наиболее корректный вывод таков:

> GRA не доказала, что уже умеет создавать лекарства. Она показала, что в заданной искусственной среде может эффективнее распределять ограниченный экспериментальный бюджет и находить больше перспективных мишеней.

Итоговая формула:

\[
\text{GRA}
=
\text{доказательства}
+
\text{согласованность механизма}
-
\text{противоречия}
-
\text{риски}
-
\text{hype}
-
\text{необоснованные расходы}.
\]

Практический результат:

\[
\text{тот же бюджет}
\rightarrow
\text{лучшее ранжирование}
\rightarrow
\text{меньше бесполезных экспериментов}
\rightarrow
\text{больше перспективных гипотез}.
\]

### English

In the synthetic benchmark, GRA-BioPharma demonstrated that a multi-factor architecture incorporating evidence, mechanism, contradictions, safety, cost, and hype can substantially improve target selection.

With a budget of 100 experiments, GRA identified an average of 10.13 relevant targets, compared with 2.64 for simple evidence and 0.12 for literature-only. The result remained consistent across 300 Monte Carlo runs.

The most accurate conclusion is:

> GRA did not demonstrate that it can already create medicines. It demonstrated that, in the specified synthetic environment, it can allocate a limited experimental budget more effectively and identify more promising targets.

The final formula is:

\[
\text{GRA}
=
\text{evidence}
+
\text{mechanistic coherence}
-
\text{contradictions}
-
\text{risks}
-
\text{hype}
-
\text{unjustified cost}.
\]

The practical outcome is:

\[
\text{same budget}
\rightarrow
\text{better prioritization}
\rightarrow
\text{fewer wasted experiments}
\rightarrow
\text{more promising hypotheses}.
\]

***

## Дисклеймер / Disclaimer

### Русский

GRA-BioPharma является концептуальной вычислительной архитектурой. Она не является лекарством, медицинским изделием, диагностическим методом или рекомендацией по лечению.

Любые выводы GRA требуют независимой лабораторной, доклинической и, при необходимости, клинической проверки. Исследования с участием людей должны проводиться в соответствии с законодательством, этическими нормами, требованиями информированного согласия и надзором компетентных органов.

### English

GRA-BioPharma is a conceptual computational architecture. It is not a drug, medical device, diagnostic method, or treatment recommendation.

All GRA outputs require independent laboratory, preclinical, and, where applicable, clinical validation. Research involving human participants must comply with applicable law, ethical standards, informed-consent requirements, and oversight by competent authorities.