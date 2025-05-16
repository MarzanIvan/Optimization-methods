import numpy as np

# Данные
supply = [300, 700, 600, 900, 500]  # поставщики
demand = [600, 800, 700, 900]  # пункты назначения
cost_matrix = np.array([[5, 8, 3, 6],
                        [4, 6, 8, 2],
                        [6, 9, 7, 2],
                        [1, 3, 4, 7],
                        [5, 3, 8, 1]])  # Тарифы

def northwest_corner_method(supply, demand):
    num_suppliers = len(supply)
    num_customers = len(demand)
    solution = np.zeros((num_suppliers, num_customers))

    i, j = 0, 0
    while i < num_suppliers and j < num_customers:
        allocation = min(supply[i], demand[j])
        solution[i][j] = allocation
        supply[i] -= allocation
        demand[j] -= allocation

        if supply[i] == 0:
            i += 1
        if demand[j] == 0:
            j += 1

    return solution


# Получение опорного решения
initial_solution = northwest_corner_method(supply.copy(), demand.copy())

print("Опорное решение:")
print(initial_solution)

total_cost = np.sum(initial_solution * cost_matrix)
print("Общая стоимость транспортировки:", total_cost)
