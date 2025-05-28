from pulp import *


def solver(l):
    # Создаем задачу максимизации
    problem = LpProblem("Minimize_Lagrangian", LpMinimize)

    # Определяем переменные с нижней границей 0
    x1 = LpVariable('x1', lowBound=0)
    x2 = LpVariable('x2', lowBound=0)
    x3 = LpVariable('x3', lowBound=0)
    x4 = LpVariable('x4', lowBound=0)

    # Определяем целевую функцию
    problem += (l - 1) * x1 - (1 + 2 * l) * x2 - x3 - x4, "Objective_Function"

    # Добавляем ограничения
    problem += x1 + 3 * x2 + 7 * x3 - x4 == 6, "Constraint_1"
    problem += x1 - x2 - x3 + 3 * x4 == 2, "Constraint_2"

    # Решаем задачу
    problem.solve()

    # Вывод результатов
    print(f"Status: {LpStatus[problem.status]}")
    print(f"x1 = {value(x1)}")
    print(f"x2 = {value(x2)}")
    print(f"x3 = {value(x3)}")
    print(f"x4 = {value(x4)}")
    print(f"l  = {l}")
    print(f"Min L = {value(problem.objective)}")
    print("\n")


def main():
    ar = [-10, 0, 10]
    for _ in ar:
        solver(_)


if __name__ == "__main__":
    main()
