from itertools import product
from operator import add

def find_neighbors(cube, dimension):
    neighbors = []
    for step in product([-1,0,1], repeat=dimension):
        if len([i for i in step if i == 0]) == dimension: continue
        neighbors.append(tuple(map(add, step, cube)))
    return neighbors

def parse_initial_cubes(input, dimension):
    state, y = {}, len(input.splitlines()) - 1
    for i, line in enumerate(input.splitlines()):
        for j, char in enumerate(line):
            value = [j, y - i] + [0] * (dimension - 2)
            state[tuple(value)] = char
    return state

def process_cycle(state, dimension):
    new_state = {}
    for k in list(state): # expand space to check later
        for n in find_neighbors(list(k), dimension):
            if tuple(n) not in state: state[tuple(n)] = "."
    for k, v in state.items():
        active = 0
        for n in find_neighbors(list(k), dimension):
            if state.get(tuple(n), ".") == "#": active += 1
        if v == "#" and active in [2,3]: new_state[k] = "#"
        elif v == "." and active == 3: new_state[k] = "#"
        else: new_state[k] = "."
    return new_state
        
def count_active(input, count, dimension):
    state, i = parse_initial_cubes(input, dimension), 0
    while i < count:
        state = process_cycle(state, dimension)
        i += 1
    return len([k for k, v in state.items() if v == "#"])

def test_input():
    input = """.#.
..#
###"""
    assert(count_active(input, 6, 3)) == 112
    assert(count_active(input, 6, 4)) == 848

if __name__ == "__main__":
    test_input()
    with open("data.txt") as file:
        print(count_active(file.read(), 6, 3))
        print(count_active(file.read(), 6, 4))