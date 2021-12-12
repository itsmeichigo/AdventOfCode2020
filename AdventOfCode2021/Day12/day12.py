def parse_input(file_name):
    with open(file_name) as file:
        subpaths = {}
        for line in file.read().splitlines():
            origin, destiny = line.split("-")
            if origin in subpaths:
                subpaths[origin].append(destiny)
            else:
                subpaths[origin] = [destiny]
            if destiny == "end" or origin == "start":
                continue # do not add reverse path for start and end.
            if destiny in subpaths:
                subpaths[destiny].append(origin)
            else:
                subpaths[destiny] = [origin]
        return subpaths

def count_paths(input) -> int:
    total = 0
    for cave in input["start"]:
        total += find_paths(input, ["start", cave])
    return total

def find_paths(input, current_caves) -> int:
    last_cave = current_caves[-1]
    total = 0
    for next_cave in input[last_cave]:
        if next_cave.islower() and next_cave in current_caves:
            continue
        if next_cave == "end":
            total += 1
            continue
        copy = current_caves.copy()
        copy.append(next_cave)
        total += find_paths(input, copy)
    return total

tests = {"test1.txt": 10, "test2.txt": 19, "test3.txt": 226}
for test, result in tests.items():
    input = parse_input(test)
    assert(count_paths(input)) == result

data = parse_input("data.txt")
print("Part 1: ", count_paths(data))