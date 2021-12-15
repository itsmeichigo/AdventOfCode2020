from typing import List, ValuesView
from math import inf
def parse_input(file_name) -> List[int]:
    with open(file_name) as file:
        return [int(i) for i in file.read().split(",")]

def find_optimized_fuel(input) -> int:
    fuel_map = {}
    for value in input:
        if value not in fuel_map:
            fuel_map[value] = sum([abs(i - value) for i in input])
    return min(fuel_map.values())

test = parse_input("test.txt")
assert find_optimized_fuel(test) == 37

data = parse_input("data.txt")
print("Part 1: ", find_optimized_fuel(data))