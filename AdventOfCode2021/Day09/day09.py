def parse_input(file_name):
    with open(file_name) as file:
        return [[int(n) for n in line] for line in file.read().splitlines()]

def find_adjacents(input):
    adjacents = [[[] for n in line] for line in input]
    width, height = len(input[0]), len(input)
    for x in range(height):
        for y in range(width):
            current = adjacents[x][y]
            if x-1 >= 0: current.append(input[x-1][y])
            if x+1 < height: current.append(input[x+1][y])
            if y-1 >= 0: current.append(input[x][y-1])
            if y+1 < width: current.append(input[x][y+1])
    return adjacents

def calculate_risk_level(input) -> int:
    risk_level = 0
    width, height = len(input[0]), len(input)
    adjacents = find_adjacents(input)
    for x in range(height):
        for y in range(width):
            if len([n for n in adjacents[x][y] if n > input[x][y]]) == len(adjacents[x][y]):
                risk_level += (1 + input[x][y])
    return risk_level

test = parse_input("test.txt")
assert calculate_risk_level(test) == 15

data = parse_input("data.txt")
print("Part 1: ", calculate_risk_level(data))