# GRA-2: Verified Self-Improving Architecture for Trustworthy AI
# GRA-2: Верифицируемая самоулучшающаяся архитектура для надёжного ИИ


## EN — Abstract

Modern AI systems accumulate internal contradictions: logical conflicts, factual errors, misaligned agent goals. Most approaches (debate, voting, smoothing) hide these contradictions rather than resolve them. We propose **GRA-2** — a verified self-improving architecture that treats contradictions as first-class objects: it measures them ("foam"), localizes them via SAT/UNSAT and Minimal Unsatisfiable Subsets (MUS), repairs them via Weighted Partial MaxSAT, certifies repairs in Lean 4, and continuously recalibrates its own tolerance thresholds based on confirmed feedback. The result is a system that improves **within** its safety constitution, never against it.

## RU — Аннотация

Современные ИИ-системы накапливают внутренние противоречия: логические конфликты, фактические ошибки, рассогласование целей агентов. Большинство подходов (дебаты, голосование, сглаживание) скрывают противоречия, а не устраняют их. Мы предлагаем **GRA-2** — верифицируемую самоулучшающуюся архитектуру, которая рассматривает противоречия как объекты первого класса: измеряет их («пена»), локализует через SAT/UNSAT и минимальные неразрешимые подмножества (MUS), исправляет через Weighted Partial MaxSAT, сертифицирует исправления в Lean 4 и непрерывно перекалибрует собственные пороги допуска на основе подтверждённой обратной связи. Результат — система, которая улучшается **внутри** своей конституции безопасности, а не вопреки ей.


## 1. The Problem / Проблема

**EN.** LLMs and multi-agent systems produce contradictions at scale. Debate and majority voting fail because a contradictory majority can outvote a correct minority. Smoothing and regularization blur contradictions without removing them. What is needed is a system that **detects, localizes, repairs, and proves** the repair.

**RU.** LLM и мультиагентные системы производят противоречия в масштабе. Дебаты и голосование большинством не работают, потому что противоречивое большинство может «переголосовать» правильное меньшинство. Сглаживание и регуляризация размывают противоречия, не устраняя их. Нужна система, которая **обнаруживает, локализует, исправляет и доказывает** исправление.


## 2. Core Architecture / Ядро архитектуры

**EN.** GRA-2 is a closed loop:

\[
s_t \to \text{GRA}(s_t;\theta_t) \to a_t \to r_t \to J_t \to \theta_{t+1}
\]

where \(J_t\) is the measured "foam" (residual contradiction level), and \(\theta_t=(\varepsilon_t,\tau_t,k_t,\mathbf w_t,\delta_t)\) are calibration parameters updated only from confirmed results.

**RU.** GRA-2 — замкнутый контур:

\[
s_t \to \text{GRA}(s_t;\theta_t) \to a_t \to r_t \to J_t \to \theta_{t+1}
\]

где \(J_t\) — измеренная «пена» (остаточный уровень противоречий), а \(\theta_t=(\varepsilon_t,\tau_t,k_t,\mathbf w_t,\delta_t)\) — параметры калибровки, обновляемые только по подтверждённым результатам.

### Foam functional / Функционал пены

\[
J(s)=\alpha\Phi_C+\beta\Phi_T+\gamma\Phi_V+\delta\Phi_S
\]

- \(\Phi_C\) — contradictions / противоречия
- \(\Phi_T\) — coordination errors / рассогласование
- \(\Phi_V\) — verification errors / ошибки верификации
- \(\Phi_S\) — instability / нестабильность

### Working tolerance / Рабочий допуск

\[
\boxed{J(s)\leq\tau=\varepsilon_{\rm GRA}+\delta_{\rm safety}}
\]

GRA-2 does not chase \(J=0\). It targets a **calibrated minimum** of residual foam.

GRA-2 не стремится к \(J=0\). Он нацелен на **калиброванный минимум** остаточной пены.


## 3. Formal Verification / Формальная верификация

**EN.** Knowledge is split into hard clauses (logic, safety, ethics — never revised) and soft clauses (hypotheses with weights). Revision is a Weighted Partial MaxSAT problem:

\[
F'^*=\arg\min_{F'\subseteq\mathcal S}\left\{\sum_{f_i\notin F'}w_i:\mathcal H\cup F'\text{ is SAT}\right\}
\]

When UNSAT is detected, a Minimal Unsatisfiable Subset (MUS) localizes the exact conflicting clauses. An external SAT solver produces a DRAT/LRAT certificate; Lean 4 imports and verifies it as a theorem.

**RU.** База знаний делится на жёсткие клаузы (логика, безопасность, этика — не пересматриваются) и мягкие (гипотезы с весами). Пересмотр — задача Weighted Partial MaxSAT:

\[
F'^*=\arg\min_{F'\subseteq\mathcal S}\left\{\sum_{f_i\notin F'}w_i:\mathcal H\cup F'\text{ is SAT}\right\}
\]

При обнаружении UNSAT минимальное неразрешимое подмножество (MUS) локализует конкретные конфликтующие клаузы. Внешний SAT-решатель выдаёт сертификат DRAT/LRAT; Lean 4 импортирует и проверяет его как теорему.

\[
\boxed{\text{Lean}\vdash\text{valid\_certificate}(c,F)\Rightarrow\text{Unsatisfiable}(F)}
\]


## 4. Self-Improvement Loop / Петля самоулучшения

**EN.** Only calibration parameters self-improve — never the safety constitution:

\[
\varepsilon_{t+1}=(1-\eta_t)\varepsilon_t+\eta_tJ_t
\]
\[
\delta_{t+1}=\max\left(\delta_{\min},\delta_t+\eta_\delta[\mathbf 1[J_t>\tau_t]-\alpha_{\rm target}]\right)
\]
\[
\theta_{t+1}=\mathrm{Proj}_{\mathcal C}\left[\theta_t-\eta_t\nabla_\theta\mathcal L(\theta_t)\right]
\]

The projection \(\mathrm{Proj}_{\mathcal C}\) guarantees the system never leaves its allowed parameter space — it cannot "lower its own bar."

**RU.** Самоулучшаются только параметры калибровки — никогда конституция безопасности:

\[
\varepsilon_{t+1}=(1-\eta_t)\varepsilon_t+\eta_tJ_t
\]
\[
\delta_{t+1}=\max\left(\delta_{\min},\delta_t+\eta_\delta[\mathbf 1[J_t>\tau_t]-\alpha_{\rm target}]\right)
\]
\[
\theta_{t+1}=\mathrm{Proj}_{\mathcal C}\left[\theta_t-\eta_t\nabla_\theta\mathcal L(\theta_t)\right]
\]

Проекция \(\mathrm{Proj}_{\mathcal C}\) гарантирует, что система никогда не выйдет за пределы допустимого пространства параметров — она не может «снизить себе планку».

***

## 5. In-Silico Verification / Верификация in silico

**EN.** Three-layer validation:

1. **Formal** — Lean 4 verifies SAT certificates.
2. **Simulation** — thousands of scenarios including adversarial.
3. **Statistical** — ECE, FPR, FNR thresholds gate every update.

\[
\mathrm{ECE}\leq\varepsilon_{\rm cal},\quad
\mathrm{FPR}\leq\alpha_{\max},\quad
\mathrm{FNR}\leq\beta_{\max}
\]

If any threshold is violated, the system rolls back to the last verified checkpoint and triggers Human Gate.

**RU.** Трёхслойная валидация:

1. **Формальная** — Lean 4 проверяет SAT-сертификаты.
2. **Симуляционная** — тысячи сценариев, включая adversarial.
3. **Статистическая** — пороги ECE, FPR, FNR контролируют каждое обновление.

Если хотя бы один порог нарушен — откат к последней проверенной точке и Human Gate.


## 6. Practical Applications / Практические применения

| Domain / Область | What GRA-2 does / Что делает GRA-2 |
|---|---|
| Science / Наука | Verifies hypotheses, detects contradictions in papers / Проверяет гипотезы, находит противоречия |
| Engineering / Инженерия | Digital twin mismatch detection / Выявление расхождений в цифровых двойниках |
| Medicine / Медицина | Cross-checks protocols and models / Сверяет протоколы и модели |
| Finance / Финансы | Reconciles risk models with market/regulatory data / Сверяет модели риска с рынком и регулятором |
| Robotics / Робототехника | Formally verified actions / Формально верифицированные действия |
| LLM agents / LLM-агенты | Meta-controller for agent swarms / Мета-контроллер роя агентов |


## 7. Honest Limits / Честные границы

**EN.** MaxSAT is NP-hard and needs decomposition at scale. Not everything formalizes as CNF (aesthetics, values, subjectivity). Lean verifies certificates, not the world. Human Gate remains non-automatable. GRA-2 is not AGI or ASI — it is a **governance layer** that makes whatever intelligence sits underneath more trustworthy.

**RU.** MaxSAT NP-труден и требует декомпозиции на масштабе. Не всё формализуется в CNF (эстетика, ценности, субъективность). Lean проверяет сертификаты, а не мир. Human Gate остаётся неавтоматизируемым. GRA-2 — это не AGI и не ASI, а **слой управления**, который делает любой лежащий под ним интеллект более надёжным.


## 8. Conclusion / Заключение

**EN.** GRA-2 unifies three previously separate ideas: contradiction-as-signal (GRA), minimal-change revision (MaxSAT/MUS), and machine-checked proof (Lean 4) — then closes the loop with online calibration constrained by a fixed safety constitution. The result is not a "machine that knows everything," but a system that **knows the limits of its own knowledge, measures them, proves repairs, and improves safely**.

\[
\boxed{\text{AI searches. GRA criticizes. MaxSAT minimizes. Lean verifies. Calibration learns. Humans remain responsible.}}
\]

**RU.** GRA-2 объединяет три ранее раздельные идеи: противоречие как сигнал (GRA), пересмотр с минимальным изменением (MaxSAT/MUS) и машинно-проверяемое доказательство (Lean 4) — затем замыкает петлю онлайн-калибровкой, ограниченной фиксированной конституцией безопасности. Результат — не «машина, которая знает всё», а система, которая **знает границы своего знания, измеряет их, доказывает исправления и безопасно улучшается**.

\[
\boxed{\text{ИИ ищет. GRA критикует. MaxSAT минимизирует. Lean верифицирует. Калибровка учится. Ответственность остаётся за человеком.}}
\]

