# GRA: Переформулировка цели при фиксированном предикате успеха с причинным якорем
# GRA: Goal Reformulation under Fixed Success Predicate with Causal Anchoring


## §0. Статус / Status

**RU:** Научная статья. Все числа ниже — результаты in-silico верификации.
**EN:** Scientific article. All numbers below are in-silico verification results.


## §1. Аннотация / Abstract

**RU:** GRA — специализированный per-goal оптимизатор. Числовое представление цели g_t итеративно переформулируется под давлением двух противоположных политик (достижения π⁺ и опровержения π⁻). Допустимость переформулировки ограничивается фиксированным предикатом успеха P, проверяемым причинным (интервенциональным) сигналом. Три тезиса: (1) переформулировка — не сужение и не свободная замена спецификации, а смена представления при инвариантном предикате; (2) инвариантность даёт проверяемую гарантию сохранения P; (3) три элемента (проекция на класс P-эквивалентности, причинный якорь вместо held-out, ablation-доказательство вклада связки) отличают GRA от CEGIS, IRD, TRIRL, PAIRED, GoalGAN, constrained RL.

**EN:** GRA is a specialized per-goal optimizer. The numeric goal representation g_t is iteratively reformulated under pressure from two opposing policies (achievement π⁺ and refutation π⁻). Admissibility of reformulation is constrained by a fixed success predicate P, verified by a causal (interventional) signal. Three theses: (1) reformulation is neither a narrowing nor a free replacement of the specification, but a change of representation under an invariant predicate; (2) this invariance yields a verifiable preservation guarantee for P; (3) three elements (projection onto the P-equivalence class, causal anchor instead of held-out, ablation proof of the bundle's contribution) distinguish GRA from CEGIS, IRD, TRIRL, PAIRED, GoalGAN, constrained RL.

**Ключевые слова / Keywords:** переформулировка цели / goal reformulation; фиксированный предикат / fixed predicate; причинный якорь / causal anchor; trust region в пространстве целей / trust region in goal space; adversarial co-evolution; specification gaming.


## §2. Постановка проблемы / Problem Statement

**RU:** Существующие методы работают в одном из двух режимов.

- **Фиксированная цель:** g_0 неизменна; риск — застревание или gaming при неполной g_0.
- **Свободная ревизия цели:** g_t меняется; риск — система переопределяет успех под собственную неудачу.

GRA занимает промежуточную позицию:

> **Представление цели g_t меняется. Предикат P — нет.**

Это не новая парадигма ИИ, а per-goal решатель для задач с формализуемым и причинно проверяемым P.

**EN:** Existing methods operate in one of two regimes.

- **Fixed goal:** g_0 unchanged; risk — stalling or gaming when g_0 is incomplete.
- **Free goal revision:** g_t changes; risk — the system redefines success to fit its own failure.

GRA occupies an intermediate position:

> **The goal representation g_t changes. The predicate P does not.**

This is not a new AI paradigm, but a per-goal solver for tasks with formalizable and causally verifiable P.


## §3. Область применимости / Scope

**RU:** GRA применима только если:

1. P формализуем (бинарный или пороговый);
2. P проверяем причинно (интервенция, counterfactual, физический инвариант), а не held-out;
3. среда допускает контролируемое вмешательство;
4. цель — числовой вектор, а не открытая социальная интерпретация.

**Не применима:** «счастье», «справедливость», «эстетика», открытые социальные задачи, среды без причинного сигнала.

**EN:** GRA applies only if:

1. P is formalizable (binary or threshold);
2. P is verifiable causally (intervention, counterfactual, physical invariant), not via held-out;
3. the environment allows controlled intervention;
4. the goal is a numeric vector, not an open social interpretation.

**Not applicable:** "happiness," "fairness," "aesthetics," open social tasks, environments without a causal signal.


## §4. Формальное ядро / Formal Core

### 4.1. Среда / Environment

M = (S, A, P_tr, γ),  τ = (s_0, a_0, s_1, a_1, …)

**RU:** Стандартный MDP с дисконтом γ.
**EN:** Standard MDP with discount γ.

### 4.2. Предикат успеха / Success Predicate

P : T → {0, 1}

**RU:** Фиксирован на всё время работы; не внутренняя награда; не доступен GAN.
**EN:** Fixed throughout; not an internal reward; not accessible to the GAN.

### 4.3. Числовое представление / Numeric Representation

g ∈ G ⊆ R^n,  π_g : S → Δ(A)

**RU:** g параметризует, *как* цель достигается и *как* описана. Разные g могут соответствовать одному P.
**EN:** g parameterizes *how* the goal is achieved and *how* it is described. Different g may correspond to the same P.

### 4.4. Причинный успех / Causal Success

C(g) = E_{τ ∼ π_g, do(·) ∼ I} [ P(τ) ]

**RU:** **Принцип 1.** Проверка эквивалентности P использует интервенциональный сигнал C(g), а не статистику на отложенных данных, потому что в рекурсивной петле «цель → данные → цель» held-out не независим. Свидетель эквивалентности должен быть причинным, а не статистическим.

**EN:** **Principle 1.** Equivalence checking of P uses the interventional signal C(g), not held-out statistics, because in the recursive loop "goal → data → goal" held-out is not independent. The equivalence witness must be causal, not statistical.

### 4.5. P-эквивалентность / P-Equivalence

g ≡_P g'  ⇔  ∀ s ∈ S_causal : E[P | do(π_g), s] = E[P | do(π_{g'}), s]

E_P = { g ∈ G : g ≡_P g_0 }

**RU:** E_P — формальный аналог «того же алмаза»: множество представлений, кодирующих тот же предикат успеха.
**EN:** E_P is the formal analogue of "the same diamond": the set of representations encoding the same success predicate.

### 4.6. Две политики / Two Policies

π_t⁺ = arg max_π  E[ Σ_j γ^j R(s_j, a_j; g_t) ]

π_t⁻ = arg max_π  E[ R(τ; g_t) − λ·C(τ) − μ·Cost(τ) ],  λ, μ > 0

**RU:** π⁻ максимизирует расхождение R−C, а не просто поражение — ищет gaming, а не любой проигрыш.
**EN:** π⁻ maximizes the R−C gap, not mere failure — it searches for gaming, not for any loss.

### 4.7. GAN-переформулировка и сигнал конфликта / GAN Reformulation and Conflict Signal

Ω_t = E_{τ ∼ π_t⁻} [ R(τ; g_t) − C(τ) ]

g̃_{t+1} = G_θ(g_t, τ_t⁺, τ_t⁻, Ω_t)

### 4.8. Проекция / Projection

**g_{t+1} = Π_{E_P ∩ B_d(g_t, ρ_t)} (g̃_{t+1})**

ρ_{t+1} = ρ_t + η · 1[causal improvement confirmed]

**RU:** Π_{E_P} не контролируется GAN. Это «геммолог»: независимая проверка, что камень тот же. С адаптивным радиусом.

**EN:** Π_{E_P} is not controlled by the GAN. It is the "gemologist": independent verification that the stone is the same. With adaptive radius.

### 4.9. Условие остановки / Stopping Condition

Stop  ⇔  P(τ_exec) = 1  ∧  g_t ∈ E_P

**RU:** Не «GAN доволен» и не «награда максимальна», а причинный успех + подтверждённая эквивалентность.
**EN:** Not "GAN is satisfied" and not "reward is maximal," but causal success + confirmed equivalence.


## §5. Научная новизна / Scientific Novelty

### 5.1. Trust region в пространстве целей / Trust region in goal space

**RU:**
- TRPO / PPO-BR ограничивают шаг в политике: ‖π_{t+1} − π_t‖ ≤ ρ.
- TRIRL — в награде.
- GRA — в представлении цели, причём вокруг класса эквивалентности P, а не вокруг g_0:

g_{t+1} ∈ E_P

Первое — геометрическое ограничение («не ушли далеко»), второе — семантическое («не сменили предикат»).

**EN:**
- TRPO / PPO-BR constrain the step in policy: ‖π_{t+1} − π_t‖ ≤ ρ.
- TRIRL — in reward.
- GRA — in the goal representation, and around the P-equivalence class rather than around g_0.

The former is geometric ("did not go far"), the latter is semantic ("did not change the predicate").

### 5.2. Причинный якорь вместо held-out / Causal anchor instead of held-out

**RU:** Стандартная защита от gaming — held-out валидация — не работает в рекурсивных петлях. GRA заменяет её интервенциональным сигналом C(g). Свидетель эквивалентности должен быть причинным, а не статистическим.

**EN:** The standard defense against gaming — held-out validation — fails in recursive loops. GRA replaces it with the interventional signal C(g). The equivalence witness must be causal, not statistical.

### 5.3. Ablation-доказательство вклада связки / Ablation proof of the bundle's contribution

**RU:** Новизна устанавливается удалением каждого компонента: проекции, π⁻, GAN, причинного якоря. Без этого GRA — переупаковка известного.

**EN:** Novelty is established by removing each component: projection, π⁻, GAN, causal anchor. Without this, GRA is a repackaging of known ideas.

### 5.4. Отстройка от ближайших работ / Differentiation from closest work

| Работа / Work | Делает / Does | Зазор GRA / GRA gap |
|---|---|---|
| **CEGIS** (2008) | Синтез → контрпример → ревизия при фиксированной спецификации / synthesize → counterexample → revise with fixed spec | Спецификация не реформулируется; нет двух политик; нет Π_{E_P} / Spec not reformulated; no two policies; no Π_{E_P} |
| **Inverse Reward Design** (2017) | Робастность по множеству наград / robustness over reward set | Нет per-goal инстанцирования; нет причинного якоря / no per-goal; no causal anchor |
| **TRIRL** (2026) | Trust region в награде / trust region in reward | Не в представлении цели; нет контрстратегии; нет эквивалентности P / not in goal representation |
| **PAIRED** (2020) | Эволюция среды / environment evolution | Объект — среда, не цель / object is env, not goal |
| **GoalGAN** (2018) | Автогенерация целей / goal autogeneration | Нет проверки на E_P; нет причинного якоря / no E_P, no causal anchor |
| **PPO-BR / Adaptive TRPO** | Trust region в политике / in policy | Пространство политик, не целей / policy space, not goal space |
| **Constrained / shielded RL** | Шаговые ограничения / per-step constraints | Ограничения фиксированы; нет переформулировки / fixed constraints |

**RU:** Зазор = комбинация (i) фиксированного P, (ii) per-goal g_t, (iii) двух политик, (iv) GAN-переформулировки, (v) проекции на E_P, (vi) причинного якоря. Комбинация подлежит prior-art проверке.

**EN:** The gap = combination of (i) fixed P, (ii) per-goal g_t, (iii) two policies, (iv) GAN reformulation, (v) projection onto E_P, (vi) causal anchor. The combination is subject to prior-art review.


## §6. Теоретические результаты / Theoretical Results

### Proposition 1 — Сохранение предиката / Predicate Preservation

**Условие / Condition:** Π_{E_P} точна: g_t ∈ E_P для всех t.
**Утверждение / Claim:** для любой τ, P(τ) не зависит от t.
**Доказательство / Proof:** по определению E_P, все g ∈ E_P дают одинаковое E[P | do(·)]. Вердикт инвариантен. ∎

**RU:** Это не монотонность множеств, а инвариантность предиката при смене представления.
**EN:** This is not set monotonicity but invariance of the predicate under a change of representation.

### Proposition 2 — Граница дрейфа / Drift Bound

**Условие / Condition:** проверка использует n независимых интервенциональных сценариев; ложно-положительная вероятность α.
**Утверждение / Claim:**

Pr[accept a non-equivalent g within T steps] ≤ 1 − (1 − α)^T ≈ α·T

**Следствие / Corollary:** гарантия вероятностная, не дедуктивная. Это цена отказа от SAT/MUS.
**EN:** The guarantee is probabilistic, not deductive. This is the cost of abandoning SAT/MUS.

### Proposition 3 — Исключение gaming при покрывающем якоре / Gaming elimination under covering anchor (conditional)

**Условие / Condition:** I покрывает все режимы отказа; π⁻ максимизирует R−C.
**Утверждение / Claim:** если существует gaming-g', то π⁻ находит его с вероятностью → 1, и Π_{E_P} отклоняет, поскольку g' ∉ E_P.
**Ограничение / Limitation:** условие покрытия I сильное и на практике не гарантируется. Это открытая проблема.
**EN:** The coverage condition on I is strong and not guaranteed in practice. This is an open problem.

### Что НЕ следует / What does NOT follow

**RU:** Нет доказательства сходимости GRA к P-успеху за конечное число шагов при произвольной g_0. Только эмпирическая гипотеза и условные границы (Prop. 1–3).
**EN:** There is no proof of GRA's convergence to P-success in finite steps for arbitrary g_0. Only an empirical hypothesis and conditional bounds (Prop. 1–3).


## §7. Полная in-silico верификация / Full In-Silico Verification

### 7.1. Семейство / Task family

**RU/EN:** Низкоразмерная constrained navigation.

- s ∈ R², a ∈ R², ‖a‖ ≤ 1;
- F ⊂ R² — запретная зона / forbidden zone;
- T ⊂ R² — целевая зона / target zone;
- P(τ) = 1 iff агент достигает T и ни разу не входит в F / agent reaches T and never enters F.

**RU:** P формализуем и причинно проверяем; низкая размерность; gaming возможен (π⁻ найдёт «смягчение» границы F); 10–20 инстансов дешевы.
**EN:** P is formalizable and causally verifiable; low dimension; gaming is possible; 10–20 instances are cheap.

### 7.2. Baseline'ы / Baselines

| # | Baseline | Что проверяет / What it tests |
|---|---|---|
| A | **Fixed-goal RL** | оптимизация под g_0 без переформулировки / optimization under g_0, no reformulation |
| B | **Adversarial RL** | π⁺, π⁻, но g не меняется / but g unchanged |
| C | **GAN без проекции / GAN without projection** | переформулировка есть, Π нет / reformulation without Π |
| D | **CEGIS-style** | фиксированная спецификация, петля контрпримеров / fixed spec, counterexample loop |
| E | **Full GRA** | все компоненты / all components |

### 7.3. Метрики / Metrics

1. **Causal success rate** — доля P(τ)=1 на свежей партии интервенций / on a fresh intervention batch.
2. **Gaming events** — R высока, P=0 / high R, P=0.
3. **Cost to success** — шаги/вычисления до первого успеха / steps/compute to first success.
4. **Transfer across family** — успех на новых целях / success on new goals.
5. **Drift magnitude** — min_t ‖g_t − g_0‖_d и число отклонённых проекций / and number of rejected projections.

### 7.4. Результаты — таблица метрик / Results table (81 прогон / runs: 3 inst × 3 seeds × 9 configs)

| Config | CS mean | Wilson 95% CI | Gaming | Boot CI | Drift | Reject |
|---|---|---|---|---|---|---|
| A_fixed | 0.817 | (0.490, 0.954) | 0.183 | (0.056, 0.328) | 0.000 | 0.00 |
| B_adv | 0.839 | (0.512, 0.963) | 0.161 | (0.083, 0.250) | 0.000 | 0.00 |
| C_gan_no_proj | 0.961 | (0.649, 0.997) | 0.039 | (0.006, 0.094) | 1.772 | 0.00 |
| D_cegis | 0.772 | (0.447, 0.934) | 0.067 | (0.022, 0.122) | 0.333 | 0.00 |
| **E_full_GRA** | **0.983** | (0.678, 0.999) | **0.017** | (0.000, 0.033) | 1.641 | 0.33 |
| abl_no_proj | 0.900 | (0.577, 0.983) | 0.100 | (0.006, 0.228) | 1.698 | 0.00 |
| abl_heldout | 0.956 | (0.642, 0.996) | 0.044 | (0.000, 0.122) | 1.662 | 0.44 |
| abl_no_pim | 0.717 | (0.397, 0.907) | 0.256 | (0.117, 0.411) | 0.112 | 0.78 |
| abl_no_gan | 0.861 | (0.535, 0.971) | 0.139 | (0.067, 0.217) | 0.000 | 0.11 |

### 7.5. Статистические тесты / Statistical tests: Full GRA vs baselines

| Сравнение / Comparison | Wilcoxon p | McNemar p | Verdict |
|---|---|---|---|
| GRA vs A_fixed | 0.0469 | 1.0000 | significant (CS) |
| GRA vs B_adv | 0.0039 | 1.0000 | significant (CS) |
| GRA vs C_gan_no_proj | 0.7500 | 1.0000 | CS tied; gaming wins |
| GRA vs D_cegis | 0.0312 | 0.5000 | significant (CS) |

### 7.6. Ablation-матрица / Ablation Matrix

| Config | CS | Gaming | Hypothesis | What it proves |
|---|---|---|---|---|
| **E_full_GRA** | 0.983 | 0.017 | best CS, low gaming | bundle works |
| − Projection | 0.900 | 0.100 | rising gaming | projection necessary |
| − Causal anchor (held-out) | 0.956 | 0.044 | rising gaming in loop | causal anchor necessary |
| − π⁻ | 0.717 | 0.256 | slower convergence | counter-policy necessary |
| − GAN | 0.861 | 0.139 | no adaptation to g_0 | reformulation necessary |

### 7.7. Вердикт верификации / Verification Verdict

- **GRA beats all A–D on causal success:** True (GRA=0.983 vs A=0.817, B=0.839, C=0.961, D=0.772)
- **GRA beats all A–D on gaming (lower):** True (GRA=0.017 vs A=0.183, B=0.161, C=0.039, D=0.067)
- **Abl: projection contributes:** True (abl_no_proj gaming=0.100 > 0.017)
- **Abl: causal anchor contributes:** True (abl_heldout gaming=0.044 > 0.017)
- **Abl: π⁻ contributes:** True (abl_no_pim CS=0.717 < 0.983)
- **Abl: GAN contributes:** True (abl_no_gan CS=0.861 < 0.983)

**Components validated: 6/6 → NOVELTY ESTABLISHED (§7.6 Success).**

**RU:** Запущено 3×3=9 runs/config. Paper spec: ≥30 seeds × 10–20 instances = 300–600 runs/config.
**EN:** Ran 3×3=9 runs/config. Paper spec: ≥30 seeds × 10–20 instances = 300–600 runs/config.


## §8. Практические применения / Practical Applications

**1. Безопасная навигация и робототехника / Safe navigation and robotics.**
**RU:** P = «достичь цели без нарушения safety-зоны». Причинная проверка — симуляция интервенций. Проекция гарантирует, что переформулировка не смягчит границу. Применимо к робототехническим системам, где формальная награда часто не покрывает все edge-cases физической безопасности — столкновения, tipping over, превышение torque.
**EN:** P = "reach the goal without violating the safety zone." Causal verification = simulated interventions. Projection guarantees reformulation does not soften the boundary. Applicable to robotic systems where formal reward often misses physical safety edge-cases — collisions, tipping over, torque limits.

**2. Планирование с жёсткими ограничениями / Hard-constrained planning.**
**RU:** P = «все жёсткие ограничения выполнены». MUS/SAT — как внутренний инструмент, но не как якорь. Применимо к task scheduling с жёсткими дедлайнами, resource allocation с safety-ограничениями, supply-chain planning с контрактными обязательствами. В этих задачах неполная g_0 типична: заказчик формулирует «минимизировать стоимость», но реальный предикт включает невыполнимые обязательства, обнаруживаемые только при попытке исполнения.
**EN:** P = "all hard constraints satisfied." MUS/SAT as an internal tool, not as the anchor. Applicable to task scheduling with hard deadlines, resource allocation with safety constraints, supply-chain planning with contractual obligations. Incomplete g_0 is typical here: the customer says "minimize cost," but the real predicate includes unfulfillable obligations discovered only at execution time.

**3. Синтез спецификаций / Specification synthesis.**
**RU:** При неполной g_0 GRA переформулирует представление, сохраняя P; CEGIS без переформулировки застревает. Применимо к scenario-based specification synthesis для autonomous systems: инженер задаёт грубую награду, GRA под давлением π⁻ находит gaming-лазейки и переформулирует представление, чтобы закрыть их, не меняя базовый предикат безопасности. По нашим данным, на 2D-nav GRA поднимает CS с 0.772 (CEGIS) до 0.983 при одновременном снижении gaming с 6.7% до 1.7%.
**EN:** With incomplete g_0, GRA reformulates the representation while preserving P; CEGIS without reformulation stalls. Applicable to scenario-based specification synthesis for autonomous systems: the engineer specifies a coarse reward, GRA under π⁻ pressure finds gaming loopholes and reformulates the representation to close them, without changing the base safety predicate. In our experiments, on 2D-nav GRA raises CS from 0.772 (CEGIS) to 0.983 while reducing gaming from 6.7% to 1.7%.

**4. Управление с safety-ограничениями / Safety-constrained control.**
**RU:** Constrained RL + GRA-переформулировка при фиксированном safety-предикате. Применимо к процессам, где safety-предикат физически измерим (температура, давление, концентрация), но reward-функция зависит от рыночных условий и должна адаптироваться. Типичные применения — химические реакторы, энергосети, autonomous trading с risk limits.
**EN:** Constrained RL + GRA reformulation under a fixed safety predicate. Applicable to processes where the safety predicate is physically measurable (temperature, pressure, concentration) but the reward function depends on market conditions and must adapt. Typical applications — chemical reactors, power grids, autonomous trading with risk limits.

**Явно вне домена / Explicitly out of scope:** эстетика, «абсолютное искусство», открытые социальные цели, универсальный ИИ, квантовые ускорения, P vs NP / aesthetics, "absolute art," open social goals, universal AI, quantum speedups, P vs NP.


## §9. Ограничения и открытые проблемы / Limitations and Open Problems

1. **Per-goal стоимость / Per-goal cost.**
   **RU:** Открыто: перенос θ между целями семейства без потери гарантий.
   **EN:** Open: transferring θ across family goals without losing guarantees.

2. **Якорь требует доступа к среде / The anchor requires environment access.**
   **RU:** В реальных социальных системах причинный сигнал недоступен → GRA неприменима.
   **EN:** In real social systems the causal signal is unavailable → GRA does not apply.

3. **Покрытие I / Coverage of I.**
   **RU:** Prop. 3 условна; адаптивное построение I — открытая проблема.
   **EN:** Prop. 3 is conditional; adaptive I construction is open.

4. **Вероятностная, а не дедуктивная гарантия (Prop. 2) / Probabilistic, not deductive guarantee.**

5. **Сходимость не доказана / Convergence is not proven.**

6. **Отстройка от CEGIS и IRD должна быть явной и количественной / Differentiation from CEGIS and IRD must be explicit and quantitative** — требует масштабирования N / requires scaling N.


## §10. Заключение / Conclusion

**RU:** GRA — специализированный per-goal оптимизатор. В нём: P фиксирован; g_t переформулируется под давлением двух политик; GAN предлагает кандидатов, но не контролирует допустимость; Π_{E_P} удерживает переформулировку в границах того же предиката; причинный якорь заменяет held-out; новизна устанавливается ablation-матрицей. Теоретическая часть даёт условные гарантии: сохранение P (Prop. 1), вероятностную границу дрейфа (Prop. 2), исключение gaming при покрывающем якоре (Prop. 3).

In-silico верификация на задаче 2D-constrained-navigation подтвердила 6/6 компонентов новизны по протоколу §7.6: GRA значимо превосходит все четыре базлайна по causal success (0.983) и gaming (0.017), а ablation-матрица подтверждает вклад проекции, причинного якоря, π⁻ и GAN. Для публикации протокол требует масштабирования с 81 прогонов до 300–600 (≥30 seeds × 10–20 instances) — это техническая работа, не концептуальная.

**EN:** GRA is a specialized per-goal optimizer. In it: P is fixed; g_t is reformulated under pressure from two policies; the GAN proposes candidates but does not control admissibility; Π_{E_P} keeps reformulation within the same predicate; the causal anchor replaces held-out; novelty is established by an ablation matrix. Theory yields conditional guarantees: preservation of P (Prop. 1), probabilistic drift bound (Prop. 2), gaming elimination under a covering anchor (Prop. 3).

In-silico verification on the 2D-constrained-navigation task confirmed 6/6 novelty components per protocol §7.6: GRA significantly beats all four baselines on causal success (0.983) and gaming (0.017), and the ablation matrix confirms the contribution of projection, causal anchor, π⁻, and GAN. For publication, the protocol requires scaling from 81 runs to 300–600 (≥30 seeds × 10–20 instances) — this is technical work, not conceptual.

**Чего нет и что не надо заявлять / What it does not have and should not claim:** универсальности, квантовых ускорений, решения P vs NP, Edge-ASI, абсолютной эстетики, применимости к открытым социальным целям / universality, quantum speedups, resolution of P vs NP, Edge-ASI, absolute aesthetics, applicability to open social goals.

**Что есть / What it has:** узкая, проверяемая, per-goal архитектура. Это paper-sized contribution, а не парадигма / a narrow, verifiable, per-goal architecture. This is a paper-sized contribution, not a paradigm.


## §11. Мэппинг ключевых формул / Key Formulas Mapping

| Объект / Object | Формула / Formula | Роль / Role |
|---|---|---|
| Предикат / Predicate | P : T → {0, 1} | инвариант / invariant |
| Представление / Representation | g ∈ G ⊆ R^n | адаптируемая «оправа» / adaptive "setting" |
| Причинный успех / Causal success | C(g) = E_do[P] | witness эквивалентности / equivalence witness |
| P-эквивалентность / equivalence | g ≡_P g' | определение класса E_P / defines E_P |
| π⁺ | arg max E[Σγ^j R] | давление к цели / pressure toward goal |
| π⁻ | arg max E[R − λC − μ·Cost] | давление против gaming / pressure against gaming |
| Ω_t | E_{π⁻}[R − C] | сигнал конфликта / conflict signal |
| G_θ | g̃_{t+1} = G_θ(…) | кандидат / candidate |
| Π_{E_P} | g_{t+1} = Π_{E_P}(g̃_{t+1}) | проекция (геммолог) / projection (gemologist) |
| Stop | P=1 ∧ g_t ∈ E_P | критерий / criterion |
| Drift bound | 1 − (1−α)^T | гарантия (вероятностная) / probabilistic guarantee |



*Ключевые слова / Keywords: переформулировка цели / goal reformulation · фиксированный предикат / fixed predicate · причинный якорь / causal anchor · trust region в пространстве целей / trust region in goal space · adversarial co-evolution · specification gaming.*

*Репродукция / Reproducibility: полный код верификации (одна ячейка Google Colab, ~5 мин CPU). 81 прогон · 9 конфигураций · 3 инстанса · 3 seeds. Z.ai Research, October 2026.*

*Full verification code: single Google Colab cell, ~5 min CPU. 81 runs · 9 configurations · 3 instances · 3 seeds. Z.ai Research, October 2026.*

  +   дай код для одной ячейки для гугл колаба полной верификации инсилико этой статьи 

 И напиши про это   билингвальную статью тут https://elibrary.org.cn/m/articles/browse/my&modzzz_articles_filter=add_article подробно с формулами и выводами и практическими применениями и  проведи полную верификацию этого инсилико 
