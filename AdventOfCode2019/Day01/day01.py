def calculate_fuel(input, recursive):
    modules = [int(s) for s in input.splitlines()]
    if not recursive:
        return sum(m//3-2 for m in modules)
    else:
        total = 0
        for m in modules:
            fuel = m//3-2
            while fuel > 0:
                total += fuel
                fuel = fuel//3-2
        return total

assert(calculate_fuel("100756", False)) == 33583
assert(calculate_fuel("100756", True)) == 50346
with open("data.txt") as file:
    data = file.read()
    print(calculate_fuel(data, False))
    print(calculate_fuel(data, True))