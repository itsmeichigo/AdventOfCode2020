with open("data.txt") as file:
    input = file.read()
    calories = sorted([sum([int(i) for i in e.splitlines()]) for e in input.split("\n\n")])
    print(calories[-1])
    print(sum(calories[-3:]))