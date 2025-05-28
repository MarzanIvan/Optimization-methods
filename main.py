import pandas as pd

# Данные: партии и вероятности
parties = [0.8, 1.0, 1.2, 1.4]  # % дефектных
probabilities = [0.4, 0.3, 0.25, 0.05]  # вероятности

# Потребители и их допустимые уровни брака
consumers = {
    "A": 0.8,
    "B": 1.2,
    "C": 1.4
}

# Создаем таблицу "решений"
data = []

for party, prob in zip(parties, probabilities):
    for consumer, max_defect in consumers.items():
        diff = round(party - max_defect, 3)  # разница
        if diff > 0:
            # штраф
            penalty = diff / 0.1 * -1000
        elif diff < 0:
            # бонус
            penalty = abs(diff) / 0.1 * 500
        else:
            penalty = 0
        expected = penalty * prob
        data.append({
            "Партия %": party,
            "Потребитель": consumer,
            "Макс. допущено": max_defect,
            "Разница %": diff,
            "Штраф/прибыль": penalty,
            "Вероятность": prob,
            "Ожидаемый доход": expected
        })

df = pd.DataFrame(data)

# Вывод дерева решений
print("\nДерево решений:\n")
print(df)

# Группируем по потребителям — суммарный ожидаемый доход
summary = df.groupby("Потребитель")["Ожидаемый доход"].sum().sort_values(ascending=False)

print("\nСуммарная ожидаемая прибыль/убыток по потребителям:\n")
print(summary)

best = summary.idxmax()
print(f"\n🔍 Лучший потребитель с наивысшим приоритетом: {best}")
