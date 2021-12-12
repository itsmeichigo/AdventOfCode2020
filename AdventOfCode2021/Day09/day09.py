def parse_input(file_name):
    with open(file_name) as file:
        return [[int(n) for n in line] for line in file.read().splitlines()]

def find_low_points(input) -> int:
    result = 0
    width, height = len(input[0]), len(input)
    for x in range(height):
        for y in range(width):
            adjacents = []
            if x-1 >= 0: adjacents.append(input[x-1][y])
            if x+1 < height: adjacents.append(input[x+1][y])
            if y-1 >= 0: adjacents.append(input[x][y-1])
            if y+1 < width: adjacents.append(input[x][y+1])
            if len([n for n in adjacents if n > input[x][y]]) == len(adjacents):
                result += (1 + input[x][y])
    return result

test = parse_input("test.txt")
assert find_low_points(test) == 15

data = parse_input("data.txt")
print("Part 1: ", find_low_points(data))