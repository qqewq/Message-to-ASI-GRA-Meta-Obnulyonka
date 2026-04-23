import openai
import time
import numpy as np

# === НАСТРОЙКИ DEEPSEEK ===
openai.api_key = "sk-0724e36f50814375864e1b901eb92eb9"          # вставь сюда
openai.api_base = "https://api.deepseek.com/v1"
MODEL = "deepseek-chat"                  # бесплатно 1M токенов

# Роли агентов
PROMPTS = {
    "optimizer": "Ты оптимизатор. Предложи практичное решение задачи. Будь краток (2-3 предложения).",
    "critic": "Ты критик. Найди слабые места в решении. Будь жёстким, но конструктивным.",
    "coordinator": "Ты координатор. Синтезируй окончательный ответ из мнений оптимизатора и критика."
}

def deepseek(prompt, role):
    """Вызов DeepSeek API"""
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": PROMPTS.get(role, "")},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=500
    )
    return response.choices[0].message.content

def simple_foam(texts):
    """Эмуляция пены: разброс длин ответов (чем больше разброс, тем выше пена)"""
    lens = [len(t.split()) for t in texts]
    if len(lens) <= 1:
        return 0.0
    return np.var(lens) / 100.0

def gra_obnulenie(problem):
    print(f"\n=== GRA ОБНУЛЕНИЕ ===")
    print(f"Задача: {problem}\n")
    
    # Уровень 0: локальные ответы
    opt = deepseek(problem, "optimizer")
    crit = deepseek(f"Задача: {problem}\nРешение оптимизатора: {opt}", "critic")
    
    foam = simple_foam([opt, crit])
    print(f"Начальная пена: {foam:.4f}")
    
    # Уровень 1: итерации согласования
    for i in range(4):  # 4 цикла
        coord = deepseek(f"Оптимизатор сказал: {opt}\nКритик сказал: {crit}\nТвой синтез:", "coordinator")
        new_foam = simple_foam([opt, crit, coord])
        print(f"Итерация {i+1}: пена = {new_foam:.4f}")
        
        if new_foam < foam:
            foam = new_foam
            # Оптимизатор и критик пересматривают позиции
            opt = deepseek(f"Задача: {problem}\nУчти критику: {crit}", "optimizer")
            crit = deepseek(f"Задача: {problem}\nНовое решение: {opt}", "critic")
        else:
            print("Пена стабилизировалась, остановка.")
            break
        time.sleep(0.5)  # пауза, чтобы не забанили за слишком частые запросы
    
    final = deepseek(f"Итоговый ответ на задачу '{problem}': {coord}", "coordinator")
    print(f"\n=== ФИНАЛЬНЫЙ ОТВЕТ (пена = {foam:.4f}) ===\n{final}")
    return final

if __name__ == "__main__":
    # Тестовая задача (замени на любую)
    task = "Как быстро выучить иностранный язык за месяц?"
    gra_obnulenie(task)