import pulp

# Названия изделий и станков
products = ['A', 'B', 'C', 'D']
machines = ['S1', 'S2', 'S3']

# Требуемые объемы продукции
demand = {'A': 495, 'B': 265, 'C': 378, 'D': 162}

# Ограничения времени по станкам
machine_time_limit = {'S1': 80, 'S2': 100, 'S3': 150}

# Время (в часах) на изготовление одного изделия
time_required = {
    'A': {'S1': 0.5, 'S2': 0.4, 'S3': 0.4},
    'B': {'S1': 0.3, 'S2': 0.2, 'S3': 0.1},
    'C': {'S1': 0.4, 'S2': 0.2, 'S3': 0.3},
    'D': {'S1': 0.1, 'S2': 0.5, 'S3': 0.6},
}

# Стоимость (в руб.) за единицу изделия
cost = {
    'A': {'S1': 0.12, 'S2': 0.15, 'S3': 0.18},
    'B': {'S1': 0.25, 'S2': 0.15, 'S3': 0.35},
    'C': {'S1': 0.30, 'S2': 0.40, 'S3': 0.50},
    'D': {'S1': 0.40, 'S2': 0.20, 'S3': 0.10},
}

# Создаем задачу на минимизацию
prob = pulp.LpProblem("Minimize_Costs", pulp.LpMinimize)

# Переменные: сколько изделий p произвести на станке m
x = pulp.LpVariable.dicts("x", ((p, m) for p in products for m in machines), lowBound=0, cat='Continuous')

# Целевая функция: сумма всех издержек
prob += pulp.lpSum(x[p, m] * cost[p][m] for p in products for m in machines)

# Ограничение по объему выпуска каждого изделия
for p in products:
    prob += pulp.lpSum(x[p, m] for m in machines) == demand[p]

# Ограничения по времени работы каждого станка
for m in machines:
    prob += pulp.lpSum(x[p, m] * time_required[p][m] for p in products) <= machine_time_limit[m]

# Решение
prob.solve()

# Вывод результатов
print(f"Статус: {pulp.LpStatus[prob.status]}")
print(f"Минимальные издержки: {pulp.value(prob.objective):.2f} руб.")

print("\nПлан производства по станкам:")
for p in products:
    for m in machines:
        quantity = x[p, m].varValue
        if quantity > 0:
            print(f"{p} на {m}: {quantity:.2f} шт.")
