from typing import List, Tuple

def parse_input(filename) -> List[str]:
    with open(filename) as file:
        return file.read().splitlines()

def check_brackets(input) -> Tuple[int, int]:
    corrupted_point, complete_points = 0, []
    matching_brackets = {"]": "[", "[": "]", "}": "{", "{": "}", ")": "(", "(": ")", ">": "<", "<": ">"}
    corrupted_map = {")": 3, "]": 57, "}": 1197, ">": 25137}
    complete_map = {")": 1, "]": 2, "}": 3, ">": 4}
    for line in input:
        brackets = []
        corrupted = False
        for char in line:
            if char in "[({<":
                brackets.append(char)
            else:
                if matching_brackets[char] == brackets[-1]:
                    brackets.pop(-1)
                else:
                    corrupted_point += corrupted_map[char]
                    corrupted = True
                    break
        if corrupted: continue
        score = 0
        for i in range(len(brackets) - 1, -1, -1):
            matching = matching_brackets[brackets[i]]
            score *= 5
            score += complete_map[matching]
        complete_points.append(score)

    complete_points.sort()
    middle_index = int(len(complete_points) / 2)
    return (corrupted_point, complete_points[middle_index])

test_input = parse_input("test.txt")
assert check_brackets(test_input) == (26397, 288957)

data = parse_input("data.txt")
result = check_brackets(data)
print("Part 1: ", result[0])
print("Part 2: ", result[1])