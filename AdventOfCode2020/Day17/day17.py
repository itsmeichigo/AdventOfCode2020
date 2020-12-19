def find_neighbors(cube):
    neighbors = []
    for a in [-1,1,0]:
        for b in [-1,1,0]:
            for c in [-1,1,0]:
                if a == 0 and b == 0 and c == 0: continue
                neighbors.append([cube[0]+a, cube[1]+b, cube[2]+c])
    return neighbors

def parse_initial_cubes(input):
    cubes, z, y = [], 0, len(input.splitlines()) - 1
    for i, line in enumerate(input.splitlines()):
        for j, char in enumerate(line):
            if char == "#": 
                cubes.append([j, y - i, z])
    return cubes

def process_cycle(active):
    result = []
    for cube in active:
        neighbors = find_neighbors(cube)
        active_neighbors = [c for c in neighbors if c in active]
        nonactive_neighbors = [c for c in neighbors if c not in active]
        if len(active_neighbors) == 2 or len(active_neighbors) == 3:
            result.append(cube)
        for cube in nonactive_neighbors:
            if len([c for c in find_neighbors(cube) if c in active]) == 3 and cube not in result:
                result.append(cube)
    return result

def count_active(input, count):
    active = parse_initial_cubes(input)
    i = 0
    while i < count:
        active = process_cycle(active)
        i += 1
    return len(active)

def test_input():
    input = """.#.
..#
###"""
    assert(count_active(input, 6)) == 112

if __name__ == "__main__":
    test_input()
    with open("data.txt") as file:
        print(count_active(file.read(), 6))