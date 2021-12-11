from typing import List

def parse_input(file_name) -> List[int]:
    with open(file_name) as file:
        return [int(n) for n in file.read().split(",")]

def count_fish(initial_timer, period) -> int:
    new_spawn_start_timer = 9
    reset_start_timer = 6
    fish_at_day = [0] * new_spawn_start_timer

    for fish in initial_timer:
        fish_at_day[fish] += 1

    for _ in range(period):
        spawn = fish_at_day.pop(0)
        fish_at_day.append(spawn)
        fish_at_day[reset_start_timer] += spawn

    return sum(fish_at_day)

test_input = parse_input("test.txt")
assert count_fish(test_input, 18) == 26
assert count_fish(test_input, 80) == 5934

actual_input = parse_input("data.txt")
print("Part 1: ", count_fish(actual_input, 80))
print("Part 2: ", count_fish(actual_input, 256))