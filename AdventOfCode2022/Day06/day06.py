from collections import deque

def calculate_numbers_before_distinct_group(input, length):
    index, group = 0, deque()
    while index < len(input):
        if len(group) == length:
            group.popleft()
        group.append(input[index])       
        if len(set(group)) == length:
            break
        index += 1
    return index + 1

with open("input.txt") as file:
    input = list(file.read())
    print(calculate_numbers_before_distinct_group(input, 4))
    print(calculate_numbers_before_distinct_group(input, 14))
