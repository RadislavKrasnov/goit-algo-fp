
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

n = len(items)
budget = 100

def max_calorie_meals(budget, items, n):
    meals = []
    calories = []
    costs = []

    for name, values in items.items():
        meals.append(name)
        calories.append(values['calories'])
        costs.append(values['cost'])

    K = [[0 for b in range(budget + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        for b in range(budget + 1):
            if i == 0 or b == 0:
                K[i][b] = 0
            elif costs[i - 1] <= b:
                K[i][b] = max(calories[i - 1] + K[i -1][b - costs[i - 1]], K[i - 1][b])
            else:
                K[i][b] = K[i - 1][b]
    
    max_calories = K[n][budget]
    b = budget
    result = {
        "items": {},
        "total_calories": max_calories
    }

    for i in range(n, 0, -1):
        if max_calories <= 0:
            break
        if max_calories == K[i - 1][b]: # item was not included in the optimal solution
            continue
        else:
            meal_name = meals[i - 1]
            result['items'][meal_name] = items[meal_name]
            max_calories -= calories[i - 1]
            b -= costs[i - 1]
    
    return result

print(max_calorie_meals(budget, items, n))
