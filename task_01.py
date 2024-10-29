from pulp import LpMaximize, LpProblem, LpVariable, value


model = LpProblem("Maximize Production", LpMaximize)

#кількість виробленого Лимонаду та Фруктового соку
limonade = LpVariable("Limonade", lowBound=0, cat="Integer")
fruit_juice = LpVariable("Fruit_Juice", lowBound=0, cat="Integer")

#Максимізувати кількість продуктів
model += limonade + fruit_juice, "Total Products"

#Обмеження на ресурси
model += 2 * limonade + 1 * fruit_juice <= 100, "Water Constraint"  
model += 1 * limonade <= 50, "Sugar Constraint"
model += 1 * limonade <= 30, "Lemon Juice Constraint"  


model.solve()

print("Кількість виробленого Лимонаду:", value(limonade))
print("Кількість виробленого Фруктового соку:", value(fruit_juice))
print("Загальна кількість продуктів:", value(model.objective))
