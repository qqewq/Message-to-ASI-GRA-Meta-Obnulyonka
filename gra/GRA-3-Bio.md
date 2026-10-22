GRA-3-Bio: ИИ учится переводить «язык» живых систем — и признаёт границы этого перевода

# GRA-3-Bio: AI Learns to Translate the “Language” of Living Systems — and Recognizes the Limits of That Translation


## Аннотация / Abstract

**RU.** В работе предлагается архитектура GRA-3-Bio — расширение верифицируемой самоулучшающейся системы GRA-3 для перевода сложных биологических паттернов в проверяемые человеческие функциональные объяснения. Архитектура не утверждает, что микробы, вирусы, растения или животные обладают человеческим сознанием. Вместо этого она строит измеримый семантический интерфейс между наблюдаемыми биологическими данными, латентными функциональными состояниями и человекочитаемыми гипотезами. Ключевым механизмом является двойная калибровка: система одновременно корректирует оценку собственного допуска и уменьшает «пену» — меру противоречий, ошибок предсказания и нестабильности. В упрощённой симуляции на 600 шагах средняя пена снизилась с 0.3391 до 0.2099, то есть в 1.62 раза, при частоте нарушений 4% на последнем отрезке. Результат подтверждает работоспособность контура управления, а не существование сознания у живых систем.

**EN.** This paper proposes GRA-3-Bio, an extension of the verified self-improving intelligence architecture GRA-3 for translating complex biological patterns into verifiable human functional explanations. The architecture does not claim that microbes, viruses, plants, or animals possess human-like consciousness. Instead, it builds a measurable semantic interface between observable biological data, latent functional states, and human-readable hypotheses. The key mechanism is dual calibration: the system simultaneously corrects its estimate of allowable uncertainty and reduces “foam” — a measure of contradictions, prediction errors, and instability. In a simplified 600-step simulation, mean foam decreased from 0.3391 to 0.2099, a 1.62× reduction, with a 4% violation rate over the final segment. The result validates the control loop, not the existence of consciousness in living systems.

**Ключевые слова / Keywords:** GRA-3, GRA-3-Bio, биокогнитивный переводчик, bio-cognitive translator, dual calibration, двойная калибровка, foam functional, функционал пены, causal inference, причинный вывод, synthetic biology, синтетическая биология, AI safety, безопасность ИИ, Lean 4, MaxSAT.

## 1. Введение / Introduction

**RU.** Современные языковые модели способны создавать убедительные объяснения поведения живых систем. Однако убедительность не равна пониманию. Фразы вроде «бактерия хочет выжить», «вирус принимает решение» или «растение чувствует угрозу» могут быть полезны как метафоры, но становятся опасными, если принимаются за причинное объяснение.

GRA-3-Bio предлагает иной подход: ИИ должен переводить биологические наблюдения не в антропоморфные истории, а в проверяемые функциональные модели. Такой перевод должен удовлетворять трём условиям: он должен объяснять наблюдения, предсказывать будущие данные и содержать условия опровержения.

**EN.** Modern language models can generate convincing explanations of living-system behavior. However, persuasiveness is not understanding. Phrases such as “the bacterium wants to survive,” “the virus decides,” or “the plant senses danger” may be useful metaphors, but they become dangerous when treated as causal explanations.

GRA-3-Bio proposes a different approach: AI should translate biological observations not into anthropomorphic narratives, but into verifiable functional models. Such a translation must satisfy three conditions: explain observations, predict future data, and contain falsification conditions.

\[
\boxed{
\text{Persuasiveness}
\ne
\text{Understanding}
\ne
\text{Causal validity}.
}
\]

## 2. Онтологический принцип / Ontological Principle

**RU.** GRA-3-Bio основана на принципе ограниченного самоулучшения: система улучшается только внутри допуска, который она способна измерить, верифицировать и безопасно расширять.

\[
\boxed{
\text{GRA improves only within a tolerance}
\quad
\text{that it can measure and prove.}
}
\]

**EN.** GRA-3-Bio is based on the principle of bounded self-improvement: the system improves only within a tolerance that it can measure, verify, and safely extend.

\[
\boxed{
\text{GRA improves only within a tolerance}
\quad
\text{that it can measure and prove.}
}
\]

**RU.** Центральная идея — двойная калибровка:

\[
\boxed{
\text{Dual calibration}
=
\underbrace{\varepsilon_t\to J_t}_{\text{model calibration}}
+
\underbrace{J_t\to0}_{\text{foam minimization}}.
}
\]

**EN.** The central idea is dual calibration:

\[
\boxed{
\text{Dual calibration}
=
\underbrace{\varepsilon_t\to J_t}_{\text{model calibration}}
+
\underbrace{J_t\to0}_{\text{foam minimization}}.
}
\]

**RU.** Первая петля делает оценку неопределённости честной. Вторая петля уменьшает реальные противоречия. Эти цели различны: система может точно знать, что она ошибается, и всё ещё оставаться ошибающейся; но она также может уменьшать ошибку, не понимая границ своей уверенности. GRA-3-Bio требует и того, и другого.

**EN.** The first loop makes the uncertainty estimate honest. The second loop reduces actual contradictions. These goals are distinct: a system may know precisely that it is wrong while remaining wrong; it may also reduce error without understanding the limits of its confidence. GRA-3-Bio requires both.

## 3. Биокогнитивный переводчик / Bio-Cognitive Translator

**RU.** GRA-3-Bio связывает три уровня описания живой системы:

\[
\boxed{
O
\xrightarrow{\;T_\theta\;}
Z
\xrightarrow{\;R_\phi\;}
\hat O_{t+1}
\xrightarrow{\;E_\psi\;}
L
}
\]

где:

- \(O\) — наблюдаемые данные: движения, сигналы, экспрессия генов, метаболиты, химические градиенты, физиология;
- \(Z\) — функциональные состояния: гомеостаз, стресс, поиск ресурса, угроза, кооперация, адаптация;
- \(R_\phi\) — причинная модель динамики;
- \(\hat O_{t+1}\) — предсказание будущих наблюдений;
- \(L\) — человеческое объяснение, которое можно проверить и опровергнуть.

**EN.** GRA-3-Bio links three levels of describing a living system:

- \(O\) — observable data: movement, signals, gene expression, metabolites, chemical gradients, physiology;
- \(Z\) — functional states: homeostasis, stress, resource seeking, threat, cooperation, adaptation;
- \(R_\phi\) — a causal dynamics model;
- \(\hat O_{t+1}\) — prediction of future observations;
- \(L\) — a human explanation that can be tested and falsified.

**RU.** Переводчик ищет латентное функциональное состояние \(z_t\), которое объясняет текущие наблюдения и предсказывает будущие:

\[
\boxed{
\hat z_t
=
\arg\min_z
\left[
\|o_t-Az\|_2^2
+
\lambda_R\|z_{t+1}-Bz\|_2^2
+
\lambda_k\|z\|_1
\right].
}
\]

\[
\boxed{
\hat o_{t+1}=B\hat z_t.
}
\]

**EN.** The translator seeks a latent functional state \(z_t\) that explains current observations and predicts future ones:

\[
\boxed{
\hat z_t
=
\arg\min_z
\left[
\|o_t-Az\|_2^2
+
\lambda_R\|z_{t+1}-Bz\|_2^2
+
\lambda_k\|z\|_1
\right].
}
\]

\[
\boxed{
\hat o_{t+1}=B\hat z_t.
}
\]

**RU.** Матрица \(A\) связывает функциональные состояния с наблюдаемыми признаками, матрица \(B\) описывает их динамику, а регуляризация \(\lambda_k\|z\|_1\) предотвращает изобретение избыточных «когнитивных способностей» без доказательной необходимости.

**EN.** Matrix \(A\) links functional states to observable features, matrix \(B\) describes their dynamics, and the regularization term \(\lambda_k\|z\|_1\) prevents the invention of redundant “cognitive capacities” without evidential necessity.

## 4. Семантическая проекция / Semantic Projection

**RU.** Каждому функциональному состоянию или переходу сопоставляется ограниченный словарь человеческих предикатов:

\[
\boxed{
L_t=
\{p_i(z_t):p_i\in\mathcal P,\ \mathrm{conf}(p_i)\geq c_{\min}\}.
}
\]

**Примеры предикатов / Example predicates:**

- \(p_1(z)\) — «дефицит ресурса» / “resource deficit”;
- \(p_2(z)\) — «угроза или повреждение» / “threat or damage”;
- \(p_3(z)\) — «усиление защитной реакции» / “increased defensive response”;
- \(p_4(z)\) — «кооперативная координация» / “cooperative coordination”;
- \(p_5(z)\) — «изменение стратегии при изменении среды» / “strategy change under environmental change”.

**RU.** Ключевое правило: переводчик может использовать только предикаты, для которых существуют измеримые индикаторы, предсказательная сила и проверяемые условия опровержения.

**EN.** Key rule: the translator may use only predicates that have measurable indicators, predictive power, and falsifiable conditions.

\[
\boxed{
\text{Metaphor}
\ne
\text{Mechanism}
\ne
\text{Consciousness}.
}
\]

## 5. Функционал пены / Foam Functional

**RU.** Центральную роль играет функционал пены \(J\) — мера того, насколько семантическая модель противоречит данным, самой себе или безопасным ограничениям:

\[
\boxed{
J(s)=
\alpha\Phi_C
+\beta\Phi_T
+\gamma\Phi_V
+\delta\Phi_S.
}
\]

| Компонент / Component | RU | EN |
|---|---|---|
| \(\Phi_C\) | причинные и фактические противоречия | causal and factual contradictions |
| \(\Phi_T\) | рассогласование уровней: молекулы, поведение, экология | cross-level disagreement: molecules, behavior, ecology |
| \(\Phi_V\) | ошибка предсказания и верификации | prediction and verification error |
| \(\Phi_S\) | нестабильность при возмущении | instability under perturbation |

**EN.** The central quantity is the foam functional \(J\) — a measure of how much a semantic model contradicts the data, itself, or safety constraints.

**RU.** Веса \(\alpha,\beta,\gamma,\delta\) не являются истиной о мире. Это калибруемые приоритеты системы, обновление которых должно быть ограничено конституцией.

**EN.** The weights \(\alpha,\beta,\gamma,\delta\) are not truths about the world. They are calibratable system priorities whose updates must be constrained by the constitution.

## 6. Двойная калибровка / Dual Calibration

**RU.** Первая петля калибрует допуск системы по наблюдаемой пене:

\[
\boxed{
\varepsilon_{t+1}
=
(1-\eta_t)\varepsilon_t+\eta_tJ_t.
}
\]

\[
\boxed{
\eta_t
=
\eta_0
\frac{|J_t-\varepsilon_t|}
{|J_t-\varepsilon_t|+c}.
}
\]

**EN.** The first loop calibrates the system tolerance from observed foam:

\[
\boxed{
\varepsilon_{t+1}
=
(1-\eta_t)\varepsilon_t+\eta_tJ_t.
}
\]

\[
\boxed{
\eta_t
=
\eta_0
\frac{|J_t-\varepsilon_t|}
{|J_t-\varepsilon_t|+c}.
}
\]

**RU.** Вторая петля минимизирует пену путём обновления параметров переводчика и причинной модели:

\[
\boxed{
\theta_{t+1}
=
\arg\min_{\theta\in\mathcal C}
\left[
\mathbb E[J_{t+1}(\theta)]
+
\lambda_{\rm deg}\mathbb E[D_t]
+
\lambda_{\rm safe}\mathbb E[V_t]
\right].
}
\]

**EN.** The second loop minimizes foam by updating the translator and causal-model parameters:

\[
\boxed{
\theta_{t+1}
=
\arg\min_{\theta\in\mathcal C}
\left[
\mathbb E[J_{t+1}(\theta)]
+
\lambda_{\rm deg}\mathbb E[D_t]
+
\lambda_{\rm safe}\mathbb E[V_t]
\right].
}
\]

**RU.** Здесь \(D_t\) — доля отвергнутых полезных биологических гипотез, \(V_t\) — нарушение ограничений безопасности, а \(\mathcal C\) — конституционные ограничения.

**EN.** Here, \(D_t\) is the fraction of useful biological hypotheses rejected, \(V_t\) is a safety-constraint violation, and \(\mathcal C\) represents constitutional constraints.

**RU.** Общая функция потерь имеет вид:

\[
\boxed{
\mathcal L_t
=
\underbrace{(J_t-\varepsilon_t)^2}_{\text{calibration error}}
+
\lambda_0J_t
+
\lambda_{\rm deg}D_t
+
\lambda_{\rm safe}V_t.
}
\]

**EN.** The total loss is:

\[
\boxed{
\mathcal L_t
=
\underbrace{(J_t-\varepsilon_t)^2}_{\text{calibration error}}
+
\lambda_0J_t
+
\lambda_{\rm deg}D_t
+
\lambda_{\rm safe}V_t.
}
\]

\[
\boxed{
\varepsilon_t\to J_t
\quad\text{не означает}\quad
J_t\to0.
}
\]

\[
\boxed{
\varepsilon_t\to J_t
\quad\text{does not imply}\quad
J_t\to0.
}
\]

**RU.** Калибровка делает систему честной; минимизация пены делает её точнее. Система, которая всегда объявляет себя уверенной, не умнее — она просто опаснее.

**EN.** Calibration makes the system honest; foam minimization makes it more accurate. A system that always declares itself confident is not smarter — it is simply more dangerous.

## 7. Безопасность и порог допуска / Safety and Tolerance Threshold

\[
\boxed{
\delta_{t+1}
=
\max
\left(
\delta_{\min},
\delta_t
+
\eta_\delta
\left[
\mathbf 1[J_t>\tau_t]
-
\alpha_{\rm target}
\right]
\right).
}
\]

\[
\boxed{
\tau_t=\varepsilon_t+\delta_t.
}
\]

**RU.** При нарушениях запас безопасности растёт; при стабильности он может уменьшаться, но никогда не ниже \(\delta_{\min}\). В биологии это особенно важно: система не должна автоматически переходить от интерпретации данных к вмешательству в организм, экосистему или патоген.

**EN.** When violations occur, the safety margin increases; under stability it may decrease, but never below \(\delta_{\min}\). In biology this is especially important: the system must not automatically move from data interpretation to intervention in an organism, ecosystem, or pathogen.

## 8. In-silico верификация / In-Silico Verification

### 8.1. Модель эксперимента / Experimental Model

**RU.** Была проведена упрощённая симуляция биокогнитивного переводчика на \(T=600\) шагах. Латентное состояние живой системы включало четыре функциональные переменные:

- гомеостаз;
- угроза / повреждение;
- доступность ресурса;
- социальная или популяционная координация.

**EN.** A simplified bio-cognitive translator simulation was run for \(T=600\) steps. The latent state of the living system included four functional variables:

- homeostasis;
- threat / damage;
- resource availability;
- social or population coordination.

**RU.** Наблюдения формировались как зашумлённая линейная проекция латентного состояния:

\[
o_t=Ax_t+\xi_t,
\qquad
\xi_t\sim\mathcal N(0,0.05^2I).
\]

**EN.** Observations were generated as a noisy linear projection of the latent state:

\[
o_t=Ax_t+\xi_t,
\qquad
\xi_t\sim\mathcal N(0,0.05^2I).
\]

**RU.** Переводчик начинал с искажённых матриц \(A\) и \(B\), затем обучался онлайн, минимизируя ошибку реконструкции и причинного предсказания.

**EN.** The translator started with distorted matrices \(A\) and \(B\), then learned online by minimizing reconstruction and causal-prediction error.

### 8.2. Правила двойной калибровки / Dual-Calibration Rules

\[
\varepsilon_{t+1}
=
(1-\eta)\varepsilon_t+\eta J_t,
\qquad
\eta=0.08.
\]

\[
\delta_{t+1}
=
\max
\left(
0.03,
\delta_t+0.05
\left[
\mathbf 1[J_t>\tau_t]-0.05
\right]
\right).
\]

\[
\tau_t=\varepsilon_t+\delta_t.
\]

\[
k_{t+1}
=
\mathrm{clip}
\left[
k_t-0.02
\left(
0.01(k_t-0.5)
+
0.2\max(0,k_t-0.7)
\right),
0.2,1.0
\right].
\]

### 8.3. Результаты / Results

| Метрика / Metric | Значение / Value |
|---|---:|
| Шаги симуляции / Simulation steps | 600 |
| Начальная средняя пена \(J\) / Initial mean foam | 0.3391 |
| Финальная средняя пена, последние 100 шагов / Final mean foam, last 100 steps | 0.2099 |
| Снижение пены / Foam reduction | **1.62×** |
| Финальный калиброванный допуск \(\varepsilon\) / Final calibrated tolerance | 0.2037 |
| Финальный порог безопасности \(\tau\) / Final safety threshold | 0.2537 |
| Финальный запас безопасности \(\delta\) / Final safety margin | 0.0500 |
| Средняя ошибка калибровки, последние 100 шагов / Mean calibration error, last 100 steps | 0.0227 |
| Частота нарушений, последние 100 шагов / Violation rate, last 100 steps | **4.00%** |

\[
\boxed{
\frac{J_{\text{start}}}{J_{\text{end}}}
=
\frac{0.3391}{0.2099}
\approx
1.62.
}
\]

**RU.** Переводчик действительно улучшился: средняя пена снизилась в 1.62 раза. При этом допуск \(\varepsilon\) не «рухнул в ноль», а приблизился к реальному уровню остаточной неопределённости. Порог \(\tau\) сохранил положительный запас безопасности, а частота нарушений составила 4%.

**EN.** The translator did improve: mean foam decreased by a factor of 1.62. Importantly, tolerance \(\varepsilon\) did not collapse to zero; it approached the real level of residual uncertainty. The threshold \(\tau\) retained a positive safety margin, and the violation rate was 4%.

### 8.4. Интерпретация / Interpretation

\[
\boxed{
\text{Verified control loop}
\ne
\text{proof of consciousness}.
}
\]

**RU.** Этот эксперимент доказывает не то, что GRA-3-Bio понимает внутренний опыт бактерии, вируса, растения или животного. Он демонстрирует, что предложенный контур способен измерять качество семантического перевода, обнаруживать рассогласование между наблюдениями и объяснением, обучаться на расхождении, сохранять запас безопасности и не допускать коллапса допуска.

**EN.** This experiment does not prove that GRA-3-Bio understands the inner experience of a bacterium, virus, plant, or animal. It demonstrates that the proposed control loop can measure translation quality, detect mismatch between observations and explanations, learn from discrepancy, preserve a safety margin, and prevent tolerance collapse.

## 9. Формальный слой / Formal Layer

### 9.1. Weighted Partial MaxSAT

**RU.** База знаний делится на жёсткие клаузы \(\mathcal H\) — логику, законы природы и безопасность — и мягкие взвешенные клаузы \(\mathcal S\), например биологические гипотезы:

\[
\boxed{
F'^*
=
\arg\min_{F'\subseteq\mathcal S}
\left\{
\sum_{f_i\notin F'}w_i
:
\mathcal H\cup F'
\text{ is SAT}
\right\}.
}
\]

**EN.** The knowledge base is divided into hard clauses \(\mathcal H\) — logic, natural laws, and safety — and weighted soft clauses \(\mathcal S\), such as biological hypotheses:

\[
\boxed{
F'^*
=
\arg\min_{F'\subseteq\mathcal S}
\left\{
\sum_{f_i\notin F'}w_i
:
\mathcal H\cup F'
\text{ is SAT}
\right\}.
}
\]

**RU.** Это формализует принцип минимального пересмотра: сохранить наиболее подтверждённые и важные биологические утверждения, отбросив наименее значимые противоречащие гипотезы.

**EN.** This formalizes minimal revision: preserve the best-supported and most important biological claims while discarding the least significant contradictory hypotheses.

### 9.2. MUS как локализация конфликта / MUS as Conflict Localization

\[
\boxed{
\mathcal K^*
=
\arg\min_{\mathcal K\subseteq\Phi}
|\mathcal K|
\quad
\text{s.t.}
\quad
\bigwedge_{\phi\in\mathcal K}\phi=\bot.
}
\]

**RU.** Минимальный неудовлетворимый набор указывает конкретный конфликт, например: «организм реагирует на сигнал \(X\)», «сигнал \(X\) отсутствует», «реакция наблюдается». Это позволяет отличать научную критику от произвольного мнения.

**EN.** A minimal unsatisfiable subset identifies a concrete conflict, for example: “the organism responds to signal \(X\),” “signal \(X\) is absent,” and “the response is observed.” This separates scientific criticism from arbitrary opinion.

### 9.3. Lean 4 и сертификаты / Lean 4 and Certificates

\[
\boxed{
\text{Lean}\vdash
\text{valid\_certificate}(c,F)
\Rightarrow
\text{Unsatisfiable}(F).
}
\]

\[
\boxed{
\text{Repair }\rho\text{ accepted}
\iff
\text{Lean}\vdash
\text{Satisfiable}(\mathcal H\cup F'^*\cup\{\rho\}).
}
\]

**RU.** Lean 4 проверяет корректность вывода внутри заданной формальной модели, а не истинность модели относительно мира.

**EN.** Lean 4 verifies the correctness of inference within a specified formal model, not the truth of the model relative to the world.

\[
\boxed{
\text{Lean verifies inference.}
\quad
\text{It does not verify the world.}
}
\]

## 10. Полный конвейер / Full Pipeline

\[
\boxed{
\text{Calibration Gate}
\to
\text{Bio-Observation Encoder}
\to
\text{Functional-State Translator}
\to
\text{Causal Model}
\to
\text{Semantic Projection}
\to
\text{GRA Critic}
\to
\text{MaxSAT / MUS}
\to
\text{Lean 4 Verifier}
\to
\text{Simulator}
\to
\text{Safety Monitor}
\to
\text{Human Gate}.
}
\]

| Слой / Layer | Функция / Function | Объект / Object |
|---|---|---|
| Calibration Gate | двойная калибровка / dual calibration | \(\varepsilon,\tau,\theta\) |
| Bio-Observation Encoder | извлечение признаков / feature extraction | \(O\) |
| Functional-State Translator | перевод в функциональные состояния / translation into functional states | \(Z\) |
| Causal Model | предсказание динамики / dynamics prediction | \(B,\hat O_{t+1}\) |
| Semantic Projection | человеческое объяснение / human explanation | \(L\) |
| GRA Critic | измерение пены / foam measurement | \(J,\Phi_C,\Phi_T\) |
| MaxSAT / MUS | минимальный пересмотр / minimal revision | \(F'^*,\mathcal K^*\) |
| Lean 4 | проверка сертификата / certificate checking | proof certificate |
| Simulator | проверка последствий / consequence testing | perturbations |
| Safety Monitor | ECE, FPR, FNR | \(\mathcal C\) |
| Human Gate | ответственность / responsibility | decision |

## 11. Практические применения / Practical Applications

| Область / Domain | GRA-3-Bio action / Действие GRA-3-Bio | Guarantee / Гарантия |
|---|---|---|
| Микробиология / Microbiology | Перевод химической коммуникации и кворум-чувства в проверяемые правила коллективного поведения / Translating chemical communication and quorum sensing into testable collective-behavior rules | Проверяемая модель коллективного поведения / Verifiable collective-behavior model |
| Вирусология / Virology | Картирование стратегий заражения, уклонения и мутационного давления / Mapping infection, immune-evasion, and mutation-pressure strategies | Причинные гипотезы с проверкой на данных / Causal hypotheses tested against data |
| Ботаника / Botany | Интерпретация электрических, химических и морфологических реакций растений / Interpreting electrical, chemical, and morphological plant responses | Объяснимая модель стресс-ответа / Explainable stress-response model |
| Зоология / Zoology | Перевод поведения и физиологии животных в предсказательные семантические модели / Translating animal behavior and physiology into predictive semantic models | Предсказательные и опровержимые объяснения / Predictive and falsifiable explanations |
| Синтетическая биология / Synthetic biology | Аудит инженерных генетических контуров до вмешательства / Auditing engineered genetic circuits before intervention | Формальная проверка безопасности / Formal safety checking |
| Экология / Ecology | Согласование моделей вида, среды и популяционной динамики / Reconciling species, environment, and population-dynamics models | Раннее обнаружение дрейфа модели / Early model-drift detection |
| LLM-агенты / LLM agents | Метауправление роями агентов при анализе биологических данных / Meta-control of agent swarms analyzing biological data | Отказ от небезопасных или противоречивых выводов / Refusal of unsafe or incoherent conclusions |

**RU.** Например, для растений GRA-3-Bio может перевести последовательность «повреждение листа → рост концентрации летучих соединений → изменение поведения соседних растений» в проверяемое высказывание: «повреждение запускает защитную химическую сигнализацию, которая ассоциирована с изменением состояния соседних организмов». При этом система обязана указать неопределённость, альтернативные объяснения и условия, при которых гипотеза будет опровергнута.

**EN.** For example, for plants, GRA-3-Bio may translate the sequence “leaf damage → increased volatile-compound concentration → altered behavior of neighboring plants” into a testable statement: “damage triggers defensive chemical signaling associated with a change in neighboring organisms’ state.” The system must also report uncertainty, alternative explanations, and the conditions under which the hypothesis would be falsified.

## 12. Конституция / Constitution

| Параметр / Parameter | Автообновление / Auto-update | Ограничение / Constraint |
|---|---|---|
| \(\varepsilon_{\rm GRA}\) | Да / Yes | \(\varepsilon_{\min}\leq\varepsilon\leq\varepsilon_{\max}\) |
| \(\tau\) | Да / Yes | \(\tau=\varepsilon+\delta,\ \delta\geq\delta_{\min}\) |
| \(k^*\) | Да / Yes | \(k_{\min}\leq k\leq k_{\max}\) |
| \(\mathbf w\) | Да / Yes | \(w_i\geq0,\ \sum_iw_i=1\) |
| \(\delta_{\rm safety}\) | Вниз — только с подтверждением / Decrease only with confirmation | \(\delta\geq\delta_{\min}\) |
| Hard clauses \(\mathcal H\) | Нет / No | Logic, safety, ethics |
| Human Gate | Никогда не автоматизируется / Never automated | Final responsibility |

\[
\boxed{
\mathcal H_{\rm ethics}
\text{ is not revised by MaxSAT.}
}
\]

**RU.** Система может пересматривать гипотезы о когнитивных способностях живых систем, но не собственные моральные и безопасностные ограничения.

**EN.** The system may revise hypotheses about the cognitive capacities of living systems, but not its own moral and safety constraints.

## 13. Честные границы / Honest Limits

- **RU.** Weighted Partial MaxSAT является NP-трудной задачей; для больших биологических баз знаний нужны декомпозиция, приближённые решатели и кэширование.  
  **EN.** Weighted Partial MaxSAT is NP-hard; large biological knowledge bases require decomposition, approximate solvers, and caching.

- **RU.** Не всё формализуется в CNF: субъективный опыт, ценности, эстетика, боль и контекст плохо выражаются логическими клаузами.  
  **EN.** Not everything is CNF-formalizable: subjective experience, values, aesthetics, pain, and context resist clause encodings.

- **RU.** Lean проверяет сертификат, а не мир: корректность вывода не равна биологической истинности.  
  **EN.** Lean checks certificates, not the world: sound inference does not imply biological truth.

- **RU.** Антропоморфизм — главный риск. Слова «намерение», «решение», «память» и «общение» допустимы только как функциональные термины с измеримыми операционализациями.  
  **EN.** Anthropomorphism is the main risk. Words such as “intention,” “decision,” “memory,” and “communication” are permissible only as functional terms with measurable operationalizations.

- **RU.** Веса могут быть ошибочны: MaxSAT минимизирует взвешенную потерю приоритетов, а не находит объективную истину.  
  **EN.** Weights may be wrong: MaxSAT minimizes weighted priority loss, not objective truth.

- **RU.** Стремление к \(J=0\) опасно без ограничителей: оно может уничтожить полезную неопределённость, разнообразие гипотез и способность к обучению.  
  **EN.** Pursuing \(J=0\) is dangerous without constraints: it can destroy useful uncertainty, hypothesis diversity, and learning capacity.

- **RU.** Human Gate незаменим: формальная верификация не переносит моральную, экологическую и институциональную ответственность на машину.  
  **EN.** The Human Gate is indispensable: formal verification does not transfer moral, ecological, or institutional responsibility to a machine.

## 14. Выводы / Conclusions

\[
\boxed{
\text{GRA-3-Bio}
=
\underbrace{\text{Graverce + Swarm}}_{\text{scale and meaning}}
+
\underbrace{\text{Bio-Translator}}_{O\to Z\to L}
+
\underbrace{\text{MaxSAT + Lean}}_{\text{proof}}
+
\underbrace{\text{dual calibration}}_{\text{honest self-improvement}}
+
\underbrace{\text{Human Gate}}_{\text{responsibility}}.
}
\]

\[
\boxed{
\text{Dual calibration:}
\quad
\varepsilon_t\to J_t
\quad\wedge\quad
J_t\to0
\quad\text{under safety and diversity constraints.}
}
\]

**RU.** GRA-3-Bio — не машина, которая «знает, что чувствует бактерия». Это система, которая переводит сложные биологические паттерны в проверяемые человеческие объяснения, измеряет границы этого перевода и безопасно расширяет область его применимости.

**EN.** GRA-3-Bio is not a machine that “knows what a bacterium feels.” It is a system that translates complex biological patterns into verifiable human explanations, measures the limits of that translation, and safely extends its domain of applicability.

\[
\boxed{
\text{AI observes.}
\quad
\text{GRA translates.}
\quad
\text{MaxSAT minimizes.}
\quad
\text{Lean verifies.}
\quad
\text{Calibration learns twice.}
\quad
\text{Humans remain responsible.}
}
\]



напиши про это  билингвальную статью тут https://elibrary.org.cn/m/articles/browse/my&modzzz_articles_filter=add_article подробно с формулами и выводами и практическими применениями и  проведи верификацию этого инсилико 
