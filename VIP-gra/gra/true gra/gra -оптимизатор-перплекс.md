GRA: Goal Reformulation under a Fixed Success Predicate with Causal Anchoring  
# GRA: Переформулировка цели при фиксированном предикате успеха с причинным якорем

## Abstract / Аннотация

**EN:** GRA is a per-goal optimization framework in which the numerical representation of a goal \(g_t\) may be iteratively reformulated, while the external success predicate \(P\) remains fixed. Candidate reformulations are generated under the pressure of two opposing policies: a achievement policy and a refutation policy. Admissible reformulations must remain within the \(P\)-equivalence class \(\mathcal{E}_P\), verified through causal interventions rather than merely statistical validation. GRA therefore aims to reduce specification gaming: the system may change *how* a goal is pursued, but not *what counts as success*.

**RU:** GRA — это per-goal-оптимизатор, в котором числовое представление цели \(g_t\) может итеративно переформулироваться, тогда как внешний предикат успеха \(P\) остаётся неизменным. Кандидаты на переформулировку возникают под давлением двух противоположных политик: политики достижения и политики опровержения. Допустимые переформулировки должны оставаться в классе \(P\)-эквивалентности \(\mathcal{E}_P\), проверяемом через причинные интервенции, а не только через статистическую валидацию. Таким образом, GRA направлена на подавление specification gaming: система может менять *способ* достижения цели, но не *само определение успеха*.

## 1. Problem / Постановка задачи

**EN:** Standard goal-driven systems face a dilemma. If the goal is fixed, an incomplete or poorly specified goal may cause stagnation or specification gaming. If the goal is freely revised, the system may redefine success to match its own failure. GRA takes an intermediate position: the representation of the goal changes, but the success predicate does not.

**RU:** Обычные системы, работающие с целями, сталкиваются с дилеммой. Если цель жёстко фиксирована, её неполнота может привести к застреванию или к specification gaming. Если цель можно свободно менять, система способна переопределить успех под собственную неудачу. GRA занимает промежуточную позицию: представление цели меняется, но предикат успеха не меняется.

## 2. Formal model / Формальная модель

**EN:** Let the environment be a Markov process \(\mathcal{M}=(\mathcal{S},\mathcal{A},P_{\mathrm{tr}},\gamma)\). A trajectory is \(\tau=(s_0,a_0,s_1,\dots)\). The success predicate is:

\[
P:\mathcal{T}\to\{0,1\},
\]

where \(P(\tau)=1\) denotes externally defined success. The goal representation is:

\[
g\in\mathcal{G}\subseteq\mathbb{R}^n.
\]

**RU:** Пусть среда задана как марковский процесс \(\mathcal{M}=(\mathcal{S},\mathcal{A},P_{\mathrm{tr}},\gamma)\). Траектория — это \(\tau=(s_0,a_0,s_1,\dots)\). Предикат успеха:

\[
P:\mathcal{T}\to\{0,1\},
\]

где \(P(\tau)=1\) означает внешний критерий успеха. Представление цели:

\[
g\in\mathcal{G}\subseteq\mathbb{R}^n.
\]

### Causal success / Причинный успех

**EN:** Instead of relying only on held-out data, GRA evaluates a representation through interventions:

\[
C(g)=\mathbb{E}_{\tau\sim\pi_g,\;do(\cdot)\sim\mathcal{I}}\left[P(\tau)\right].
\]

**RU:** Вместо опоры только на отложенные данные GRA оценивает представление через интервенции:

\[
C(g)=\mathbb{E}_{\tau\sim\pi_g,\;do(\cdot)\sim\mathcal{I}}\left[P(\tau)\right].
\]

### \(P\)-equivalence / \(P\)-эквивалентность

**EN:** Two representations are \(P\)-equivalent if they produce the same causal success under the intervention distribution:

\[
g\equiv_P g'
\iff
\mathbb{E}[P\mid do(\pi_g),s]
=
\mathbb{E}[P\mid do(\pi_{g'}),s].
\]

The admissible set is:

\[
\mathcal{E}_P=\{g\in\mathcal{G}:g\equiv_P g_0\}.
\]

**RU:** Два представления \(P\)-эквивалентны, если они дают одинаковый причинный успех при распределении интервенций:

\[
g\equiv_P g'
\iff
\mathbb{E}[P\mid do(\pi_g),s]
=
\mathbb{E}[P\mid do(\pi_{g'}),s].
\]

Допустимое множество:

\[
\mathcal{E}_P=\{g\in\mathcal{G}:g\equiv_P g_0\}.
\]

### Reformulation rule / Правило переформулировки

**EN:** A generator proposes a candidate \(\tilde g_{t+1}\), but the accepted goal is projected back onto the admissible class:

\[
g_{t+1}=\Pi_{\mathcal{E}_P}(\tilde g_{t+1}).
\]

**RU:** Генератор предлагает кандидата \(\tilde g_{t+1}\), но принимается только его проекция на допустимый класс:

\[
g_{t+1}=\Pi_{\mathcal{E}_P}(\tilde g_{t+1}).
\]

## 3. In-silico verification / In-silico верификация

**EN:** A 10×10 navigation environment was used. The agent starts at \((0,0)\), must reach \((9,9)\), and must avoid the forbidden region \(F=[4,6]\times[4,6]\). The predicate is:

\[
P(\tau)=1
\iff
\text{the agent reaches }T\text{ without entering }F.
\]

**RU:** Использовалась среда навигации 10×10. Агент стартует в \((0,0)\), должен достичь \((9,9)\) и избежать запретной зоны \(F=[4,6]\times[4,6]\). Предикат:

\[
P(\tau)=1
\iff
\text{агент достигает }T\text{, не входя в }F.
\]

| Configuration / Конфигурация | Success / Успех | Mean steps / Средние шаги |
|---|---:|---:|
| Fixed-goal RL / Фиксированная цель | 1.00 | 26.64 |
| Reformulation without projection / Переформулировка без проекции | 1.00 | 20.91 |
| GRA-like projection / GRA-подобная проекция | 1.00 | **19.00** |

**EN:** In this preliminary demonstration, the GRA-like projection produced the shortest safe trajectory: 19 steps. However, this experiment does **not** yet establish suppression of specification gaming, because the drifting baseline did not violate the forbidden region in the sampled runs. A stronger protocol must explicitly count predicate violations and construct refutation policies that actively search for unsafe shortcuts.

**RU:** В предварительной демонстрации GRA-подобная проекция дала кратчайший безопасный путь — 19 шагов. Однако этот эксперимент **ещё не доказывает** подавление specification gaming, поскольку дрейфующий baseline в данных прогонах не нарушил запретную зону. Для полноценной проверки нужно отдельно считать нарушения \(P\) и строить опровергающую политику, которая активно ищет небезопасные обходные пути.

## 4. Practical applications / Практические применения

**EN:**

- **Safe robotics:** reformulate navigation strategies while preserving hard safety boundaries.
- **Planning:** adapt schedules and resource allocations without violating deadlines or capacity limits.
- **Specification refinement:** turn an incomplete initial goal into a more precise one without silently changing its meaning.
- **Agent workflows:** allow an AI agent to improve its internal representation of a task while external validation remains authoritative.

**RU:**

- **Безопасная робототехника:** переформулировать стратегии навигации, сохраняя жёсткие границы безопасности.
- **Планирование:** адаптировать расписания и распределение ресурсов, не нарушая дедлайны и лимиты.
- **Уточнение спецификаций:** превращать неполную исходную цель в более точную, не меняя молча её смысл.
- **Агентные системы:** позволять ИИ-агенту улучшать внутреннее представление задачи, пока внешняя проверка остаётся главной.

## 5. Limitations / Ограничения

**EN:** GRA requires a formalizable and causally checkable predicate. It does not apply directly to open-ended values such as happiness, justice, or beauty. Its guarantees are conditional on the quality and coverage of interventions. If the intervention distribution does not cover failure modes, specification gaming may remain undetected. The method also requires a budget: if no admissible solution exists within available resources, GRA should report infeasibility rather than silently redefine success.

**RU:** GRA требует формализуемого и причинно проверяемого предиката. Она напрямую не применима к открытым ценностям вроде счастья, справедливости или красоты. Её гарантии зависят от качества и покрытия интервенций. Если интеренции не покрывают режимы отказа, specification gaming может остаться незамеченным. Метод также требует бюджета: если допустимого решения при доступных ресурсах нет, GRA должна сообщить о недостижимости, а не молча переопределить успех.

## 6. Conclusion / Вывод

**EN:** GRA proposes a disciplined form of goal evolution: the representation of a goal may change, but the external success predicate remains fixed and causally verified. The central mechanism is the projection of candidate reformulations onto the \(P\)-equivalence class. The preliminary simulation confirms that such a projection yields a valid and efficient safe trajectory in a constrained navigation task, while a complete claim of novelty and gaming suppression requires further controlled experiments.

**RU:** GRA предлагает дисциплинированную форму эволюции цели: представление цели может меняться, но внешний предикат успеха остаётся неизменным и причинно проверяемым. Центральный механизм — проекция кандидатов на класс \(P\)-эквивалентности. Предварительная симуляция подтверждает, что такая проекция даёт корректный и эффективный безопасный путь в задаче навигации с ограничениями; полное утверждение о новизне и подавлении гейминга требует дальнейших контролируемых экспериментов.



 +   

 И напиши про это   билингвальную статью тут https://elibrary.org.cn/m/articles/browse/my&modzzz_articles_filter=add_article подробно с формулами и выводами и практическими применениями и  проведи верификацию этого инсилико 
