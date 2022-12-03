import string

def calculate_incorrect_item(rucksack):
    size = len(rucksack)//2
    first, second = set(rucksack[:size]), set(rucksack[size:])
    duplicate = list(first & second)[0]
    return calculate_priority(duplicate)

def calculate_group(group):
    sets = [set(i) for i in group]
    shared_item = list(sets[0] & sets[1] & sets[2])[0]
    return calculate_priority(shared_item)

def calculate_priority(item):
    letters = list(string.ascii_lowercase)
    index = letters.index(item.lower())
    return index + 1 if item.islower() else index + 1 + len(letters)

with open("input.txt") as file:
    lines = file.read().splitlines()
    total_incorrect_item = sum(calculate_incorrect_item(list(r)) for r in lines)
    print(total_incorrect_item)

    total_groups = 0
    for i in range(0, len(lines), 3):
        total_groups += calculate_group(lines[i:i+3])
    print(total_groups)    