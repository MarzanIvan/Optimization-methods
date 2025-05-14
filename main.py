from pulp import *

# Создаем задачу максимизации
problem = LpProblem("Maximize_Profit", LpMaximize)

# Определяем переменные с нижней границей 0
x1 = LpVariable('x1', lowBound=0)
x2 = LpVariable('x2', lowBound=0)

# Определяем целевую функцию
problem += 410 * x1 + 840 * x2, "Objective_Function"

# Добавляем ограничения
problem += 22 * x1 + 140 * x2 <= 61500, "Constraint_1"
problem += 1.5 * x1 + 30 * x2 <= 15000, "Constraint_2"
problem += x1 <= 600, "Constraint_3"
problem += x2 <= 400, "Constraint_4"


# Решаем задачу
problem.solve()

# Вывод результатов
print(f"Status: {LpStatus[problem.status]}")
print(f"x1 = {value(x1)}")
print(f"x2 = {value(x2)}")
print(f"Max profit = {value(problem.objective)}")
