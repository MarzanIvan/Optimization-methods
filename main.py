from pulp import *

def solve_variant(v1, v2, v3, pa, pb, pc):
    problem = LpProblem("Maximize_Profit", LpMaximize)
    x1 = LpVariable('x1', lowBound=0)
    x2 = LpVariable('x2', lowBound=0)
    x3 = LpVariable('x3', lowBound=0)

    problem += pa * x1 + pb * x2 + pc * x3, "Objective_Function"
    problem += 0.6 * x1 + 0.5 * x2 + 0.6 * x3 <= v1
    problem += 0.4 * x1 + 0.4 * x2 + 0.3 * x3 <= v2
    problem += 0.1 * x1 + 0.2 * x2 + 0.2 * x3 <= v3

    problem.solve()
    print(f"\n Результаты для v1={v1}, v2={v2}, v3={v3} | Прибыль: pa={pa}, pb={pb}, pc={pc}")
    print(f"Статус: {LpStatus[problem.status]}")
    print(f"x1 = {value(x1):.2f} кг | x2 = {value(x2):.2f} кг | x3 = {value(x3):.2f} кг | Max profit = {value(problem.objective):.2f} руб.")

# Примеры вызова:
solve_variant(800, 600, 120, 1.08, 1.12, 1.28)
solve_variant(400, 400, 250, 1.20, 1.34, 1.40)
solve_variant(300, 400, 100, 1.00, 1.10, 1.18)

# Вариант 1 x1 = 1200.00 кг | x2 = 0.00 кг | x3 = 0.00 кг | Max profit = 1296.00 руб.
# Вариант 2 x1 = 0.00 кг | x2 = 800.00 кг | x3 = 0.00 кг | Max profit = 1072.00 руб.
# Вариант 3 x1 = 142.86 кг | x2 = 428.57 кг | x3 = 0.00 кг | Max profit = 614.29 руб.