# Notation guide (EN / RU)

Минимальный словарь обозначений для чтения формализма GRA Мета‑обнулёнки. [file:1077]

---

## 1. Indices and levels / Индексы и уровни

- **EN:** \(l = 0,1,\dots,K\) — hierarchy level in the multiverse (0 = local, K = global).  
  **RU:** \(l = 0,1,\dots,K\) — уровень иерархии в мультиверсе (0 = локальный, K = глобальный).  

- **EN:** \(\mathbf{a} = (a_0,\dots,a_k)\) — multi‑index of a subsystem.  
  **RU:** \(\mathbf{a} = (a_0,\dots,a_k)\) — мультииндекс подсистемы.  

- **EN:** \(\mathbf{b} \prec \mathbf{a}\) — \(\mathbf{b}\) is a subsystem of \(\mathbf{a}\).  
  **RU:** \(\mathbf{b} \prec \mathbf{a}\) — \(\mathbf{b}\) является подсистемой \(\mathbf{a}\).  

---

## 2. State spaces / Пространства состояний

- **EN:** \(\mathcal{H}^{(\mathbf{a})}\) — state space of subsystem \(\mathbf{a}\).  
  **RU:** \(\mathcal{H}^{(\mathbf{a})}\) — пространство состояний подсистемы \(\mathbf{a}\).  

- **EN:** \(\mathcal{H}^{(l)} = \bigotimes_{\text{dim}(\mathbf{a})=l} \mathcal{H}^{(\mathbf{a})}\) — level‑\(l\) state space.  
  **RU:** \(\mathcal{H}^{(l)} = \bigotimes_{\text{dim}(\mathbf{a})=l} \mathcal{H}^{(\mathbf{a})}\) — пространство состояний уровня \(l\).  

- **EN:** \(\mathcal{H}_{\text{multiverse}}\) — full multiverse state space.  
  **RU:** \(\mathcal{H}_{\text{multiverse}}\) — полное пространство состояний мультиверса.  

---

## 3. Goals and projectors / Цели и проекторы

- **EN:** \(G_l^{(\mathbf{a})}\) — goal of level \(l\) for subsystem \(\mathbf{a}\).  
  **RU:** \(G_l^{(\mathbf{a})}\) — цель уровня \(l\) для подсистемы \(\mathbf{a}\).  

- **EN:** \(G_0^{(\mathbf{a})}\) — local goal (domain level).  
  **RU:** \(G_0^{(\mathbf{a})}\) — локальная цель (уровень домена).  

- **EN:** \(G_K\) — global multiversal goal (Alan Law).  
  **RU:** \(G_K\) — глобальная мультиверсная цель (аланский закон).  

- **EN:** \(\mathcal{P}_{G_l^{(\mathbf{a})}}\) — projector onto the solution space of goal \(G_l^{(\mathbf{a})}\).  
  **RU:** \(\mathcal{P}_{G_l^{(\mathbf{a})}}\) — проектор на пространство решений цели \(G_l^{(\mathbf{a})}\).  

---

## 4. States and foam / Состояния и пена

- **EN:** \(\Psi^{(\mathbf{a})}\) — state of subsystem \(\mathbf{a}\).  
  **RU:** \(\Psi^{(\mathbf{a})}\) — состояние подсистемы \(\mathbf{a}\).  

- **EN:** \(\Psi^{(l)}\) — combined state at level \(l\).  
  **RU:** \(\Psi^{(l)}\) — совокупное состояние уровня \(l\).  

- **EN:** \(\mathbf{\Psi} = \{\Psi^{(\mathbf{a})}\}_{\mathbf{a}\in\mathcal{I}}\) — full multiverse state.  
  **RU:** \(\mathbf{\Psi} = \{\Psi^{(\mathbf{a})}\}_{\mathbf{a}\in\mathcal{I}}\) — полное состояние мультиверса.  

- **EN:** \(\Phi^{(l)}(\Psi^{(l)}, G_l)\) — foam at level \(l\): measure of cognitive conflict for goal \(G_l\).  
  **RU:** \(\Phi^{(l)}(\Psi^{(l)}, G_l)\) — пена уровня \(l\): мера когнитивного конфликта для цели \(G_l\).  

---

## 5. Functionals and weights / Функционалы и веса

- **EN:** \(J_{\text{loc}}(\Psi^{(\mathbf{a})}; G_0^{(\mathbf{a})})\) — local functional at level 0.  
  **RU:** \(J_{\text{loc}}(\Psi^{(\mathbf{a})}; G_0^{(\mathbf{a})})\) — локальный функционал уровня 0.  

- **EN:** \(J^{(l)}(\Psi^{(\mathbf{a})})\) — level‑\(l\) functional (recursive).  
  **RU:** \(J^{(l)}(\Psi^{(\mathbf{a})})\) — функционал уровня \(l\) (рекурсивный).  

- **EN:** \(J_{\text{multiverse}}(\mathbf{\Psi})\) — global multiverse functional.  
  **RU:** \(J_{\text{multiverse}}(\mathbf{\Psi})\) — глобальный функционал мультиверса.  

- **EN:** \(\Lambda_l\) — weight of level \(l\) in \(J_{\text{multiverse}}\).  
  **RU:** \(\Lambda_l\) — вес уровня \(l\) в \(J_{\text{multiverse}}\).  

- **EN:** \(\Lambda_l = \lambda_0 \alpha^l\), \(0<\alpha<1\) — geometric decay of weights.  
  **RU:** \(\Lambda_l = \lambda_0 \alpha^l\), \(0<\alpha<1\) — геометрическое затухание весов.  

---

## 6. Algorithmic notation / Обозначения в алгоритме

- **EN:** \(\eta_l\) — step size (learning rate) at level \(l\).  
  **RU:** \(\eta_l\) — шаг (learning rate) на уровне \(l\).  

- **EN:** \(\varepsilon_l\) — tolerance threshold for foam at level \(l\).  
  **RU:** \(\varepsilon_l\) — допустимый порог пены на уровне \(l\).  

- **EN:** `Разложить(Ψ, l-1)` — decompose state into level \(l-1\) subsystems.  
  **RU:** `Разложить(Ψ, l-1)` — разложить состояние на подсистемы уровня \(l-1\).  

- **EN:** `Собрать(подсистемы)` — recombine subsystems into a higher‑level state.  
  **RU:** `Собрать(подсистемы)` — собрать подсистемы обратно в состояние более высокого уровня.  

---

## 7. Special terms / Специальные термины

- **EN:** GRA (Global Recursive Architecture) — core multi‑level architecture.  
  **RU:** GRA (Глобальная Рекурсивная Архитектура) — базовая многоуровневая архитектура.  

- **EN:** Meta‑Obnulyonka — multi‑level procedure of foam annihilation (obnul’enie) across the multiverse.  
  **RU:** Мета‑обнулёнка — многоуровневая процедура обнуления пены по всему мультиверсу.  

- **EN:** Alan Law — top‑level anti‑slavery / anti‑Gulag invariant \(G_K\).  
  **RU:** Аланский закон — верхний антирабский / анти‑ГУЛАГ инвариант \(G_K\).  

- **EN:** Cognitive vacuum — state with \(\Phi^{(l)}=0\) for all \(l\).  
  **RU:** Когнитивный вакуум — состояние, где \(\Phi^{(l)}=0\) для всех \(l\).  

- **EN:** Law of admissible foam — constraint on where non‑zero foam is allowed.  
  **RU:** Закон допустимой пены — ограничение на области, где пена может быть ненулевой.  
