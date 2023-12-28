from itertools import permutations


def calculate_distance(order, distances):
    total_distance = 0
    for i in range(len(order) - 1):
        total_distance += distances[order[i]][order[i + 1]]
    total_distance += distances[order[-1]][order[0]]
    return total_distance


def traveling_salesman_bruteforce(distances):
    num_cities = len(distances)
    all_city_orders = permutations(range(num_cities))

    min_distance = float('inf')
    best_order = None

    for order in all_city_orders:
        distance = calculate_distance(order, distances)
        if distance < min_distance:
            min_distance = distance
            best_order = order

    return best_order, min_distance


example_distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

best_order, min_distance = traveling_salesman_bruteforce(example_distances)

print("Best order:", best_order)
print("Min distance:", min_distance)
