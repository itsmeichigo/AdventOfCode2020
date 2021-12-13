from typing import List, Tuple
from math import prod

def parse_input(file_name) -> List[List[List[int]]]:
    with open(file_name) as file:
        return [[int(n) for n in line] for line in file.read().splitlines()]

def find_adjacents(input) -> List[List[List[Tuple[int, int, int]]]]:
    adjacents = [[[] for n in line] for line in input]
    width, height = len(input[0]), len(input)
    for x in range(height):
        for y in range(width):
            current = adjacents[x][y]
            if x-1 >= 0: current.append((input[x-1][y], x-1, y))
            if x+1 < height: current.append((input[x+1][y], x+1, y))
            if y-1 >= 0: current.append((input[x][y-1], x, y-1))
            if y+1 < width: current.append((input[x][y+1], x, y+1))
    return adjacents

def calculate_lava_tubes(input) -> Tuple[int, int]:
    risk_level, basins = 0, []
    in_basin = [[None for n in line] for line in input]
    width, height = len(input[0]), len(input)
    adjacents = find_adjacents(input)
    for x in range(height):
        for y in range(width):
            if len([n for n in adjacents[x][y] if n[0] > input[x][y]]) == len(adjacents[x][y]):
                risk_level += (1 + input[x][y])
            if in_basin[x][y] is None:
                if input[x][y] == 9: in_basin[x][y] = False
                else:
                    in_basin[x][y] = True
                    basin = []
                    basin.append(input[x][y])
                    find_basin(x, y, adjacents, in_basin, basin)
                    basins.append(basin)
    sizes = [len(basin) for basin in basins]
    sizes.sort(reverse=True)
    three_largest_basins = prod(sizes[0:3])
    return (risk_level, three_largest_basins)

def find_basin(x, y, adjacents, in_basin, basin):
    for (value, i, j) in adjacents[x][y]:
        if in_basin[i][j] is None:
            if value == 9:
                in_basin[i][j] = False
            else:
                in_basin[i][j] = True
                basin.append(value)
                find_basin(i, j, adjacents, in_basin, basin)

test = parse_input("test.txt")
test_risk_level, test_largest_basins = calculate_lava_tubes(test)
assert test_risk_level == 15
assert test_largest_basins == 1134

data = parse_input("data.txt")
risk_level, largest_basins = calculate_lava_tubes(data)
print("Part 1: ", risk_level)
print("Part 2: ", largest_basins)