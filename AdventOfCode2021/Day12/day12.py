def parse_input(file_name):
    with open(file_name) as file:
        subpaths = {}
        for line in file.read().splitlines():
            origin, destiny = line.split("-")
            if destiny != "start": # ignore start as destiny
                if origin not in subpaths:
                    subpaths[origin] = []
                subpaths[origin].append(destiny)
            if destiny != "end" and origin != "start":
                if destiny not in subpaths:
                    subpaths[destiny] = []
                subpaths[destiny].append(origin)
        return subpaths

def count_paths(input, allows_visiting_twice) -> int:
    total = 0
    for cave in input["start"]:
        total += find_paths(input, ["start", cave], allows_visiting_twice)
    return total

def find_paths(input, current_caves, allows_visiting_twice) -> int:
    last_cave = current_caves[-1]
    total = 0
    for next_cave in input[last_cave]:
        if next_cave == "end":
            total += 1
            continue
        if next_cave.isupper() or next_cave not in current_caves:
            total += find_paths(input, current_caves + [next_cave], allows_visiting_twice)
    if allows_visiting_twice:
        for next_cave in input[last_cave]:
            if next_cave.islower() and next_cave in current_caves:
                total += find_paths(input, current_caves + [next_cave], False)
    return total

tests = {"test1.txt": 10, "test2.txt": 19, "test3.txt": 226}
for test, result in tests.items():
    input = parse_input(test)
    assert(count_paths(input, False)) == result
    if test == "test1.txt":
        assert(count_paths(input, True)) == 36

data = parse_input("data.txt")
print("Part 1: ", count_paths(data, False))
print("Part 2: ", count_paths(data, True))