from typing import List, ValuesView
from math import dist, inf
def parse_input(file_name) -> List[int]:
    with open(file_name) as file:
        return [int(i) for i in file.read().split(",")]

def find_optimized_fuel(input) -> int:
    fuel_costs, linear_costs = [], []
    for value in range(max(input)):
        fuel_costs.append(sum(abs(i - value) for i in input))
        linear_costs.append(sum(calculate_actual_cost(i, value) for i in input))
    return min(fuel_costs), min(linear_costs)

def calculate_actual_cost(a, b) -> int:
    distance = abs(a - b)
    return (distance + 1) * distance // 2

test = parse_input("test.txt")
test_costs = find_optimized_fuel(test)
assert test_costs[0] == 37
assert test_costs[1] == 168

data = parse_input("data.txt")
cost = find_optimized_fuel(data)
print("Part 1: ", cost[0])
print("Part 2: ", cost[1])