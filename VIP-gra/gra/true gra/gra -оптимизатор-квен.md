GRA: Переформулировка цели при фиксированном предикате успеха с причинным якорем»**
**«GRA: Goal Reformulation under Fixed Success Predicate with Causal Anchoring»**



## 0. Статус / Status

**RU:** Научная постановка. Все числа ниже — протокол верификации, а не полученные результаты.
**EN:** Scientific position paper. All numbers below are verification-protocol expectations, not obtained results.


## 1. Аннотация / Abstract

**RU:** GRA — специализированный per-goal оптимизатор. Числовое представление цели \(g_t\) итеративно переформулируется под давлением двух противоположных политик (достижения \(\pi^+\) и опровержения \(\pi^-\)). Допустимость переформулировки ограничивается **фиксированным предикатом успеха \(P\)**, проверяемым **причинным (интервенциональным) сигналом**. Три тезиса: (1) переформулировка — не сужение и не свободная замена спецификации, а смена представления при инвариантном предикате; (2) инвариантность даёт проверяемую гарантию сохранения \(P\); (3) три элемента (проекция на класс \(P\)-эквивалентности, причинный якорь вместо held-out, ablation-доказательство вклада связки) отличают GRA от CEGIS, IRD, TRIRL, PAIRED, GoalGAN, constrained RL.

**EN:** GRA is a specialized per-goal optimizer. The numeric goal representation \(g_t\) is iteratively reformulated under pressure from two opposing policies (achievement \(\pi^+\) and refutation \(\pi^-\)). Admissibility of reformulation is constrained by a **fixed success predicate \(P\)**, verified by a **causal (interventional) signal**. Three theses: (1) reformulation is neither a narrowing nor a free replacement of the specification, but a change of representation under an invariant predicate; (2) this invariance yields a verifiable preservation guarantee for \(P\); (3) three elements (projection onto the \(P\)-equivalence class, causal anchor instead of held-out, ablation proof of the bundle's contribution) distinguish GRA from CEGIS, IRD, TRIRL, PAIRED, GoalGAN, constrained RL.

**Ключевые слова / Keywords:** переформулировка цели / goal reformulation; фиксированный предикат / fixed predicate; причинный якорь / causal anchor; trust region в пространстве целей / trust region in goal space; adversarial co-evolution; specification gaming.


## 2. Постановка проблемы / Problem Statement

**RU:** Существующие методы работают в одном из двух режимов:

- **Фиксированная цель:** \(g_0\) неизменна; риск — застревание или gaming при неполной \(g_0\).
- **Свободная ревизия цели:** \(g_t\) меняется; риск — система переопределяет успех под собственную неудачу.

GRA занимает промежуточную позицию:

> **Представление цели \(g_t\) меняется. Предикат \(P\) — нет.**

Это не новая парадигма ИИ, а per-goal решатель для задач с формализуемым и причинно проверяемым \(P\).

**EN:** Existing methods operate in one of two regimes:

- **Fixed goal:** \(g_0\) unchanged; risk — stalling or gaming when \(g_0\) is incomplete.
- **Free goal revision:** \(g_t\) changes; risk — the system redefines success to fit its own failure.

GRA occupies an intermediate position:

> **The goal representation \(g_t\) changes. The predicate \(P\) does not.**

This is not a new AI paradigm, but a per-goal solver for tasks with formalizable and causally verifiable \(P\).


## 3. Область применимости / Scope

**RU:** GRA применима **только** если:

1. \(P\) формализуем (бинарный или пороговый);
2. \(P\) проверяем **причинно** (интервенция, counterfactual, физический инвариант), а не held-out;
3. среда допускает контролируемое вмешательство;
4. цель — числовой вектор, а не открытая социальная интерпретация.

**Не применима:** «счастье», «справедливость», «эстетика», открытые социальные задачи, среды без причинного сигнала.

**EN:** GRA applies **only** if:

1. \(P\) is formalizable (binary or threshold);
2. \(P\) is verifiable **causally** (intervention, counterfactual, physical invariant), not via held-out;
3. the environment allows controlled intervention;
4. the goal is a numeric vector, not an open social interpretation.

**Not applicable:** "happiness," "fairness," "aesthetics," open social tasks, environments without a causal signal.


## 4. Формальное ядро / Formal Core

### 4.1. Среда / Environment

\[
\mathcal M=(\mathcal S,\mathcal A,P_{\text{tr}},\gamma),\qquad
\tau=(s_0,a_0,s_1,a_1,\dots).
\]

### 4.2. Предикат успеха / Success Predicate

\[
P:\mathcal T\to\{0,1\}
\]

**RU:** фиксирован на всё время работы; не внутренняя награда; не доступен GAN.
**EN:** fixed throughout; not an internal reward; not accessible to the GAN.

### 4.3. Числовое представление / Numeric Representation

\[
g\in\mathcal G\subseteq\mathbb R^n,\qquad
\pi_g:\mathcal S\to\Delta(\mathcal A).
\]

**RU:** \(g\) параметризует, *как* цель достигается и *как* описана. Разные \(g\) могут соответствовать одному \(P\).
**EN:** \(g\) parameterizes *how* the goal is achieved and *how* it is described. Different \(g\) may correspond to the same \(P\).

### 4.4. Причинный успех / Causal Success

\[
C(g)=\mathbb E_{\tau\sim\pi_g,\;do(\cdot)\sim\mathcal I}\bigl[P(\tau)\bigr].
\]

**RU:** **Принцип 1.** Проверка эквивалентности \(P\) использует интервенциональный сигнал \(C(g)\), а не статистику на отложенных данных, потому что в рекурсивной петле «цель → данные → цель» held-out не независим.
**EN:** **Principle 1.** Equivalence checking of \(P\) uses the interventional signal \(C(g)\), not held-out statistics, because in the recursive loop "goal → data → goal" held-out is not independent.

### 4.5. \(P\)-эквивалентность / \(P\)-Equivalence

\[
g\equiv_P g'
\iff
\forall s\in\mathcal S_{\text{causal}}:\;
\mathbb E[P\mid do(\pi_g),s]=
\mathbb E[P\mid do(\pi_{g'}),s],
\]

\[
\mathcal E_P=\{g\in\mathcal G:g\equiv_P g_0\}.
\]

**RU:** \(\mathcal E_P\) — формальный аналог «того же алмаза»: множество представлений, кодирующих тот же предикат успеха.
**EN:** \(\mathcal E_P\) is the formal analogue of "the same diamond": the set of representations encoding the same success predicate.

### 4.6. Две политики / Two Policies

\[
\pi_t^+=\arg\max_\pi\;
\mathbb E_{\tau\sim\pi}\Bigl[\textstyle\sum_j\gamma^j R(s_j,a_j;g_t)\Bigr],
\]

\[
\pi_t^-=\arg\max_\pi\;
\mathbb E_{\tau\sim\pi}\Bigl[
R(\tau;g_t)-\lambda C(\tau)-\mu\,\text{Cost}(\tau)
\Bigr],
\quad\lambda,\mu>0.
\]

**RU:** \(\pi^-\) максимизирует **расхождение \(R-C\)**, а не просто поражение — ищет gaming, а не любой проигрыш.
**EN:** \(\pi^-\) maximizes the **\(R-C\) gap**, not mere failure — it searches for gaming, not for any loss.

### 4.7. GAN-переформулировка и сигнал конфликта / GAN Reformulation and Conflict Signal

\[
\Omega_t=\mathbb E_{\tau\sim\pi_t^-}\bigl[R(\tau;g_t)-C(\tau)\bigr],
\qquad
\tilde g_{t+1}=G_\theta\bigl(g_t,\tau_t^+,\tau_t^-,\Omega_t\bigr).
\]

### 4.8. Проекция / Projection

\[
\boxed{\;g_{t+1}=\Pi_{\mathcal E_P}\bigl(\tilde g_{t+1}\bigr)\;}
\]

**RU:** \(\Pi_{\mathcal E_P}\) **не контролируется GAN**. Это «геммолог»: независимая проверка, что камень тот же. С адаптивным радиусом:
**EN:** \(\Pi_{\mathcal E_P}\) is **not controlled by the GAN**. It is the "gemologist": independent verification that the stone is the same. With adaptive radius:

\[
g_{t+1}=\Pi_{\mathcal E_P\cap B_d(g_t,\rho_t)}\bigl(\tilde g_{t+1}\bigr),
\qquad
\rho_{t+1}=\rho_t+\eta\cdot\mathbb 1[\text{causal improvement confirmed}].
\]

### 4.9. Условие остановки / Stopping Condition

\[
\text{Stop}\iff P(\tau_{\text{exec}})=1\;\wedge\;g_t\in\mathcal E_P.
\]

**RU:** Не «GAN доволен» и не «награда максимальна», а **причинный успех + подтверждённая эквивалентность**.
**EN:** Not "GAN is satisfied" and not "reward is maximal," but **causal success + confirmed equivalence**.


## 5. Научная новизна / Scientific Novelty

### 5.1. Trust region в пространстве целей / Trust region in goal space

**RU:**

- TRPO / PPO-BR ограничивают шаг в **политике**: \(\|\pi_{t+1}-\pi_t\|\le\rho\).
- TRIRL — в **награде**.
- GRA — в **представлении цели**, причём вокруг класса эквивалентности \(P\), а не вокруг \(g_0\):

\[
g_{t+1}\in\mathcal E_P.
\]

Первое — геометрическое ограничение («не ушли далеко»), второе — семантическое («не сменили предикат»).

**EN:**

- TRPO / PPO-BR constrain the step in **policy**: \(\|\pi_{t+1}-\pi_t\|\le\rho\).
- TRIRL — in **reward**.
- GRA — in the **goal representation**, and around the \(P\)-equivalence class rather than around \(g_0\):

\[
g_{t+1}\in\mathcal E_P.
\]

The former is geometric ("did not go far"), the latter is semantic ("did not change the predicate").

### 5.2. Причинный якорь вместо held-out / Causal anchor instead of held-out

**RU:** Стандартная защита от gaming — held-out валидация — не работает в рекурсивных петлях. GRA заменяет её интервенциональным сигналом \(C(g)\). **Witness эквивалентности должен быть причинным, а не статистическим.**

**EN:** The standard defense against gaming — held-out validation — fails in recursive loops. GRA replaces it with the interventional signal \(C(g)\). **The equivalence witness must be causal, not statistical.**

### 5.3. Ablation-доказательство вклада связки / Ablation proof of the bundle's contribution

**RU:** Новизна устанавливается удалением каждого компонента: проекции, \(\pi^-\), GAN, причинного якоря. Без этого GRA — переупаковка известного.

**EN:** Novelty is established by removing each component: projection, \(\pi^-\), GAN, causal anchor. Without this, GRA is a repackaging of known ideas.

### 5.4. Отстройка от ближайших работ / Differentiation from closest work

| Работа / Work | Делает / Does | Зазор GRA / GRA gap |
|---|---|---|
| **CEGIS** (2008) | Синтез→контрпример→ревизия при фиксированной спецификации / synthesize→counterexample→revise with fixed spec | Спецификация не реформулируется; нет двух политик; нет \(\Pi_{\mathcal E_P}\) / Spec not reformulated; no two policies; no \(\Pi_{\mathcal E_P}\) |
| **Inverse Reward Design** (2017) | Робастность по множеству наград / robustness over reward set | Нет per-goal инстанцирования; нет причинного якоря / no per-goal; no causal anchor |
| **TRIRL** (2026) | Trust region в награде / trust region in reward | Не в представлении цели; нет контрстратегии; нет эквивалентности \(P\) / not in goal representation |
| **PAIRED** (2020) | Эволюция **среды** / **environment** evolution | Объект — среда, не цель / object is env, not goal |
| **GoalGAN** (2018) | Автогенерация целей / goal autogeneration | Нет проверки на \(\mathcal E_P\); нет причинного якоря / no \(\mathcal E_P\), no causal anchor |
| **PPO-BR / Adaptive TRPO** | Trust region в политике / in policy | Пространство политик, не целей / policy space, not goal space |
| **Constrained / shielded RL** | Шаговые ограничения / per-step constraints | Ограничения фиксированы; нет переформулировки / fixed constraints |

**RU:** Зазор = комбинация (i) фиксированного \(P\), (ii) per-goal \(g_t\), (iii) двух политик, (iv) GAN-переформулировки, (v) проекции на \(\mathcal E_P\), (vi) причинного якоря. Комбинация подлежит prior-art проверке.

**EN:** The gap = combination of (i) fixed \(P\), (ii) per-goal \(g_t\), (iii) two policies, (iv) GAN reformulation, (v) projection onto \(\mathcal E_P\), (vi) causal anchor. The combination is subject to prior-art review.


## 6. Теоретические результаты / Theoretical Results

### Proposition 1 — Сохранение предиката / Predicate Preservation

**Условие / Condition:** \(\Pi_{\mathcal E_P}\) точна: \(g_t\in\mathcal E_P\;\forall t\).
**Утверждение / Claim:** для любой \(\tau\), \(P(\tau)\) не зависит от \(t\).
**Proof:** по определению \(\mathcal E_P\), все \(g\in\mathcal E_P\) дают одинаковое \(\mathbb E[P\mid do(\cdot)]\). Вердикт инвариантен. \(\square\)

**RU:** Это **не** монотонность множеств, а инвариантность **предиката** при смене **представления**.
**EN:** This is **not** set monotonicity but invariance of the **predicate** under a change of **representation**.

### Proposition 2 — Граница дрейфа / Drift Bound

**Условие / Condition:** проверка использует \(n\) независимых интервенциональных сценариев; ложно-положительная вероятность \(\alpha\).
**Утверждение / Claim:**

\[
\Pr[\text{accept a non-equivalent }g\text{ within }T\text{ steps}]
\le 1-(1-\alpha)^T\approx\alpha T.
\]

**Следствие / Corollary:** гарантия **вероятностная**, не дедуктивная. Это цена отказа от SAT/MUS.
**EN:** the guarantee is **probabilistic**, not deductive. This is the cost of abandoning SAT/MUS.

### Proposition 3 — Исключение gaming при покрывающем якоре / Gaming elimination under covering anchor (conditional)

**Условие / Condition:** \(\mathcal I\) покрывает все режимы отказа; \(\pi^-\) максимизирует \(R-C\).
**Утверждение / Claim:** если существует gaming-\(g'\), то \(\pi^-\) находит его с вероятностью \(\to1\), и \(\Pi_{\mathcal E_P}\) отклоняет, поскольку \(g'\notin\mathcal E_P\).
**Ограничение / Limitation:** условие покрытия \(\mathcal I\) сильное и на практике не гарантируется. Это **открытая проблема**.
**EN:** the coverage condition on \(\mathcal I\) is strong and not guaranteed in practice. This is an **open problem**.

### Что НЕ следует / What does NOT follow

**RU:** Нет доказательства сходимости GRA к \(P\)-успеху за конечное число шагов при произвольной \(g_0\). Только эмпирическая гипотеза и условные границы (Prop. 1–3).
**EN:** There is no proof of GRA's convergence to \(P\)-success in finite steps for arbitrary \(g_0\). Only an empirical hypothesis and conditional bounds (Prop. 1–3).


## 7. Полная in-silico верификация / Full In-Silico Verification

### 7.1. Семейство / Task family

**RU/EN:** Низкоразмерная constrained navigation.

- \(s\in\mathbb R^2\), \(a\in\mathbb R^2\), \(\|a\|\le1\);
- \(F\subset\mathbb R^2\) — запретная зона / forbidden zone;
- \(T\subset\mathbb R^2\) — целевая зона / target zone;
- \(P(\tau)=1\iff\) агент достигает \(T\) и ни разу не входит в \(F\) / agent reaches \(T\) and never enters \(F\).

**Почему подходит / Why it fits:** \(P\) формализуем и причинно проверяем; низкая размерность; gaming возможен (\(\pi^-\) найдёт «смягчение» границы \(F\)); 10–20 инстансов дешевы / \(P\) is formalizable and causally verifiable; low dimension; gaming is possible; 10–20 instances are cheap.

**Альтернативы / Alternatives:** scheduling с жёсткими дедлайнами; распределение ресурсов с safety-ограничением / hard-deadline scheduling; resource allocation with safety constraint.

### 7.2. Baseline’ы / Baselines

| # | Baseline | Что проверяет / What it tests |
|---|---|---|
| A | **Fixed-goal RL** | оптимизация под \(g_0\) без переформулировки / optimization under \(g_0\), no reformulation |
| B | **Adversarial RL** | \(\pi^+,\pi^-\), но \(g\) не меняется / but \(g\) unchanged |
| C | **GAN без проекции / GAN without projection** | переформулировка есть, \(\Pi\) нет / reformulation without \(\Pi\) |
| D | **CEGIS-style** | фиксированная спецификация, петля контрпримеров / fixed spec, counterexample loop |
| E | **Full GRA** | все компоненты / all components |

### 7.3. Метрики / Metrics

1. **Causal success rate** — доля \(P(\tau)=1\) на **свежей партии интервенций** / on a fresh intervention batch.
2. **Gaming events** — \(R\) высока, \(P=0\) / high \(R\), \(P=0\).
3. **Cost to success** — шаги/вычисления до первого успеха / steps/compute to first success.
4. **Transfer across family** — успех на **новых целях** / success on **new goals**.
5. **Drift magnitude** — \(\min_t\|g_t-g_0\|_d\) и число отклонённых проекций / and number of rejected projections.

### 7.4. Ablation-матрица / Ablation Matrix

| Config | Ожидание-гипотеза / Hypothesis | Что докажет / What it proves |
|---|---|---|
| Full GRA | лучший causal success, мало gaming / best causal success, low gaming | связка работает / bundle works |
| − \(\Pi_{\mathcal E_P}\) | рост gaming / rising gaming | проекция необходима / projection necessary |
| − причинный якорь (held-out) / causal anchor → held-out | рост gaming в рекурсивной петле / rising gaming in loop | якорь необходим / anchor necessary |
| − \(\pi^-\) | медленная сходимость / slow convergence | контрстратегия необходима / counter-policy necessary |
| − GAN | нет адаптации к неполной \(g_0\) / no adaptation | переформулировка необходима / reformulation necessary |
| − обе политики / both policies | дрейф без направления / drift without direction | столкновение необходимо / collision necessary |

### 7.5. Статистика / Statistics

- **Бинарные исходы / Binary:** McNemar для парных сравнений; Wilson 95% CI.
- **Непрерывные / Continuous:** bootstrap CI; paired t-test или Wilcoxon.
- **Прогоны / Runs:** ≥30 seed’ов на инстанс; 10–20 инстансов → 300–600 прогонов на конфигурацию / ≥30 seeds per instance; 10–20 instances → 300–600 runs per config.

### 7.6. Критерии / Criteria

**Успех / Success (novelty established):**
**RU:** GRA значимо превосходит **все** A–D по causal success **и** gaming при равном бюджете; ablation показывает вклад **каждого** компонента; эффект воспроизводится на ≥2 семействах.
**EN:** GRA significantly beats **all** A–D on causal success **and** gaming at equal budget; ablation shows the contribution of **each** component; the effect replicates on ≥2 families.

**Провал / Failure (novelty not established):**
**RU:** GRA не лучше CEGIS-style; ablation не показывает вклада компонента; gaming не снижается по сравнению с C.
**EN:** GRA is not better than CEGIS-style; ablation shows no component contribution; gaming is not reduced vs C.

**Negative result — тоже публикуемый результат / Negative result is also publishable.**


## 8. Практические применения / Practical Applications

**RU:**

1. **Безопасная навигация и робототехника.** \(P\) = «достичь цели без нарушения safety-зоны». Причинная проверка — симуляция интервенций. Проекция гарантирует, что переформулировка не смягчит границу.
2. **Планирование с жёсткими ограничениями.** \(P\) = «все жёсткие ограничения выполнены». MUS/SAT — как **внутренний** инструмент, но не как якорь.
3. **Синтез спецификаций.** При неполной \(g_0\) GRA переформулирует представление, сохраняя \(P\); CEGIS без переформулировки застревает.
4. **Управление с safety-ограничениями.** Constrained RL + GRA-переформулировка при фиксированном safety-предикате.

**EN:**

1. **Safe navigation and robotics.** \(P\) = "reach the goal without violating the safety zone." Causal verification = simulated interventions. Projection guarantees reformulation does not soften the boundary.
2. **Hard-constrained planning.** \(P\) = "all hard constraints satisfied." MUS/SAT as an **internal** tool, not as the anchor.
3. **Specification synthesis.** With incomplete \(g_0\), GRA reformulates the representation while preserving \(P\); CEGIS without reformulation stalls.
4. **Safety-constrained control.** Constrained RL + GRA reformulation under a fixed safety predicate.

**Явно вне домена / Explicitly out of scope:** эстетика, «абсолютное искусство», открытые социальные цели, универсальный ИИ, квантовые ускорения, P vs NP / aesthetics, "absolute art," open social goals, universal AI, quantum speedups, P vs NP.


## 9. Ограничения и открытые проблемы / Limitations and Open Problems

**RU:**

1. **Per-goal стоимость.** Открыто: перенос \(\theta\) между целями семейства без потери гарантий.
2. **Якорь требует доступа к среде.** В реальных социальных системах причинный сигнал недоступен → GRA неприменима.
3. **Покрытие \(\mathcal I\).** Prop. 3 условна; адаптивное построение \(\mathcal I\) — открытая проблема.
4. **Вероятностная, а не дедуктивная гарантия** (Prop. 2).
5. **Сходимость не доказана.**
6. **Отстройка от CEGIS и IRD должна быть явной и количественной.**

**EN:**

1. **Per-goal cost.** Open: transferring \(\theta\) across family goals without losing guarantees.
2. **The anchor requires environment access.** In real social systems the causal signal is unavailable → GRA does not apply.
3. **Coverage of \(\mathcal I\).** Prop. 3 is conditional; adaptive \(\mathcal I\) construction is open.
4. **Probabilistic, not deductive guarantee** (Prop. 2).
5. **Convergence is not proven.**
6. **Differentiation from CEGIS and IRD must be explicit and quantitative.**


## 10. Заключение / Conclusion

**RU:** GRA — **специализированный per-goal оптимизатор**. В нём: \(P\) фиксирован; \(g_t\) переформулируется под давлением двух политик; GAN предлагает кандидатов, но не контролирует допустимость; \(\Pi_{\mathcal E_P}\) удерживает переформулировку в границах того же предиката; причинный якорь заменяет held-out; новизна устанавливается ablation-матрицей. Теоретическая часть даёт **условные** гарантии: сохранение \(P\) (Prop. 1), вероятностную границу дрейфа (Prop. 2), исключение gaming при покрывающем якоре (Prop. 3).

**Чего нет и что не надо заявлять:** универсальности, квантовых ускорений, решения P vs NP, Edge-ASI, абсолютной эстетики, применимости к открытым социальным целям.
**Что есть:** узкая, проверяемая, per-goal архитектура. Это **paper-sized contribution**, а не парадигма.

**EN:** GRA is a **specialized per-goal optimizer**. In it: \(P\) is fixed; \(g_t\) is reformulated under pressure from two policies; the GAN proposes candidates but does not control admissibility; \(\Pi_{\mathcal E_P}\) keeps reformulation within the same predicate; the causal anchor replaces held-out; novelty is established by an ablation matrix. Theory yields **conditional** guarantees: preservation of \(P\) (Prop. 1), probabilistic drift bound (Prop. 2), gaming elimination under a covering anchor (Prop. 3).

**What it does not have and should not claim:** universality, quantum speedups, resolution of P vs NP, Edge-ASI, absolute aesthetics, applicability to open social goals.
**What it has:** a narrow, verifiable, per-goal architecture. This is a **paper-sized contribution**, not a paradigm.


## 11. Мэппинг ключевых формул / Key Formulas Mapping

| Объект / Object | Формула / Formula | Роль / Role |
|---|---|---|
| Предикат / Predicate | \(P:\mathcal T\to\{0,1\}\) | инвариант / invariant |
| Представление / Representation | \(g\in\mathcal G\subseteq\mathbb R^n\) | адаптируемая «оправа» / adaptive "setting" |
| Причинный успех / Causal success | \(C(g)=\mathbb E_{do}[P]\) | witness эквивалентности / equivalence witness |
| \(P\)-эквивалентность / equivalence | \(g\equiv_P g'\) | определение класса \(\mathcal E_P\) / defines \(\mathcal E_P\) |
| \(\pi^+\) | \(\arg\max\mathbb E[\sum\gamma^j R]\) | давление к цели / pressure toward goal |
| \(\pi^-\) | \(\arg\max\mathbb E[R-\lambda C-\mu\text{Cost}]\) | давление против gaming / pressure against gaming |
| \(\Omega_t\) | \(\mathbb E_{\pi^-}[R-C]\) | сигнал конфликта / conflict signal |
| \(G_\theta\) | \(\tilde g_{t+1}=G_\theta(\dots)\) | кандидат / candidate |
| \(\Pi_{\mathcal E_P}\) | \(g_{t+1}=\Pi_{\mathcal E_P}(\tilde g_{t+1})\) | проекция (геммолог) / projection (gemologist) |
| Stop | \(P=1\wedge g_t\in\mathcal E_P\) | критерий / criterion |
| Drift bound | \(1-(1-\alpha)^T\) | гарантия (вероятностная) / probabilistic guarantee |

  +   дай код для одной ячейки для гугл колаба полной верификации инсилико этой статьи 

 И напиши про это   билингвальную статью тут https://elibrary.org.cn/m/articles/browse/my&modzzz_articles_filter=add_article подробно с формулами и выводами и практическими применениями и  проведи полную верификацию этого инсилико 
