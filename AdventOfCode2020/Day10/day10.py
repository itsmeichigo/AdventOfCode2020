from math import factorial

def count_differences(adapters):
    one_count, three_count = 0, 0
    current_rating = 0
    adapters.sort()
    for x in set(adapters):
        if x - current_rating == 1: 
            one_count += 1
        elif x - current_rating == 3:
            three_count += 1
        current_rating = x
    return one_count * (three_count + 1)

def count_arrangements(adapters):
    adapters.sort()
    complete_list = [0] + list(set(adapters)) + [max(adapters) + 3]
    times = 1
    left, right = 0, 0
    while left < len(complete_list) - 1 and right < len(complete_list) - 1:
        while complete_list[right + 1] - complete_list[right] == 1:
            right += 1
        times *= count_combination(complete_list[left:right+1])
        right += 1
        left = right
    return times

def count_combination(adapters):
    if len(adapters) == 3:
        return 2
    elif len(adapters) > 3:
        result = 1 + len(adapters) - 2 + int(factorial(len(adapters) - 2) / 2)
        return result
    return 1

with open("data.txt") as file:
    adapters = [int(i) for i in file.read().splitlines()]
    print(count_differences(adapters))
    print(count_arrangements(adapters))