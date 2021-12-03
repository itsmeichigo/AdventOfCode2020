from typing import List

def parse_input(file_name) -> List[str]:
    with open(file_name) as file:
        return file.read().splitlines()

def calculate_power_consumption(input) -> int:
    gamma_rate = [get_outstanding_bit(input, True, i) for i in range(len(input[0]))]
    epsilon_rate = [get_outstanding_bit(input, False, i) for i in range(len(input[0]))]
    return int("".join(gamma_rate), 2) * int("".join(epsilon_rate), 2)

def calculate_life_support_rating(input) -> int:
    oxygen_generator_rating = filter_by_bit_criteria(input, True)
    co2_scrubber_rating = filter_by_bit_criteria(input, False)
    return int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2)

def filter_by_bit_criteria(input, is_most_common, current_index=0) -> str:
    if len(input) == 1:
        return input[0]
    candidates = []
    for line in input:
        if line[current_index] == get_outstanding_bit(input, is_most_common, current_index):
            candidates.append(line)
    return filter_by_bit_criteria(candidates, is_most_common, current_index + 1) 

def get_outstanding_bit(input, is_most_common, index) -> str:
    ones, zeros = 0, 0
    for line in input:
        if line[index] == "0": zeros += 1
        else: ones += 1
    if is_most_common: 
        return "1" if ones >= zeros else "0"
    else:
        return "1" if ones < zeros else "0"

test_input = parse_input("test.txt")
assert calculate_power_consumption(test_input) == 198
assert calculate_life_support_rating(test_input) == 230

real_input = parse_input("data.txt")
print("Part 1: ", calculate_power_consumption(real_input) )
print("Part 2:", calculate_life_support_rating(real_input))
