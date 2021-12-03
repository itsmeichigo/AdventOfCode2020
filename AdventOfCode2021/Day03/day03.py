from typing import List, Dict

def parse_input(file_name) -> List[str]:
    with open(file_name) as file:
        return file.read().splitlines()

def calculate_power_consumption(input) -> int:
    gamma_rate = "".join(get_most_common_bits(input))
    epsilon_rate = "".join(get_least_common_bits(input))
    return int(gamma_rate, 2) * int(epsilon_rate, 2)

def calculate_life_support_rating(input) -> int:
    oxygen_generator_rating = filter_by_bit_criteria(input, True)
    co2_scrubber_rating = filter_by_bit_criteria(input, False)
    return int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2)

def filter_by_bit_criteria(input, is_most_common, current_index=0) -> str:
    if len(input) == 1:
        return input[0]
    candidates = []
    criteria = get_most_common_bits(input) if is_most_common else get_least_common_bits(input)
    for line in input:
        if line[current_index] == criteria[current_index]:
            candidates.append(line)
    return filter_by_bit_criteria(candidates, is_most_common, current_index + 1)

def get_most_common_bits(input) -> List[str]:
    return ["1" if bit["1"] >= bit["0"] else "0" for bit in calculate_bits(input)]

def get_least_common_bits(input) -> List[str]:
    return ["1" if bit["1"] < bit["0"] else "0" for bit in calculate_bits(input)]

def calculate_bits(input) -> List[Dict]:
    bit_count = [{"0": 0, "1": 0} for i in range(len(input[0]))]
    for line in input:
        for i in range(len(line)):
            current_count = bit_count[i]
            if line[i] == "0": current_count["0"] += 1
            elif line[i] == "1": current_count["1"] += 1
            bit_count[i] = current_count
    return bit_count

test_input = parse_input("test.txt")
assert calculate_power_consumption(test_input) == 198
assert calculate_life_support_rating(test_input) == 230

real_input = parse_input("data.txt")
print("Part 1: ", calculate_power_consumption(real_input) )
print("Part 2:", calculate_life_support_rating(real_input))
