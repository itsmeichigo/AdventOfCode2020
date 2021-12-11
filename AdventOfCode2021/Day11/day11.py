from typing import List

def parse_input(file_name) -> List[List[int]]:
    with open(file_name) as file:
        return [[int(n) for n in list(line)] for line in file.read().splitlines()]

def count_flashes(input, total_steps) -> int:
    flash_count, width, height = 0, len(input[0]), len(input)
    copy = input.copy()
    for _ in range(total_steps):
        for x in range(width):
            for y in range(height):
                increase_energy(copy, x, y)
        flash_count += sum([sum([1 for n in line if n > 9]) for line in copy])
        copy = [[0 if n > 9 else n for n in line] for line in copy]
    return flash_count 

def find_step_for_all_flashes(input) -> int:
    step, width, height = 1, len(input[0]), len(input)
    copy = input.copy()
    while(True):
        step += 1
        for x in range(width):
            for y in range(height):
                increase_energy(copy, x, y)
        flash_count = sum([sum([1 for n in line if n > 9]) for line in copy])
        if flash_count == width * height:
            return step
        copy = [[0 if n > 9 else n for n in line] for line in copy]

def increase_energy(input, x, y):
    if input[x][y] > 9:
        return # no need to increase more

    input[x][y] += 1
    if input[x][y] > 9:
        if x - 1 >= 0:
            increase_energy(input, x-1, y)
        if y - 1 >= 0:
            increase_energy(input, x, y-1)
        if y + 1 < len(input):
            increase_energy(input, x, y+1)
        if x + 1 < len(input[0]):
            increase_energy(input, x+1, y)
        if x - 1 >= 0 and y - 1 >= 0:
            increase_energy(input, x-1, y-1)
        if x + 1 < len(input[0]) and y + 1 < len(input):
            increase_energy(input, x+1, y+1)
        if x - 1 >= 0 and y + 1 < len(input):
            increase_energy(input, x-1, y+1)
        if x + 1 < len(input[0]) and y - 1 >= 0:
            increase_energy(input, x+1, y-1)

demo_input = parse_input("demo.txt")
assert count_flashes(demo_input, 2) == 9

test_input = parse_input("test.txt")
assert count_flashes(test_input, 100) == 1656
assert find_step_for_all_flashes(test_input) == 195

data = parse_input("data.txt")
print("Part 1: ", count_flashes(data, 100))
print("Part 2: ", find_step_for_all_flashes(data))