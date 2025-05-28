def min_rental_cost_with_plan(demand):
    n = len(demand)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    rental_plan = [0] * n  # Количество арендованных автомобилей на каждой неделе

    for i in range(1, n + 1):
        # Вариант 1: начать новую аренду на неделе i
        cost_new = 500 + 220 * demand[i-1]
        if dp[i-1] + cost_new < dp[i]:
            dp[i] = dp[i-1] + cost_new
            rental_plan[i-1] = demand[i-1]  # Арендуем ровно сколько нужно

        # Вариант 2: продлить аренду с предыдущей недели j
        for j in range(i-1, 0, -1):
            max_demand = max(demand[j-1:i])
            cost_extend = 220 * max_demand * (i - j + 1)
            total_cost = dp[j-1] + 500 + cost_extend
            if total_cost < dp[i]:
                dp[i] = total_cost
                # Обновляем план аренды: на неделях j..i арендуем max_demand
                for k in range(j-1, i):
                    rental_plan[k] = max_demand

    return dp[n], rental_plan

demand = [7, 4, 7, 8]
min_cost, plan = min_rental_cost_with_plan(demand)
print(f"План по договору: {demand}")
print(f"Минимальная стоимость аренды: {min_cost}$")
print("Стратегия аренды по неделям:")
for week, cars in enumerate(plan, start=1):
    print(f"Неделя {week}: {cars} автомобилей")