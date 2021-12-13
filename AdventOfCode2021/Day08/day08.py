def parse_input(file_name):
    with open(file_name) as file:
        parsed = []
        for line in file.read().splitlines():
            patterns_str, digits_str = line.split(" | ")
            patterns = patterns_str.split(" ")
            digits = digits_str.split(" ")
            parsed.append((patterns, digits))
        return parsed

def count_digits_with_unique_number_of_segments(input):
    total = 0
    for (_, digits) in input:
        total += len([d for d in digits if len(d) in [2, 4, 3, 7]])
    return total

test = parse_input("test.txt")
assert count_digits_with_unique_number_of_segments(test) == 26

data = parse_input("data.txt")
print("Part 1: ", count_digits_with_unique_number_of_segments(data))