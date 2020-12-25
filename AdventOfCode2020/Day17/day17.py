from itertools import product
from operator import add

def find_neighbors(cube, dimension):
    neighbors = []
    for step in product([-1,0,1], repeat=dimension):
        if len([i for i in step if i == 0]) == dimension: continue
        neighbors.append(tuple(map(add, step, cube)))
    return neighbors

def parse_initial_cubes(input, dimension):
    active_cubes, y = set(), len(input.splitlines()) - 1
    for i, line in enumerate(input.splitlines()):
        for j, char in enumerate(line):
            value = [j, y - i] + [0] * (dimension - 2)
            if char == "#": active_cubes.add(tuple(value))
    return active_cubes

def process_cycle(active, dimension):
    new_set, neighbors = set(), {}
    for cube in active:
        for n in find_neighbors(list(cube), dimension):
            if n in neighbors: neighbors[n] += 1
            else: neighbors[n] = 1
    for cube, count in neighbors.items():
        if (cube not in active and count == 3) or (cube in active and count in [2,3]):
            new_set.add(cube)
    return new_set
        
def count_active(input, count, dimension):
    active_cubes = parse_initial_cubes(input, dimension)
    for _ in range(count):
        active_cubes = process_cycle(active_cubes, dimension)
    return len(active_cubes)

def test_input():
    input = """.#.
..#
###"""
    assert(count_active(input, 6, 3)) == 112
    assert(count_active(input, 6, 4)) == 848

if __name__ == "__main__":
    test_input()
    with open("data.txt") as file:
        input = file.read()
        print(count_active(input, 6, 3))
        print(count_active(input, 6, 4))