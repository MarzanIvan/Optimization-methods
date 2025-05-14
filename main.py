from pulp import *

# Создаем задачу максимизации
problem = LpProblem("Maximize_Objective", LpMaximize)

# Определяем переменные
x1 = LpVariable("x1", lowBound=0)
x2 = LpVariable("x2", lowBound=0)
x3 = LpVariable("x3", lowBound=0)
x4 = LpVariable("x4", lowBound=0)
x5 = LpVariable("x5", lowBound=0)

# Целевая функция
problem += x1 - x2 + x3 - x4 + x5, "Objective_Function"

# Ограничения
problem += x1 + x2 + 4*x3 + 4*x4 + 3*x5 <= 3, "Constraint_1"
problem += x1 - x2 - 2*x3 + 2*x4 + 5*x5 <= 1, "Constraint_2"

# Решение задачи
problem.solve()

# Вывод результатов
print(f"Status: {LpStatus[problem.status]}")
for i in range(1, 6):
    print(f"x{i} = {value(eval('x'+str(i)))}")
print(f"Max value = {value(problem.objective)}")
