from typing import List, Tuple

def parse_input(file_name) -> List[str]:
    with open(file_name) as file:
        return file.read().splitlines()

def calculate_coordinates(input, withAim=False) -> int:
    x, y, aim = 0, 0, 0
    for line in input:
        direction, strValue = line.split()
        value = int(strValue)
        if direction == "forward":
            x += value
            if withAim:
                y += value * aim
        elif direction == "down":
            if withAim:
                aim += value
            else:
                y += value
        elif direction == "up":
            if withAim:
                aim -= value
            else:
                y -= value
    return x * y

test_input = parse_input("test.txt")
assert calculate_coordinates(test_input) == 150
assert calculate_coordinates(test_input, withAim=True) == 900

input = parse_input("data.txt")
print("Part 1: ", calculate_coordinates(input))
print("Part 2:", calculate_coordinates(input, withAim=True))
    