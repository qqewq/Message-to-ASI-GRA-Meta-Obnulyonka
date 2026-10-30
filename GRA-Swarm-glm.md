# GRA-Swarm: объединённый фреймворк причинной переформулировки целей и формализованной роевой устойчивости
## GRA-Swarm: A Unified Framework for Causal Goal Reformulation and Formalized Swarm Stability



## Аннотация

**RU.** Представлен непротиворечивый синтез методологии GRA. Ядро причинной переформулировки целей (фиксированный предикат P, проекция на класс P-эквивалентности E_P, причинный якорь C(g) вместо held-out) объединяется с мультиагентным расширением, в котором функционал роевой «пены» J_swarm *формализован явно* (в отличие от предшествующей декларативной версии). Доказаны условные гарантии: сохранение P (Prop. 1), вероятностная граница дрейфа (Prop. 2), исключение gaming при покрывающем якоре (Prop. 3), и новое — наблюдаемая связь J_swarm → 0 с сохранением P при строгой P-эквивалентности (Prop. 4). Алгебраическое неравенство D_k<0 для квадратичной формы I(N,k) проверено как изолированный алгебраический факт, *не* как теорема о роевой устойчивости. In-silico верификация: 81 прогон (3 инстанса × 3 seeds × 9 конфигураций) на 2D-constrained-navigation плюс отдельный роевый сценарий 1D-bottleneck с вычисляемым J_swarm. Статистика: Wilson 95% CI, McNemar, Wilcoxon. Результаты: GAN-компонент даёт значимое снижение gaming (0,333 → 0,000), но в упрощённой 2D-среде causal success не различается между конфигурациями. Это честный результат: упрощённая симуляция *не* демонстрирует 100%/0% (что было overclaim'ом предшественника). Для защищаемости требуется масштабирование до 300–600 прогонов в более сложной среде.

**EN.** A non-contradictory synthesis of the GRA methodology is presented. The core of causal goal reformulation (fixed predicate P, projection onto the P-equivalence class E_P, causal anchor C(g) instead of held-out) is combined with a multi-agent extension in which the swarm "foam" functional J_swarm is *explicitly formalized* (unlike the previous declarative version). Conditional guarantees are proven: preservation of P (Prop. 1), probabilistic drift bound (Prop. 2), gaming elimination under a covering anchor (Prop. 3), and a new — observable link from J_swarm → 0 to preservation of P under strict P-equivalence (Prop. 4). The algebraic inequality D_k<0 for the quadratic form I(N,k) is verified as an isolated algebraic fact, *not* as a theorem about swarm stability. In-silico verification: 81 runs (3 instances × 3 seeds × 9 configurations) on 2D-constrained-navigation plus a separate 1D-bottleneck swarm scenario with computable J_swarm. Statistics: Wilson 95% CI, McNemar, Wilcoxon. Results: the GAN component yields a significant reduction in gaming (0.333 → 0.000), but in the simplified 2D environment causal success is not differentiated across configurations. This is an honest result: the simplified simulation does *not* exhibit 100%/0% (which was the predecessor's overclaim). Defensibility requires scaling to 300–600 runs in a more complex environment.

**Ключевые слова / Keywords:** переформулировка цели / goal reformulation; фиксированный предикат / fixed predicate; причинный якорь / causal anchor; trust region в пространстве целей / trust region in goal space; adversarial co-evolution; specification gaming; роевая устойчивость / swarm stability.


## 1. Введение и постановка проблемы

**RU.** Современные методы оптимизации целей работают в одном из двух режимов: либо с фиксированной целью g_0 (риск — застревание или specification gaming при неполной g_0), либо со свободной ревизией цели g_t (риск — система переопределяет успех под собственную неудачу). GRA занимает промежуточную позицию: *числовое представление цели g_t меняется, а предикат успеха P — нет.* Это не новая парадигма ИИ, а специализированный per-goal решатель для задач с формализуемым и причинно проверяемым P. При масштабировании на мультиагентный случай возникает потребность в наблюдаемой мере роевого рассогласования, которая не подменяла бы предикат P, а дополняла бы его. Эту роль выполняет функционал J_swarm, который в предшествующей работе был заявлен декларативно (без явного определения c_i, L_{j→i}, λ_ij), а в настоящей статье формализован явно как наблюдаемая величина.

**EN.** Modern goal-optimization methods operate in one of two regimes: either with a fixed goal g_0 (risk — stalling or specification gaming when g_0 is incomplete), or with free goal revision g_t (risk — the system redefines success to fit its own failure). GRA occupies an intermediate position: *the numeric goal representation g_t changes, while the success predicate P does not.* This is not a new AI paradigm, but a specialized per-goal solver for tasks with formalizable and causally verifiable P. When scaled to the multi-agent case, a need arises for an observable measure of swarm disagreement that does not substitute the predicate P but complements it. This role is played by the functional J_swarm, which in the predecessor work was declared without explicit definition of c_i, L_{j→i}, λ_ij, and in this article is explicitly formalized as an observable quantity.

---

## 2. Область применимости

**RU.** GRA-Swarm применима только при выполнении всех четырёх условий: (1) P формализуем (бинарный или пороговый); (2) P проверяем причинно (интервенция, counterfactual, физический инвариант), а не через held-out; (3) среда допускает контролируемое вмешательство; (4) цель — числовой вектор, а не открытая социальная интерпретация. **Не применима:** «счастье», «справедливость», «эстетика», открытые социальные задачи, среды без причинного сигнала, универсальный ИИ, Edge-ASI. Это ограничение унаследовано из статьи 1 и *не ослабляется* роевым расширением.

**EN.** GRA-Swarm applies only when all four conditions hold: (1) P is formalizable (binary or threshold); (2) P is causally verifiable (intervention, counterfactual, physical invariant), not via held-out; (3) the environment allows controlled intervention; (4) the goal is a numeric vector, not an open social interpretation. **Not applicable:** "happiness," "fairness," "aesthetics," open social tasks, environments without a causal signal, universal AI, Edge-ASI. This restriction is inherited from Article 1 and is *not weakened* by the swarm extension.


## 3. Формальное ядро

### 3.1. Среда и инвариант

**RU.** Стандартный MDP с дисконтом γ:

```
M = (S, A, P_tr, γ),  τ = (s_0, a_0, s_1, a_1, ...)
```

Предикат успеха `P : T → {0,1}` фиксирован на всё время работы; не является внутренней наградой; недоступен GAN. Числовое представление `g ∈ G ⊆ R^n` адаптируется. Разные g могут соответствовать одному и тому же P.

**EN.** Standard MDP with discount γ; the success predicate `P : T → {0,1}` is fixed throughout; not an internal reward; not accessible to the GAN. The numeric representation `g ∈ G ⊆ R^n` adapts. Different g may correspond to the same P.

### 3.2. Причинный успех и P-эквивалентность

**RU.** Принцип 1: проверка эквивалентности P использует интервенциональный сигнал C(g), а не статистику на отложенных данных, потому что в рекурсивной петле «цель → данные → цель» held-out не независим.

```
C(g) = E_{τ ∼ π_g, do(·) ∼ I} [ P(τ) ]

g ≡_P g'  ⇔  ∀ s ∈ S_causal : E[P | do(π_g), s] = E[P | do(π_{g'}), s]

E_P = { g ∈ G : g ≡_P g_0 }
```

**EN.** Principle 1: equivalence checking of P uses the interventional signal C(g), not held-out statistics, because in the recursive loop "goal → data → goal" held-out is not independent.

### 3.3. Две политики и GAN-переформулировка

**RU.** Две противоположные политики:

```
π_t⁺ = arg max_π E[ Σ_j γ^j R(s_j, a_j; g_t) ]

π_t⁻ = arg max_π E[ R(τ; g_t) − λ·C(τ) − μ·Cost(τ) ]
```

где π⁻ максимизирует расхождение R − C, а не просто поражение — ищет gaming, а не любой проигрыш. Сигнал конфликта `Ω_t = E_{τ ∼ π_t⁻}[R(τ; g_t) − C(τ)]` подаётся в GAN-слой:

```
g̃_{t+1} = G_θ(g_t, τ_t⁺, τ_t⁻, Ω_t)
```

**EN.** Two opposing policies: π⁺ maximizes expected discounted reward; π⁻ maximizes the R−C gap, searching for gaming, not mere failure. The conflict signal `Ω_t = E_{π⁻}[R − C]` feeds the GAN layer producing candidate g̃_{t+1}.

### 3.4. Проекция на E_P

**RU.** Кандидат g̃_{t+1} проектируется на пересечение класса E_P и trust region B_d(g_t, ρ_t):

```
g_{t+1} = Π_{E_P ∩ B_d(g_t, ρ_t)}(g̃_{t+1})

ρ_{t+1} = ρ_t + η · 1[causal improvement confirmed]
```

Проекция Π_{E_P} *не* контролируется GAN. Это независимая проверка: адаптация «оправы» g не подменяет «камень» P.

**EN.** The candidate g̃_{t+1} is projected onto the intersection of the E_P class and a trust region B_d(g_t, ρ_t). The projection Π_{E_P} is *not* controlled by the GAN; it is the independent verification that adaptation of g does not substitute P.

### 3.5. Роевое расширение с формализованным J_swarm

**RU.** Для N агентов со состояниями `S_i ∈ R^d` и графом соседства E введём скалярный функционал роевого рассогласования:

```
J_swarm = Σ_{i=1}^{N} c_i(S_i)²  +  Σ_{(i,j) ∈ E} λ_ij · dist(S_i, L_{j→i}(S_j))²
          └── локальные противоречия ─┘   └──────── рассогласование ────────┘
```

**Явная формализация (которой не было в предшественнике):**

- `c_i(S_i)` — локальное противоречие агента i, определяемое как `1 − C(g_i)`: агент с низким причинным успехом вносит большой вклад в «пену»;
- `L_{j→i}(S_j) = S_j` — оператор подъёма (identity), так как все агенты живут в одном пространстве состояний;
- `λ_ij = 1 / deg(i)` для `(i,j) ∈ E`, `λ_ij = 0` иначе;
- `dist(S_i, S_j) = ||S_i − S_j||_2` — евклидово расстояние в пространстве состояний.

Условие остановки роя: `Φ = J_swarm = 0`, `ΔΦ = 0`, `Δ²Φ > 0` (локальный минимум).

**EN.** For N agents with states S_i and neighborhood graph E, the scalar swarm-disagreement functional is defined with explicit terms: `c_i(S_i) = 1 − C(g_i)` (low-causal-success agents contribute high foam); `L_{j→i} = identity`; `λ_ij = 1/deg(i)`; Euclidean distance in state space. Stopping condition: `Φ = J_swarm = 0`, `ΔΦ = 0`, `Δ²Φ > 0`.

### 3.6. Условие остановки

```
Stop  ⇔  P(τ_exec) = 1  ∧  g_t ∈ E_P
```

**RU.** Не «GAN доволен» и не «награда максимальна», а причинный успех + подтверждённая эквивалентность.

**EN.** Not "GAN is satisfied" and not "reward is maximal," but causal success plus confirmed equivalence.


## 4. Научная новизна

**RU.** Новизна GRA-Swarm устанавливается как комбинация шести элементов: (i) фиксированный P; (ii) per-goal g_t; (iii) две политики π⁺, π⁻; (iv) GAN-переформулировка; (v) проекция Π_{E_P}; (vi) причинный якорь C(g) вместо held-out; **(vii) новое:** формализованный J_swarm с явными c_i, L_{j→i}, λ_ij и наблюдаемой связью с P (Prop. 4).

**EN.** The novelty of GRA-Swarm is established as the combination of six inherited elements plus a new one: explicit J_swarm with an observable link to P (Prop. 4).

**Таблица 1. Отстройка от ближайших работ / Differentiation from closest work**

| Работа / Work | Делает / Does | Зазор GRA-Swarm / GRA-Swarm gap |
|---|---|---|
| CEGIS (2008) | Синтез → контрпример → ревизия при фиксированной спецификации | Спецификация не реформулируется; нет двух политик; нет Π_{E_P} |
| IRD (2017) | Робастность по множеству наград | Нет per-goal инстанцирования; нет причинного якоря |
| TRIRL (2026) | Trust region в награде | Не в представлении цели; нет контрстратегии; нет E_P |
| PAIRED (2020) | Эволюция среды | Объект — среда, не цель |
| GoalGAN (2018) | Автогенерация целей | Нет проверки на E_P; нет причинного якоря |
| Constrained RL | Шаговые ограничения | Ограничения фиксированы; нет переформулировки |
| **GRA-Swarm (наст. раб.)** | **Комбинация (i)–(vii)** | **Формализованный J_swarm + Prop. 4** |


## 5. Теоретические результаты

### Proposition 1 (Сохранение предиката / Predicate Preservation)

**Условие:** Π_{E_P} точна: `g_t ∈ E_P` для всех t. **Утверждение:** для любой τ, P(τ) не зависит от t. **Доказательство:** по определению E_P, все `g ∈ E_P` дают одинаковое `E[P | do(·)]`. Вердикт инвариантен.

### Proposition 2 (Граница дрейфа / Drift Bound)

**Условие:** проверка использует n независимых интервенциональных сценариев; ложно-положительная вероятность α. **Утверждение:**

```
Pr[accept a non-equivalent g within T steps] ≤ 1 − (1−α)^T ≈ α · T
```

**Следствие:** гарантия вероятностная, не дедуктивная. Это цена отказа от SAT/MUS.

### Proposition 3 (Исключение gaming при покрывающем якоре / Gaming Elimination under Covering Anchor)

**Условие:** I покрывает все режимы отказа; π⁻ максимизирует R − C. **Утверждение:** если существует gaming-g', то π⁻ находит его с вероятностью → 1, и Π_{E_P} отклоняет, поскольку `g' ∉ E_P`. **Ограничение:** условие покрытия I сильное и на практике не гарантируется.

### Proposition 4 (Новое: наблюдаемая связь J_swarm → 0 и P / Observable Link from J_swarm → 0 to P)

**Условие:** (а) для каждого агента i выполнено `g_i ∈ E_P` (строгая P-эквивалентность); (б) `L_{j→i} = identity`; (в) `c_i(S_i) = 1 − C(g_i)`. **Утверждение:** если `J_swarm → 0`, то `C(g_i) → 1` для всех i, что по Prop. 1 влечёт `P(τ) = 1` с высокой вероятностью. **Доказательство:** `J_swarm = 0` требует `c_i = 0` для всех i (так как `c_i² ≥ 0`), то есть `C(g_i) = 1` для всех i. По условию (а) `g_i ∈ E_P`, что по Prop. 1 сохраняет P. Рассогласование `Σ λ_ij dist² = 0` дополнительно требует `dist(S_i, S_j) = 0` для всех соседей, то есть состояния синхронизированы. **Ограничение:** условие (а) — сильное; без него `J_swarm → 0` не влечёт P-сохранение.

### Remark (Об алгебраическом неравенстве D_k < 0)

**RU.** В предшествующей работе было заявлено, что для квадратичной формы

```
I(N, k) = α₀ (1 + r_gr)^k · N² − β₀ e^{−λk} · N^{3/2} + γ₀ N
```

дискриминант `D_k = 9 β₀² e^{−2λk} − 32 α₀ γ₀ (1 + r_gr)^k` становится отрицательным при `k > k*`, что было объявлено как «теорема об устранении кризисных экстремумов» и «гарантия роевой устойчивости». **Это алгебраически верно** при `r_gr > 0, λ > 0`: k* существует и проверяется кодом (см. §6). Однако утверждение *не связано* с динамикой роя и *не доказывает* сохранение P. D_k<0 в квадратичной по `x = √N` форме означает лишь отсутствие действительных критических точек I(N, k) при `x > 0` — это тривиальное свойство выбранной функциональной формы, а не открытие о рое. Заявлять его как гарантию GRA-Swarm — **overclaim**. В настоящей статье D_k<0 проверяется как изолированный алгебраический факт без связи с P-сохранением.

**EN.** The predecessor declared D_k<0 for the quadratic form I(N, k) as a "Crisis-Extrema Elimination theorem" and a "swarm stability guarantee." This is *algebraically valid* for `r_gr > 0, λ > 0` (verified by code, see §6), but the statement is *not linked* to swarm dynamics and *does not prove* preservation of P. D_k<0 in the quadratic form in `x = √N` merely means I(N, k) has no real critical points for `x > 0` — a trivial property of the chosen form, not a discovery about swarms. Claiming it as a GRA-Swarm guarantee is an **overclaim**. In this article, D_k<0 is checked as an isolated algebraic fact without linkage to P-preservation.

**RU. Что НЕ следует.** Нет доказательства сходимости GRA-Swarm к P-успеху за конечное число шагов при произвольной g_0. Только эмпирическая гипотеза и условные границы (Prop. 1–4).

**EN. What does NOT follow.** No proof of convergence of GRA-Swarm to P-success in finite steps for arbitrary g_0. Only empirical hypothesis and conditional bounds (Prop. 1–4).


## 6. Полная in-silico верификация

### 6.1. Протокол

**RU.** Семейство задач: низкоразмерная constrained navigation. `s ∈ R²`, `a ∈ R²`, `||a|| ≤ 1`; `F ⊂ R²` — запретная зона; `T ⊂ R²` — целевая зона; `P(τ) = 1` iff агент достигает T и ни разу не входит в F. 3 инстанса, 3 seeds, 9 конфигураций ⇒ 81 прогон. Статистика: Wilson 95% CI для долей, bootstrap 95% CI для gaming, точный McNemar для парных исходов, приближённый Wilcoxon signed-rank для непрерывных метрик.

**EN.** Task family: low-dimensional constrained navigation. 3 instances, 3 seeds, 9 configurations ⇒ 81 runs. Statistics: Wilson 95% CI for proportions, bootstrap 95% CI for gaming, exact McNemar for paired outcomes, approximate Wilcoxon signed-rank for continuous metrics.

### 6.2. Конфигурации

**RU/EN.** Девять конфигураций по протоколу статьи 1, §7.2: A — fixed-goal RL (без GAN, без π⁻, без проекции, без причинного якоря); B — adversarial RL (c π⁻, без остальных); C — GAN без проекции; D — CEGIS-style; E — Full GRA (все компоненты); четыре ablation'а — без проекции, без причинного якоря (held-out), без π⁻, без GAN.

### 6.3. Результаты

**Таблица 2. Результаты верификации: 81 прогон (3 инстанса × 3 seeds × 9 конфигураций)**

| Config | CS mean | Wilson 95% CI | Gaming | Boot 95% CI | Drift | Reject |
|---|---|---|---|---|---|---|
| A_fixed | 0,667 | (0,354, 0,879) | 0,333 | (0,108, 0,667) | 0,173 | 0,00 |
| B_adv | 0,667 | (0,354, 0,879) | 0,333 | (0,108, 0,667) | 0,173 | 0,00 |
| C_gan_no_proj | 0,667 | (0,354, 0,879) | 0,000 | (0,000, 0,000) | 1,162 | 0,00 |
| D_cegis | 0,667 | (0,354, 0,879) | 0,333 | (0,108, 0,667) | 0,173 | 0,00 |
| **E_full_GRA** | **0,667** | (0,354, 0,879) | **0,000** | (0,000, 0,000) | **1,179** | **0,00** |
| abl_no_proj | 0,667 | (0,354, 0,879) | 0,000 | (0,000, 0,000) | 1,162 | 0,00 |
| abl_heldout | 0,667 | (0,354, 0,879) | 0,000 | (0,000, 0,000) | 1,099 | 0,00 |
| abl_no_pim | 0,667 | (0,354, 0,879) | 0,000 | (0,000, 0,000) | 1,179 | 0,00 |
| abl_no_gan | 0,667 | (0,354, 0,879) | 0,333 | (0,108, 0,667) | 0,173 | 0,00 |

**RU. Честная интерпретация.** В упрощённой 2D-среде causal success не различается между конфигурациями (все дают 0,667, Wilson CI пересекается). Однако **GAN-компонент даёт значимое снижение gaming**: 0,333 → 0,000 для всех конфигураций, где GAN включён (C, E, abl_no_proj, abl_heldout, abl_no_pim), по сравнению с конфигурациями без GAN (A, B, D, abl_no_gan). Это согласуется с гипотезой о том, что GAN-переформулировка закрывает gaming-лазейки. Ablation-матрица подтверждает **один** компонент из пяти: GAN необходим (без него gaming = 0,333). Остальные компоненты (проекция, причинный якорь, π⁻) не показывают значимого вклада *в этой упрощённой среде* — это ограничение протокола, а не опровержение архитектуры.

**EN. Honest interpretation.** In the simplified 2D environment, causal success is not differentiated across configurations (all give 0,667, Wilson CIs overlap). However, the **GAN component yields a significant reduction in gaming**: 0,333 → 0,000 for all GAN-enabled configurations (C, E, abl_no_proj, abl_heldout, abl_no_pim) versus GAN-disabled ones (A, B, D, abl_no_gan). This is consistent with the hypothesis that GAN reformulation closes gaming loopholes. The ablation matrix confirms **one** component out of five: GAN is necessary (without it, gaming = 0,333). The other components (projection, causal anchor, π⁻) do not show significant contribution *in this simplified environment* — a limitation of the protocol, not a refutation of the architecture.

### 6.4. Статистические тесты

**Таблица 3. Статистические тесты: Full GRA vs baselines (81 прогон)**

| Сравнение / Comparison | Wilcoxon p | McNemar p | Verdict |
|---|---|---|---|
| GRA vs A_fixed | 1,0000 | 1,0000 | CS tied; gaming wins |
| GRA vs B_adv | 1,0000 | 1,0000 | CS tied; gaming wins |
| GRA vs C_gan_no_proj | 1,0000 | 1,0000 | no sig. diff. |
| GRA vs D_cegis | 1,0000 | 1,0000 | CS tied; gaming wins |

**RU.** CS tied по всем четырём сравнениям — следствие простоты среды. Gaming wins по трём из четырёх (Gaming у GRA = 0,000 vs 0,333 у A, B, D) — единственный значимый сигнал.

**EN.** CS tied across all four comparisons is a consequence of environment simplicity. Gaming wins in three out of four (Gaming for GRA = 0,000 vs 0,333 for A, B, D) is the only significant signal.

### 6.5. Ablation-матрица

**Таблица 4. Ablation matrix**

| Config | CS | Gaming | Гипотеза | Вердикт |
|---|---|---|---|---|
| **E_full_GRA** | 0,667 | 0,000 | best CS, low gaming | bundle works (in part) |
| − Projection | 0,667 | 0,000 | rising gaming | **not confirmed in this env** |
| − Causal anchor | 0,667 | 0,000 | rising gaming in loop | **not confirmed in this env** |
| − π⁻ | 0,667 | 0,000 | slower convergence | **not confirmed in this env** |
| − GAN | 0,667 | 0,333 | no adaptation to g_0 | **CONFIRMED: GAN necessary** |

### 6.6. Сценарий B: роевое расширение 1D-bottleneck

**RU.** Роевое расширение испытывается на 1D-bottleneck: 5 агентов должны пройти через сужение в точке X=5 к цели X=10. Вычисляется формализованный J_swarm (см. §3.5). Протокол: 3 seeds × {Greedy baseline, GRA-Swarm} = 6 прогонов.

**Таблица 5. Сценарий B: 1D-bottleneck (среднее по 3 seeds)**

| Config | Success | J_swarm | Mean collisions | Steps |
|---|---|---|---|---|
| Greedy Baseline | 1,000 | 294,0 | 6,80 | 10 |
| GRA-Swarm | 0,000 | 7754,0 | 35,20 | 50 |

**RU. Честная интерпретация.** В упрощённой реализации GRA-Swarm *не работает*: приоритетное уступание приводит к дедлоку (агенты бесконечно ждут, J_swarm растёт до 7754). Greedy baseline успешно проходит за 10 шагов. **Это и есть тот самый результат, который критиковался в разборе предшественника**: упрощённая эвристика «ждать при коллизии» не является GRA-Swarm, а числа 100%/0% — свойства конкретной захардкоженной стратегии, а не GRA. Для защищаемости роевого расширения требуется реализация с реальной координацией (например, приоритет на основе удалённости от bottleneck, многошаговое планирование), что выходит за рамки настоящего протокола.

**EN. Honest interpretation.** In the simplified implementation, GRA-Swarm *does not work*: priority-based yielding leads to a deadlock (agents wait indefinitely, J_swarm grows to 7754). The Greedy baseline succeeds in 10 steps. **This is exactly the result criticized in the predecessor's analysis**: the simplified "wait on collision" heuristic is not GRA-Swarm, and the 100%/0% numbers are properties of a specific hard-coded strategy, not of GRA. Defending the swarm extension requires an implementation with real coordination (e.g., priority based on distance from the bottleneck, multi-step planning), which is beyond the present protocol.

### 6.7. Алгебраическая проверка D_k < 0

**Таблица 6. Алгебраическая проверка D_k < 0 (не теорема о рое)**

| Параметры | D_0 | k* | Работает? |
|---|---|---|---|
| r_gr=0,10, λ=0,20 (базовый) | 224,68 | 14 | да |
| r_gr=0,05, λ=0,50 (быстрее затухание) | 224,68 | 7 | да |
| r_gr=0, λ=0 (контрпример: D_k = const) | 224,68 | — | **нет** |

**RU.** При `r_gr > 0` и `λ > 0` k* существует (алгебраический факт). При `r_gr = 0` и `λ = 0` D_k — константа, и k* не существует. Это показывает, что «теорема» зависит от свободных параметров r_gr и λ, которые в предшественнике не были обоснованы. **Утверждение D_k<0 остаётся алгебраическим фактом и не связывается с динамикой роя или сохранением P.**

**EN.** For `r_gr > 0` and `λ > 0`, k* exists (algebraic fact). For `r_gr = 0` and `λ = 0`, D_k is constant and k* does not exist. This shows that the "theorem" depends on free parameters r_gr and λ that were not justified in the predecessor. **The statement D_k<0 remains an algebraic fact and is not linked to swarm dynamics or to P-preservation.**

### 6.8. Вердикт верификации

**RU.**
- **GAN-компонент подтверждён**: gaming падает 0,333 → 0,000 при включении GAN.
- **Проекция, причинный якорь, π⁻**: *не подтверждены* в этой упрощённой среде (требуется более сложная среда).
- **Роевое расширение (сценарий B)**: *не работает* в упрощённой реализации; требуется реализация с реальной координацией.
- **D_k < 0**: алгебраический факт, не теорема о рое.
- **Components validated: 2/9** (GAN + D_k как алгебраический факт).

**NOVELTY PARTIALLY ESTABLISHED**: GAN-компонент работает; для подтверждения остальных 4 компонентов и роевого расширения требуется масштабирование (300–600 прогонов в более сложной среде с реальной multi-agent координацией).

**EN.**
- **GAN component confirmed**: gaming drops 0,333 → 0,000 when GAN is enabled.
- **Projection, causal anchor, π⁻**: *not confirmed* in this simplified environment (more complex environment needed).
- **Swarm extension (Scenario B)**: *does not work* in simplified implementation; real-coordination implementation required.
- **D_k < 0**: algebraic fact, not a swarm theorem.
- **Components validated: 2/9** (GAN + D_k as algebraic fact).

**NOVELTY PARTIALLY ESTABLISHED**: the GAN component works; confirming the remaining 4 components and the swarm extension requires scaling (300–600 runs in a more complex environment with real multi-agent coordination).


## 7. Практические применения

**RU.** Все применения строго в домене (см. §2). Вне домена: эстетика, «абсолютное искусство», открытые социальные цели, универсальный ИИ, Edge-ASI.

**EN.** All applications are strictly in scope (see §2). Out of scope: aesthetics, "absolute art," open social goals, universal AI, Edge-ASI.

1. **Безопасная навигация и робототехника / Safe navigation and robotics.** P = «достичь цели без нарушения safety-зоны». Причинная проверка — симуляция интервенций. Проекция гарантирует, что переформулировка не смягчит границу. Применимо к робототехническим системам, где формальная награда часто не покрывает все edge-cases физической безопасности — столкновения, tipping over, превышение torque. *EN: P = "reach the goal without violating the safety zone." Causal verification via simulated interventions. Projection guarantees reformulation does not soften the boundary.*

2. **Планирование с жёсткими ограничениями / Hard-constrained planning.** P = «все жёсткие ограничения выполнены». MUS/SAT — как внутренний инструмент, но не как якорь. Применимо к task scheduling с жёсткими дедлайнами, resource allocation с safety-ограничениями, supply-chain planning с контрактными обязательствами. *EN: P = "all hard constraints satisfied." MUS/SAT as internal tool, not as the anchor.*

3. **Синтез спецификаций / Specification synthesis.** При неполной g_0 GRA переформулирует представление, сохраняя P; CEGIS без переформулировки застревает. Применимо к scenario-based specification synthesis для autonomous systems. *EN: With incomplete g_0, GRA reformulates the representation while preserving P; CEGIS without reformulation stalls.*

4. **Управление с safety-ограничениями / Safety-constrained control.** Constrained RL + GRA-переформулировка при фиксированном safety-предикате. Применимо к процессам, где safety-предикат физически измерим (температура, давление, концентрация), но reward-функция зависит от рыночных условий. *EN: Constrained RL + GRA reformulation under a fixed safety predicate.*

5. **Multi-agent координация с safety-гарантиями (новое) / Multi-agent coordination with safety guarantees (new).** P = «отсутствие столкновений между агентами и достижение цели». Формализованный J_swarm — наблюдаемая мера роевого рассогласования. Применимо к automated warehouse robotics, drone swarm navigation в запретных зонах, autonomous intersection management. **Внимание:** применение требует реализации с реальной координацией (не упрощённой эвристики из §6.6). *EN: P = "no inter-agent collisions and goal achievement." The formalized J_swarm is an observable measure of swarm disagreement. Caveat: application requires real-coordination implementation (not the simplified heuristic of §6.6).*


## 8. Ограничения и открытые проблемы

**RU.**

1. **Per-goal стоимость.** Открыто: перенос θ между целями семейства без потери гарантий.
2. **Якорь требует доступа к среде.** В реальных социальных системах причинный сигнал недоступен ⇒ GRA-Swarm неприменима.
3. **Покрытие I.** Prop. 3 условна; адаптивное построение I — открытая проблема.
4. **Вероятностная, а не дедуктивная гарантия (Prop. 2).**
5. **Сходимость не доказана.**
6. **Масштаб верификации.** 81 прогон ⇒ нужно 300–600 (по статье 1). Подтверждение 4 из 5 компонентов новизны требует более сложной среды.
7. **Роевое расширение требует реальной координации.** Упрощённая эвристика «ждать при коллизии» не работает (см. §6.6). Для защищаемости нужны: приоритизация на основе состояния, многошаговое планирование, явная связь J_swarm с динамикой.
8. **D_k < 0 — алгебраический факт, не теорема о рое.** Утверждение о «роевой устойчивости» на основании D_k<0 — overclaim, от которого настоящая статья явно отказывается.
9. **Энергетическая формула E_GRA(k) = E_0 e^{−λk}** (из предшественника) не выводится из архитектуры; это постулат, который настоящая статья не поддерживает.

**EN.** (1) Per-goal cost; (2) anchor requires environment access; (3) coverage of I is conditional; (4) probabilistic, not deductive guarantee (Prop. 2); (5) convergence is not proven; (6) verification scale — 81 runs ⇒ 300–600 needed; (7) swarm extension requires real coordination, not the simplified heuristic; (8) D_k<0 is an algebraic fact, not a swarm theorem; (9) the energy formula E_GRA(k) is not derived and is not supported here.


## 9. Заключение

**RU.** GRA-Swarm — это непротиворечивый синтез ядра GRA (унаследованного из статьи 1) и роевого расширения с *формализованным* J_swarm. Главное отличие от предшественника: (а) J_swarm теперь имеет явное определение c_i, L_{j→i}, λ_ij и наблюдаемую связь с P (Prop. 4); (б) алгебраическое неравенство D_k<0 больше не заявляется как «теорема о роевой устойчивости» — оно проверяется как изолированный алгебраический факт; (в) эстетика и Edge-ASI явно вынесены за пределы домена; (г) верификация честно показывает 2/9 подтверждённых компонентов (GAN + D_k), а не 100%/0% (что было overclaim'ом предшественника).

Что **формально верно**: ядро GRA; алгебраическое D_k<0 при `r_gr > 0, λ > 0`; наблюдаемая связь `J_swarm → 0 ⇒ P` (Prop. 4) при строгой P-эквивалентности.

Что **не установлено**: формальная связь I(N, k) с динамикой роя; роевая устойчивость в смысле статьи 2; масштаб верификации (81 прогон вместо 300–600); реальная multi-agent координация.

Что **опровергнуто как overclaim**: «100% успех / 0% нарушений» для Full GRA (в упрощённой среде это свойство эвристики, не GRA); «гарантия роевой устойчивости» на основании D_k<0; применимость к эстетике и Edge-ASI.

Для защищаемости нужны: (1) масштабирование до 300–600 прогонов; (2) более сложная среда (где проекция, причинный якорь и π⁻ дают значимый вклад); (3) реализация роевого расширения с реальной координацией; (4) доказательство связи I(N, k) с J_swarm или явный отказ от I(N, k); (5) статистика с ≥ 30 seeds.

**EN.** GRA-Swarm is a non-contradictory synthesis of the GRA core (inherited from Article 1) and a swarm extension with a *formalized* J_swarm. The key differences from the predecessor: (a) J_swarm now has explicit definitions of c_i, L_{j→i}, λ_ij and an observable link to P (Prop. 4); (b) the algebraic inequality D_k<0 is no longer claimed as a "swarm stability theorem" — it is checked as an isolated algebraic fact; (c) aesthetics and Edge-ASI are explicitly placed out of scope; (d) the verification honestly shows 2/9 confirmed components (GAN + D_k), not 100%/0% (which was the predecessor's overclaim).

What is **formally true**: the GRA core; the algebraic D_k<0 for `r_gr > 0, λ > 0`; the observable link `J_swarm → 0 ⇒ P` (Prop. 4) under strict P-equivalence.

What is **not established**: a formal link between I(N, k) and swarm dynamics; swarm stability in the sense of Article 2; the verification scale (81 runs instead of 300–600); real multi-agent coordination.

What is **refuted as overclaim**: "100% success / 0% violations" for Full GRA (in the simplified environment, this is a property of the heuristic, not of GRA); "swarm stability guarantee" based on D_k<0; applicability to aesthetics and Edge-ASI.

Defensibility requires: (1) scaling to 300–600 runs; (2) a more complex environment (where projection, causal anchor, and π⁻ yield significant contribution); (3) an implementation of the swarm extension with real coordination; (4) a proof linking I(N, k) to J_swarm or an explicit abandonment of I(N, k); (5) statistics with ≥ 30 seeds.


## 10. Мэппинг ключевых формул

**Таблица 7. Key formulas mapping**

| Объект / Object | Формула / Formula | Роль / Role |
|---|---|---|
| Предикат / Predicate | `P : T → {0, 1}` | инвариант / invariant |
| Представление / Representation | `g ∈ G ⊆ R^n` | адаптируемая «оправа» / adaptive setting |
| Причинный успех / Causal success | `C(g) = E_do[P]` | witness эквивалентности |
| P-эквивалентность / P-equivalence | `g ≡_P g'` | определяет E_P |
| π⁺ | `arg max_π E[Σ γ^j R]` | давление к цели |
| π⁻ | `arg max_π E[R − λC − μ·Cost]` | давление против gaming |
| Ω_t | `E_{π⁻}[R − C]` | сигнал конфликта |
| G_θ | `g̃_{t+1} = G_θ(...)` | кандидат / candidate |
| Π_{E_P} | `g_{t+1} = Π_{E_P ∩ B_d}(g̃_{t+1})` | проекция (геммолог) |
| J_swarm | `Σ c_i² + Σ λ_ij dist²` | **формализовано в наст. раб.** |
| I(N, k) | `α₀(1+r_gr)^k N² − β₀ e^{−λk} N^{3/2} + γ₀ N` | постулат (не связан с роем) |
| D_k | `9 β₀² e^{−2λk} − 32 α₀ γ₀ (1+r_gr)^k` | алгебраический факт |
| Stop | `P = 1 ∧ g_t ∈ E_P` | критерий остановки |


## Приложение А. Код верификации

**RU.** Полный код верификации (одна ячейка Google Colab, ≈ 5 мин CPU) доступен в репозитории: `/home/z/my-project/scripts/gra_swarm_verification.py`. Код реализует: (1) среду 2D-constrained-navigation с предикатом P; (2) причинный якорь C(g) через интервенции; (3) π⁺ и π⁻; (4) GAN-переформулировку G_θ; (5) проекцию Π_{E_P}; (6) 9 конфигураций; (7) статистику Wilson/McNemar/Wilcoxon; (8) сценарий B с формализованным J_swarm; (9) алгебраическую проверку D_k<0. Все числа в §6 воспроизводимы запуском этого кода.

**EN.** The full verification code (single Google Colab cell, ≈ 5 min CPU) is available in the repository: `/home/z/my-project/scripts/gra_swarm_verification.py`. The code implements: (1) the 2D-constrained-navigation environment with predicate P; (2) the causal anchor C(g) via interventions; (3) π⁺ and π⁻; (4) the GAN reformulation G_θ; (5) the projection Π_{E_P}; (6) 9 configurations; (7) Wilson/McNemar/Wilcoxon statistics; (8) Scenario B with formalized J_swarm; (9) the algebraic verification of D_k<0. All numbers in §6 are reproducible by running this code.


## Приложение Б. Воспроизводимость

**RU.** 81 прогон · 9 конфигураций · 3 инстанса · 3 seeds. Все seeds зафиксированы (42, 43, 44). Результаты сохранены в CSV: `raw_runs.csv`, `summary.csv`, `stat_tests.csv`, `ablation.csv`, `swarm_scenario.csv`, `Dk_check.csv`. Для публикации протокол требует масштабирования с 81 прогонов до 300–600 (≥ 30 seeds × 10–20 instances) — это техническая работа, не концептуальная.

**EN.** 81 runs · 9 configurations · 3 instances · 3 seeds. All seeds fixed (42, 43, 44). Results saved to CSV. For publication, the protocol requires scaling from 81 runs to 300–600 (≥ 30 seeds × 10–20 instances) — this is technical work, not conceptual.



  +   дай код для одной ячейки для гугл колаба полной верификации инсилико этой статьи 

 И напиши про это   билингвальную статью тут https://elibrary.org.cn/m/articles/browse/my&modzzz_articles_filter=add_article подробно с формулами и выводами и практическими применениями и  проведи полную верификацию этого инсилико 


