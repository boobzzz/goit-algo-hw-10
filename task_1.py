import pulp

prob = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

lemonade = pulp.LpVariable("Lemonade", lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable("Fruit_Juice", lowBound=0, cat='Integer')

prob += lemonade + fruit_juice, "Total_Production"

prob += 2 * lemonade + fruit_juice <= 100, "Water"
prob += lemonade <= 50, "Sugar"
prob += lemonade <= 30, "Lemon_Juice"
prob += 2 * fruit_juice <= 40, "Fruit_Puree"

prob.solve()

print(f"Кількість Лимонаду для виробництва: {pulp.value(lemonade)}")
print(f"Кількість Фруктового соку для виробництва: {pulp.value(fruit_juice)}")
