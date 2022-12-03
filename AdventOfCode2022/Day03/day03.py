import string

letters = list(string.ascii_lowercase)

def calculate_priority(rucksack):
    size = len(rucksack)//2
    first, second = set(rucksack[:size]), set(rucksack[size:])
    duplicate = list(first & second)[0]
    index = letters.index(duplicate.lower())
    return index + 1 if duplicate.islower() else index + 1 + len(letters)

with open("input.txt") as file:
    lines = file.read().splitlines()
    total_priorities = sum([calculate_priority(list(r)) for r in lines])
    print(total_priorities)
    