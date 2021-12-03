from typing import List, Tuple

def parse_input(file_name) -> List[str]:
    with open(file_name) as file:
        return file.read().splitlines()

def calculate_statistics(input) -> Tuple[int, int]:
    most_common_bits, least_common_bits = calculate_bits(input)
    power_consumption = int("".join(most_common_bits), 2) * int("".join(least_common_bits), 2)
 
    oxygen_generator_rating = filter_by_bit_criteria(input, True)
    co2_scrubber_rating = filter_by_bit_criteria(input, False)
    life_support_rating = int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2)
    return (power_consumption, life_support_rating)

def filter_by_bit_criteria(input, is_most_common, current_index=0) -> str:
    if len(input) == 1:
        return input[0]
    candidates = []
    most_common_bits, least_common_bits = calculate_bits(input)
    criteria = most_common_bits if is_most_common else least_common_bits
    for line in input:
        if line[current_index] == criteria[current_index]:
            candidates.append(line)
    return filter_by_bit_criteria(candidates, is_most_common, current_index + 1)

def calculate_bits(input):
    bit_count = [{"0": 0, "1": 0} for i in range(len(input[0]))]
    for line in input:
        for i in range(len(line)):
            current_count = bit_count[i]
            if line[i] == "0": current_count["0"] += 1
            elif line[i] == "1": current_count["1"] += 1
            bit_count[i] = current_count
    most_common_bits = ["1" if bit["1"] >= bit["0"] else "0" for bit in bit_count]
    least_common_bits = ["1" if bit["1"] < bit["0"] else "0" for bit in bit_count]
    return (most_common_bits, least_common_bits)

test_input = parse_input("test.txt")
assert calculate_statistics(test_input) == (198, 230)

real_input = parse_input("data.txt")
power_consumption, life_support_rating = calculate_statistics(real_input)
print("Part 1: ", power_consumption)
print("Part 2:", life_support_rating)
