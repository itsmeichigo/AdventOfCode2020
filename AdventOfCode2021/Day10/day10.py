from typing import List

def parse_input(filename) -> List[str]:
    with open(filename) as file:
        return file.read().splitlines()

def calculate_corrupted_lines(input) -> int:
    points = 0
    matching_brackets = {"]": "[", "}": "{", ")": "(", ">": "<"}
    corrupted_points = {")": 3, "]": 57, "}": 1197, ">": 25137}
    for line in input:
        brackets = []
        for char in line:
            if char in "[({<":
                brackets.append(char)
            else:
                if matching_brackets[char] == brackets[-1]:
                    brackets.pop(-1)
                else:
                    points += corrupted_points[char]
                    break

    return points

test_input = parse_input("test.txt")
assert calculate_corrupted_lines(test_input) == 26397

data = parse_input("data.txt")
print("Part 1: ", calculate_corrupted_lines(data))