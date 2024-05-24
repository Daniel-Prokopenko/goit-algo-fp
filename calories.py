def greedy_algorithm(items: dict, money: int) -> int:
    sorted_food = sorted(
        list(items.keys()),
        key=lambda food: items[food]["calories"] / items[food]["cost"],
        reverse=True,
    )
    current = 0
    bill = []
    for food in sorted_food:
        if current + items[food]["cost"] <= money:
            bill.append(food)
            current += items[food]["cost"]
    return bill


def dynamic_programming(items, money):
    costs = [items[item]["cost"] for item in items]
    calories = [items[item]["calories"] for item in items]
    names = list(items.keys())
    n = len(costs)

    K = [[0 for _ in range(money + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for m in range(1, money + 1):
            if costs[i - 1] <= m:
                K[i][m] = max(K[i - 1][m], K[i - 1][m - costs[i - 1]] + calories[i - 1])
            else:
                K[i][m] = K[i - 1][m]

    max_cals = K[n][money]
    result = []

    for i in range(n, 0, -1):
        if max_cals <= 0:
            break
        if max_cals == K[i - 1][m]:
            continue
        else:
            result.append(names[i - 1])
            max_cals -= calories[i - 1]
            money -= costs[i - 1]

    return result


menu = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}


print(greedy_algorithm(menu, 150))
print(dynamic_programming(menu, 150))
