from collections import deque

def construct_stacks(crates):
    lines = crates.splitlines()[:-1] # removes the last line as we don't need it
    stack_count = len(lines[-1].split(" "))
    stacks = [deque() for i in list(range(0, stack_count))]
    for line in reversed(lines):
        items = [line[i:i+4] for i in range(0, len(line), 4)]
        for index, item in list(enumerate(items)):
            if "[" in item:
                stacks[index].append(item[1]) # adds the crate name only
    return stacks

def move_stacks(stacks, steps, one_by_one=True):
    for step in steps.splitlines():
        count, origin, destination = [int(s) for s in step.split(" ") if s.isnumeric()]
        new_stack = deque()
        while count > 0:
            item = stacks[origin-1].pop()
            if one_by_one:
                stacks[destination-1].append(item)
            else:
                new_stack.append(item)
            count -= 1
        if not one_by_one:
            while len(new_stack) > 0:
                item = new_stack.pop()
                stacks[destination-1].append(item)
    return stacks

def get_top_items(stacks):
    return "".join([stack.pop() for stack in stacks])

with open("input.txt") as file:
    crates, steps = file.read().split("\n\n")
    one_by_one_stacks = move_stacks(construct_stacks(crates), steps)
    print(get_top_items(one_by_one_stacks))

    advanced_stacks = move_stacks(construct_stacks(crates), steps, one_by_one=False)
    print(get_top_items(advanced_stacks))



