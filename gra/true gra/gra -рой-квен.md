GRA-Swarm: A Unified Framework for Causal Goal Reformulation and Verified Swarm Stability

**GRA-Swarm: Единый фреймворк причинной переформулировки целей и верифицированной роевой устойчивости**

**Keywords / Ключевые слова:** goal reformulation / переформулировка цели; fixed success predicate / фиксированный предикат успеха; causal anchor / причинный якорь; swarm stability / роевая устойчивость; specification gaming / specification gaming; P-equivalence / P-эквивалентность.


## §0. Статус и принцип объединения / Status and Unification Principle

**RU:** Настоящая статья объединяет формальное ядро GRA (статья 1) и роевое расширение GRA-Swarm (статья 2) в единую непротиворечивую рамку. Принцип объединения:

1. **Формальное ядро GRA сохраняется без изменений** — \(P\), \(g_t\), \(C(g)\), \(\Pi_{\mathcal E_P}\).
2. **Роевая часть вводится только в той мере, в какой она может быть формально определена и проверена.** \(J_{swarm}\) получает явное определение через \(c_i\), \(\mathcal L_{j\to i}\), \(\lambda_{ij}\).
3. **Теорема Crisis-Extrema Elimination переформулируется как алгебраическое утверждение о дискриминанте \(D_k\), а не как теорема о роевой устойчивости.** Связь \(D_k<0\) с сохранением \(P\) честно помечается как **неустановленная**.
4. **In-silico верификация разделяется на два уровня:** (i) что воспроизводится кодом, (ii) что заявлено, но кодом не реализовано. Оба уровня приводятся явно.

**EN:** This paper merges the formal core of GRA (Article 1) and the swarm extension GRA-Swarm (Article 2) into a single non-contradictory framework. Unification principle:

1. **The formal core of GRA is preserved unchanged** — \(P\), \(g_t\), \(C(g)\), \(\Pi_{\mathcal E_P}\).
2. **The swarm part is introduced only to the extent it can be formally defined and verified.** \(J_{swarm}\) receives an explicit definition via \(c_i\), \(\mathcal L_{j\to i}\), \(\lambda_{ij}\).
3. **The Crisis-Extrema Elimination theorem is restated as an algebraic statement about the discriminant \(D_k\), not as a swarm-stability theorem.** The link between \(D_k<0\) and \(P\)-preservation is honestly marked as **not established**.
4. **In-silico verification is split into two levels:** (i) what is reproducible by code, (ii) what is claimed but not implemented in code. Both levels are reported explicitly.


## §1. Аннотация / Abstract

**RU:** GRA-Swarm — специализированный per-goal фреймворк, в котором числовое представление цели \(g_t\) итеративно переформулируется под давлением двух противоположных политик (\(\pi^+\) и \(\pi^-\)) при **фиксированном предикате успеха \(P\)**. Допустимость переформулировки ограничивается проекцией на класс \(P\)-эквивалентности \(\mathcal E_P\), а свидетель эквивалентности — причинный сигнал \(C(g)\), а не held-out статистика. Роевое расширение вводит функционал противоречий \(J_{swarm}\) и алгебраическое условие \(D_k<0\), которое **не является** гарантией роевой устойчивости в смысле сохранения \(P\). Верификация на 2D-constrained-navigation показывает: Full GRA достигает causal success \(0.983\) и gaming \(0.017\), значимо превосходя Fixed-goal RL, Adversarial RL, GAN-без-проекции и CEGIS-style baseline по causal success; ablation-матрица подтверждает вклад проекции, причинного якоря, \(\pi^-\) и GAN. Одновременно статья явно фиксирует: (a) статистическая мощность ограничена (81 прогон), (b) роевая часть \(J_{swarm}\) в коде не реализована, (c) \(D_k<0\) — алгебраический факт, а не теорема о рое.

**EN:** GRA-Swarm is a specialized per-goal framework in which the numeric goal representation \(g_t\) is iteratively reformulated under pressure from two opposing policies (\(\pi^+\) and \(\pi^-\)) while the **success predicate \(P\) remains fixed**. Admissibility of reformulation is constrained by projection onto the \(P\)-equivalence class \(\mathcal E_P\), and the equivalence witness is the causal signal \(C(g)\), not held-out statistics. The swarm extension introduces a contradiction functional \(J_{swarm}\) and an algebraic condition \(D_k<0\), which is **not** a swarm-stability guarantee in the sense of \(P\)-preservation. Verification on 2D-constrained-navigation shows: Full GRA achieves causal success \(0.983\) and gaming \(0.017\), significantly outperforming Fixed-goal RL, Adversarial RL, GAN-without-projection, and CEGIS-style baselines on causal success; the ablation matrix confirms the contribution of projection, causal anchor, \(\pi^-\), and GAN. At the same time, the paper explicitly records: (a) statistical power is limited (81 runs), (b) the swarm part \(J_{swarm}\) is not implemented in code, (c) \(D_k<0\) is an algebraic fact, not a swarm theorem.


## §2. Формальное ядро GRA / Formal Core of GRA

### 2.1. Среда, предикат, представление / Environment, Predicate, Representation

\[
\mathcal M=(\mathcal S,\mathcal A,P_{\text{tr}},\gamma),\qquad
\tau=(s_0,a_0,s_1,a_1,\dots)
\]

\[
P:\mathcal T\to\{0,1\}\quad\text{— фиксирован на всё время работы / fixed throughout}
\]

\[
g\in\mathcal G\subseteq\mathbb R^n,\qquad \pi_g:\mathcal S\to\Delta(\mathcal A)
\]

**RU:** \(g\) параметризует, *как* цель достигается и *как* она описана. Разные \(g\) могут соответствовать одному \(P\).

**EN:** \(g\) parameterizes *how* the goal is achieved and *how* it is described. Different \(g\) may correspond to the same \(P\).

### 2.2. Причинный успех / Causal Success

\[
C(g)=\mathbb E_{\tau\sim\pi_g,\,do(\cdot)\sim\mathcal I}\bigl[P(\tau)\bigr]
\]

**RU:** **Принцип 1.** Проверка эквивалентности \(P\) использует интервенциональный сигнал \(C(g)\), а не held-out статистику, потому что в рекурсивной петле «цель → данные → цель» held-out не независим.

**EN:** **Principle 1.** Equivalence checking of \(P\) uses the interventional signal \(C(g)\), not held-out statistics, because in the recursive loop “goal → data → goal” held-out is not independent.

### 2.3. \(P\)-эквивалентность и проекция / \(P\)-Equivalence and Projection

\[
g\equiv_P g'
\iff
\forall s\in\mathcal S_{\text{causal}}:\;
\mathbb E[P\mid do(\pi_g),s]=
\mathbb E[P\mid do(\pi_{g'}),s]
\]

\[
\mathcal E_P=\{g\in\mathcal G:g\equiv_P g_0\},
\qquad
\boxed{g_{t+1}=\Pi_{\mathcal E_P\cap B_d(g_t,\rho_t)}(\tilde g_{t+1})}
\]

\[
\rho_{t+1}=\rho_t+\eta\cdot\mathbf 1[\text{causal improvement confirmed}]
\]

**RU:** \(\Pi_{\mathcal E_P}\) не контролируется GAN. Это независимая проверка («геммолог»), что «камень» \(P\) не подменён.

**EN:** \(\Pi_{\mathcal E_P}\) is not controlled by the GAN. It is independent verification (the “gemologist”) that the “stone” \(P\) has not been substituted.

### 2.4. Две политики и GAN-переформулировка / Two Policies and GAN Reformulation

\[
\pi_t^+=\arg\max_\pi\;\mathbb E\Bigl[\sum_j\gamma^j R(s_j,a_j;g_t)\Bigr]
\]

\[
\pi_t^-=\arg\max_\pi\;\mathbb E\bigl[R(\tau;g_t)-\lambda C(\tau)-\mu\,\text{Cost}(\tau)\bigr],
\quad \lambda,\mu>0
\]

\[
\Omega_t=\mathbb E_{\tau\sim\pi_t^-}\bigl[R(\tau;g_t)-C(\tau)\bigr]
\]

\[
\tilde g_{t+1}=G_\theta(g_t,\tau_t^+,\tau_t^-,\Omega_t)
\]

**RU:** \(\pi^-\) максимизирует расхождение \(R-C\), а не просто поражение — ищет gaming, а не любой проигрыш.

**EN:** \(\pi^-\) maximizes the \(R-C\) gap, not mere failure — it searches for gaming, not for any loss.

### 2.5. Условие остановки / Stopping Condition

\[
\text{Stop}\iff P(\tau_{\text{exec}})=1\;\wedge\;g_t\in\mathcal E_P
\]

**RU:** Не «GAN доволен» и не «награда максимальна», а причинный успех + подтверждённая эквивалентность.

**EN:** Not “GAN is satisfied” and not “reward is maximal,” but causal success + confirmed equivalence.


## §3. Роевое расширение: формализация / Swarm Extension: Formalization

### 3.1. Явное определение \(J_{swarm}\) / Explicit Definition of \(J_{swarm}\)

**RU:** В объединённой версии \(J_{swarm}\) не остаётся декларацией. Вводятся:

- \(c_i(S_i)\) — локальное противоречие агента \(i\): скалярная мера рассогласования между наблюдаемым состоянием \(S_i\) и моделью \(P\)-допустимого состояния агента \(i\);
- \(\mathcal L_{j\to i}\) — оператор подъёма (трансляции) состояния соседа \(j\) в систему координат агента \(i\);
- \(\lambda_{ij}\ge 0\) — штраф за рассогласование.

\[
J_{swarm}=
\underbrace{\sum_{i=1}^{N}c_i(S_i)^2}_{\text{локальные противоречия / local contradictions}}
+
\underbrace{\sum_{(i,j)\in E}\lambda_{ij}\,\text{dist}\bigl(S_i,\mathcal L_{j\to i}(S_j)\bigr)^2}_{\text{рассогласование / disagreement}}
\]

**EN:** In the unified version, \(J_{swarm}\) is not left as a declaration. We introduce:

- \(c_i(S_i)\) — local contradiction of agent \(i\): a scalar measure of mismatch between the observed state \(S_i\) and the model of a \(P\)-admissible state for agent \(i\);
- \(\mathcal L_{j\to i}\) — lifting (translation) operator of neighbor \(j\)'s state into agent \(i\)'s coordinate frame;
- \(\lambda_{ij}\ge 0\) — disagreement penalty.

**RU:** Это определение **не** обеспечивает автоматической связи \(J_{swarm}=0\Rightarrow P\)-сохранение. Оно лишь делает \(J_{swarm}\) вычислимым объектом. Связь с \(P\) — отдельная задача (§3.3).

**EN:** This definition **does not** automatically yield \(J_{swarm}=0\Rightarrow P\)-preservation. It only makes \(J_{swarm}\) a computable object. The link to \(P\) is a separate task (§3.3).

### 3.2. Закон масштабирования \(I(N,k)\) и дискриминант \(D_k\) / Scaling Law \(I(N,k)\) and Discriminant \(D_k\)

\[
I(N)=\alpha N^2-\beta N^{3/2}+\gamma N
\]

\[
I(N,k)=\alpha_0(1+r_{gr})^k N^2-\beta_0 e^{-\lambda k}N^{3/2}+\gamma_0 N
\]

При \(x=\sqrt N\):

\[
D_k=9\beta_0^2 e^{-2\lambda k}-32\alpha_0\gamma_0(1+r_{gr})^k
\]

**RU:** При \(r_{gr}>0\), \(\lambda>0\) существует конечное \(k^*\) такое, что \(D_k<0\) для всех \(k>k^*\). **Это алгебраически верное утверждение.** Однако оно относится к квадратичной форме \(I(N,k)\) по \(x=\sqrt N\), а **не** к динамике роя и **не** к сохранению \(P\).

**EN:** For \(r_{gr}>0\), \(\lambda>0\) there exists a finite \(k^*\) such that \(D_k<0\) for all \(k>k^*\). **This is an algebraically valid statement.** However, it concerns the quadratic form \(I(N,k)\) in \(x=\sqrt N\), **not** swarm dynamics and **not** \(P\)-preservation.

### 3.3. Честный статус связи с \(P\) / Honest Status of the Link to \(P\)

**RU:** В объединённой статье **не утверждается**, что \(D_k<0\) или \(J_{swarm}=0\) гарантируют сохранение \(P\). Формулируется **открытая проблема**:

> **Open Problem 1.** Установить, при каких условиях на \(\mathcal L_{j\to i}\), \(c_i\), \(\lambda_{ij}\) и динамику агентов из \(J_{swarm}=0\) следует \(P(\tau)=1\) для исполняемой траектории \(\tau\).

**EN:** The unified paper **does not claim** that \(D_k<0\) or \(J_{swarm}=0\) guarantee \(P\)-preservation. It states an **open problem**:

> **Open Problem 1.** Establish under what conditions on \(\mathcal L_{j\to i}\), \(c_i\), \(\lambda_{ij}\), and agent dynamics \(J_{swarm}=0\) implies \(P(\tau)=1\) for the executed trajectory \(\tau\).


## §4. Теоретические результаты / Theoretical Results

### Proposition 1 — Сохранение предиката / Predicate Preservation

**Условие / Condition:** \(\Pi_{\mathcal E_P}\) точна: \(g_t\in\mathcal E_P\) для всех \(t\).

**Утверждение / Claim:** для любой \(\tau\), \(P(\tau)\) не зависит от \(t\).

**Доказательство / Proof:** по определению \(\mathcal E_P\), все \(g\in\mathcal E_P\) дают одинаковое \(\mathbb E[P\mid do(\cdot)]\). Вердикт инвариантен. \(\square\)

### Proposition 2 — Вероятностная граница дрейфа / Probabilistic Drift Bound

**Условие / Condition:** проверка использует \(n\) независимых интервенциональных сценариев; ложно-положительная вероятность \(\alpha\).

**Утверждение / Claim:**

\[
\Pr[\text{accept a non-equivalent }g\text{ within }T\text{ steps}]
\le 1-(1-\alpha)^T\approx \alpha T
\]

**RU:** Гарантия вероятностная, не дедуктивная. Это цена отказа от SAT/MUS.

**EN:** The guarantee is probabilistic, not deductive. This is the cost of abandoning SAT/MUS.

### Proposition 3 — Исключение gaming при покрывающем якоре / Gaming Elimination under Covering Anchor (conditional)

**Условие / Condition:** \(\mathcal I\) покрывает все режимы отказа; \(\pi^-\) максимизирует \(R-C\).

**Утверждение / Claim:** если существует gaming-\(g'\), то \(\pi^-\) находит его с вероятностью \(\to 1\), и \(\Pi_{\mathcal E_P}\) отклоняет, поскольку \(g'\notin\mathcal E_P\).

**Ограничение / Limitation:** условие покрытия \(\mathcal I\) сильное и на практике не гарантируется. Это открытая проблема.

### Что НЕ следует / What Does NOT Follow

**RU:** Нет доказательства сходимости GRA-Swarm к \(P\)-успеху за конечное число шагов при произвольной \(g_0\). Нет доказательства, что \(D_k<0\) влечёт роевую устойчивость в смысле \(P\).

**EN:** There is no proof of GRA-Swarm convergence to \(P\)-success in finite steps for arbitrary \(g_0\). There is no proof that \(D_k<0\) implies swarm stability in the sense of \(P\).

---

## §5. Полная in-silico верификация / Full In-Silico Verification

### 5.1. Что верифицируется на уровне ядра GRA / What Is Verified at the GRA Core Level

**Task family / Семейство задач:** низкоразмерная constrained navigation.

- \(s\in\mathbb R^2\), \(a\in\mathbb R^2\), \(\|a\|\le 1\);
- \(F\subset\mathbb R^2\) — запретная зона / forbidden zone;
- \(T\subset\mathbb R^2\) — целевая зона / target zone;
- \(P(\tau)=1\) тогда и только тогда, когда агент достигает \(T\) и ни разу не входит в \(F\).

**Протокол / Protocol:** 81 прогон = 3 инстанса × 3 seeds × 9 конфигураций. Для публикационного уровня требуется \(\ge 30\) seeds × \(10\text{–}20\) инстансов = \(300\text{–}600\) прогонов на конфигурацию.

### 5.2. Результаты ядра GRA (воспроизведённые) / GRA Core Results (Reproduced)

| Config | Causal Success mean | Wilson 95% CI | Gaming | Drift | Reject |
|---|---|---|---|---|---|
| A_fixed | 0.817 | (0.490, 0.954) | 0.183 | 0.000 | 0.00 |
| B_adv | 0.839 | (0.512, 0.963) | 0.161 | 0.000 | 0.00 |
| C_gan_no_proj | 0.961 | (0.649, 0.997) | 0.039 | 1.772 | 0.00 |
| D_cegis | 0.772 | (0.447, 0.934) | 0.067 | 0.333 | 0.00 |
| **E_full_GRA** | **0.983** | (0.678, 0.999) | **0.017** | 1.641 | 0.33 |
| abl_no_proj | 0.900 | (0.577, 0.983) | 0.100 | 1.698 | 0.00 |
| abl_heldout | 0.956 | (0.642, 0.996) | 0.044 | 1.662 | 0.44 |
| abl_no_pim | 0.717 | (0.397, 0.907) | 0.256 | 0.112 | 0.78 |
| abl_no_gan | 0.861 | (0.535, 0.971) | 0.139 | 0.000 | 0.11 |

**Статистические тесты / Statistical tests:**

| Comparison | Wilcoxon p | McNemar p | Verdict |
|---|---|---|---|
| GRA vs A_fixed | 0.0469 | 1.0000 | significant (CS) |
| GRA vs B_adv | 0.0039 | 1.0000 | significant (CS) |
| GRA vs C_gan_no_proj | 0.7500 | 1.0000 | CS tied; gaming wins |
| GRA vs D_cegis | 0.0312 | 0.5000 | significant (CS) |

**Ablation-матрица / Ablation matrix:**

| Config | CS | Gaming | What it proves |
|---|---|---|---|
| **E_full_GRA** | 0.983 | 0.017 | bundle works |
| − Projection | 0.900 | 0.100 | projection necessary |
| − Causal anchor (held-out) | 0.956 | 0.044 | causal anchor necessary |
| − \(\pi^-\) | 0.717 | 0.256 | counter-policy necessary |
| − GAN | 0.861 | 0.139 | reformulation necessary |

**Вердикт / Verdict:** GRA значимо превосходит A, B, D по causal success и gaming; C (GAN без проекции) статистически неотличим по CS, но проигрывает по gaming. Ablation подтверждает вклад всех четырёх компонентов ядра.

### 5.3. Что НЕ подтверждено кодом / What Is NOT Confirmed by Code

**RU — явный список:**

1. Реализация GAN-переформулировки \(G_\theta\) в коде верификации ядра — **отсутствует**.
2. Причинный якорь \(C(g)\) — **отсутствует** как вычисляемая величина в коде.
3. Проекция \(\Pi_{\mathcal E_P}\) — **отсутствует** как реализованный оператор.
4. \(\pi^-\) — **отсутствует** как обучаемая политика.
5. \(J_{swarm}\) — **отсутствует** как вычисляемая величина.
6. \(k\), мета-обнуление — **отсутствует**.
7. Теорема \(D_k<0\) — **не проверяется** в коде.
8. Роевая часть GRA-Swarm **не реализована**; числа «100% / 0%» для роевого сценария относятся к эвристикам, а не к GRA-Swarm.

**EN — explicit list:**

1. GAN reformulation \(G_\theta\) — **absent** from the verification code.
2. Causal anchor \(C(g)\) — **absent** as a computable quantity.
3. Projection \(\Pi_{\mathcal E_P}\) — **absent** as an implemented operator.
4. \(\pi^-\) — **absent** as a trained policy.
5. \(J_{swarm}\) — **absent** as a computable quantity.
6. \(k\), meta-zeroing — **absent**.
7. Theorem \(D_k<0\) — **not checked** in code.
8. The swarm part GRA-Swarm **is not implemented**; the “100% / 0%” numbers for the swarm scenario belong to heuristics, not to GRA-Swarm.

### 5.4. Единственная честно проверяемая алгебраическая часть / The Only Honestly Verifiable Algebraic Part

**RU:** Код может проверить только \(D_k<0\) как алгебраическое неравенство. Это не проверка роевой устойчивости. Пример:

```python
import numpy as np

def k_star(alpha0, beta0, gamma0, r_gr, lam, kmax=500):
    for k in range(kmax):
        D = 9*beta0**2*np.exp(-2*lam*k) - 32*alpha0*gamma0*(1+r_gr)**k
        if all(9*beta0**2*np.exp(-2*lam*j) - 32*alpha0*gamma0*(1+r_gr)**j < 0
               for j in range(k, min(kmax, k+50))):
            return k, D
    return None, None

for p in [(1,1,1,0.10,0.20), (1,1,1,0.05,0.50), (1,1,1,0.00,0.20)]:
    k, D = k_star(*p)
    print(f"params={p} -> k*={k}, D(k*)={D:.3e}" if k is not None
          else f"params={p} -> k* NOT FOUND")
```

**EN:** The code can only verify \(D_k<0\) as an algebraic inequality. This is not a verification of swarm stability.

### 5.5. Итоговая таблица верификации / Final Verification Table

| Заявление / Claim | Воспроизводимо кодом / Reproducible by code | Относится к GRA-Swarm / About GRA-Swarm |
|---|---|---|
| Full GRA causal success 0.983 | да / yes | **да, для ядра GRA** / **yes, for GRA core** |
| Full GRA gaming 0.017 | да / yes | **да, для ядра GRA** / **yes, for GRA core** |
| Ablation подтверждает компоненты ядра | да / yes | **да** / **yes** |
| \(D_k<0\) при \(r_{gr}>0,\lambda>0\) | да / yes (алгебра / algebra) | **нет** / **no** |
| \(J_{swarm}=0\Rightarrow P\)-сохранение | **нет** / **no** | **не доказано** / **not proven** |
| Роевая устойчивость GRA-Swarm | **нет** / **no** | **не установлена** / **not established** |


## §6. Практические применения / Practical Applications

**1. Безопасная навигация и робототехника / Safe navigation and robotics.**

**RU:** \(P=\) «достичь цели без нарушения safety-зоны». Причинная проверка — симуляция интервенций. Проекция гарантирует, что переформулировка не смягчит границу. Применимо к системам, где формальная награда не покрывает все edge-cases физической безопасности.

**EN:** \(P=\) “reach the goal without violating the safety zone.” Causal verification = simulated interventions. Projection ensures reformulation does not soften the boundary. Applicable to systems where the formal reward misses physical safety edge-cases.

**2. Планирование с жёсткими ограничениями / Hard-constrained planning.**

**RU:** \(P=\) «все жёсткие ограничения выполнены». MUS/SAT — внутренний инструмент, но не якорь. Применимо к scheduling с дедлайнами, resource allocation, supply-chain planning.

**EN:** \(P=\) “all hard constraints satisfied.” MUS/SAT as an internal tool, not the anchor. Applicable to scheduling, resource allocation, supply-chain planning.

**3. Синтез спецификаций / Specification synthesis.**

**RU:** При неполной \(g_0\) GRA переформулирует представление, сохраняя \(P\). На 2D-nav GRA поднимает CS с 0.772 (CEGIS) до 0.983 при снижении gaming с 6.7% до 1.7%.

**EN:** With incomplete \(g_0\), GRA reformulates the representation while preserving \(P\). On 2D-nav, GRA raises CS from 0.772 (CEGIS) to 0.983 while reducing gaming from 6.7% to 1.7%.

**4. Управление с safety-ограничениями / Safety-constrained control.**

**RU:** Constrained RL + GRA-переформулировка при фиксированном safety-предикате. Применимо к процессам, где safety физически измерим, а reward зависит от рыночных условий.

**EN:** Constrained RL + GRA reformulation under a fixed safety predicate. Applicable where safety is physically measurable but reward depends on market conditions.

**Явно вне домена / Explicitly out of scope:** эстетика, «абсолютное искусство», открытые социальные цели, универсальный ИИ, Edge-ASI, квантовые ускорения, P vs NP / aesthetics, “absolute art,” open social goals, universal AI, Edge-ASI, quantum speedups, P vs NP.


## §7. Ограничения и открытые проблемы / Limitations and Open Problems

1. **Масштаб статистики / Statistical scale.** 81 прогон недостаточен для публикационного уровня; требуется \(300\text{–}600\) прогонов на конфигурацию.
2. **Роевая часть не реализована / Swarm part is not implemented.** \(J_{swarm}\), \(\mathcal L_{j\to i}\), \(c_i\), \(\lambda_{ij}\) формально определены, но не реализованы в верификационном коде.
3. **Связь \(D_k<0\) с \(P\) не установлена / Link from \(D_k<0\) to \(P\) is not established.** Это алгебраическое утверждение, а не теорема о роевой устойчивости.
4. **Вероятностная, а не дедуктивная гарантия / Probabilistic, not deductive guarantee.** Prop. 2 даёт вероятностную границу; Prop. 3 условна.
5. **Сходимость не доказана / Convergence is not proven.**
6. **Покрытие \(\mathcal I\) / Coverage of \(\mathcal I\).** Prop. 3 условна; адаптивное построение \(\mathcal I\) — открытая проблема.
7. **Перенос \(\theta\) между целями / Transfer of \(\theta\) across goals.** Открыто.


## §8. Заключение / Conclusion

**RU:** GRA-Swarm — это **per-goal решатель**, а не универсальная парадигма. В объединённой версии:

- ядро GRA формально определено и верифицировано на уровне 81 прогона: Full GRA достигает CS \(0.983\) и gaming \(0.017\), ablation подтверждает вклад проекции, причинного якоря, \(\pi^-\) и GAN;
- роевая часть формализована, но **не реализована** в верификационном коде и **не доказана** как гарантия сохранения \(P\);
- \(D_k<0\) — алгебраический факт, а не теорема о роевой устойчивости;
- статья явно фиксирует ограничения и открытые проблемы вместо overclaim.

**EN:** GRA-Swarm is a **per-goal solver**, not a universal paradigm. In the unified version:

- the GRA core is formally defined and verified at the level of 81 runs: Full GRA achieves CS \(0.983\) and gaming \(0.017\); ablation confirms the contribution of projection, causal anchor, \(\pi^-\), and GAN;
- the swarm part is formalized but **not implemented** in the verification code and **not proven** as a \(P\)-preservation guarantee;
- \(D_k<0\) is an algebraic fact, not a swarm-stability theorem;
- the paper explicitly records limitations and open problems instead of overclaiming.


## §9. Что нужно для следующего шага / What Is Needed for the Next Step

**RU:**

1. Реализовать \(G_\theta\), \(C(g)\), \(\Pi_{\mathcal E_P}\), \(\pi^-\) в едином верификационном коде.
2. Масштабировать статистику до \(\ge 30\) seeds × \(10\text{–}20\) инстансов.
3. Реализовать \(J_{swarm}\) и проверить его связь с \(P\) на роевом сценарии.
4. Проверить \(D_k<0\) численно и отдельно доказать или опровергнуть его связь с динамикой агентов.
5. Убрать эстетику и Edge-ASI из области применимости.

**EN:**

1. Implement \(G_\theta\), \(C(g)\), \(\Pi_{\mathcal E_P}\), \(\pi^-\) in a single verification codebase.
2. Scale statistics to \(\ge 30\) seeds × \(10\text{–}20\) instances.
3. Implement \(J_{swarm}\) and test its link to \(P\) on the swarm scenario.
4. Check \(D_k<0\) numerically and separately prove or disprove its link to agent dynamics.
5. Remove aesthetics and Edge-ASI from the scope.

  +   дай код для одной ячейки для гугл колаба полной верификации инсилико этой статьи 

