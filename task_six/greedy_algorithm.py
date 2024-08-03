
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

class Item:
    def __init__(self, name, cost, calories):
        self.name = name
        self.cost = cost
        self.calories = calories
        self.ratio = calories / cost

def get_high_calorie_cost_meals(items, budget):
    items.sort(key=lambda x: x.ratio, reverse=True)
    result = {
        "items": {}
    }
    total_cost = 0
    total_calories = 0
    for item in items:
        if budget >= item.cost:
            budget -= item.cost
            result['items'][item.name] = {
                "cost": item.cost,
                "calories": item.calories
            }
            total_cost += item.cost
            total_calories += item.calories
    result['total_cost'] = total_cost
    result['total_calories'] = total_calories

    return result

items = [Item(name, values['cost'], values['calories']) for name, values in items.items()]
budget = 100
result = get_high_calorie_cost_meals(items, budget)
high_calorie_cost_meals = result['items']

for name, values in high_calorie_cost_meals.items():
    print(f'{name}: cost {values['cost']}, calories: {values['calories']}')

print(result['total_cost'])
print(result['total_calories'])
