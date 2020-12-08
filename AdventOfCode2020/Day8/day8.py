import re

def calulate_loop_acc(steps):
    current_index, acc = 0, 0
    visited = []
    while current_index not in visited and current_index is not None:
        visited.append(current_index)
        current_index, acc = move_next(steps, current_index, acc)
    return (current_index, acc)

def fix_program(steps):
    for index, step in enumerate(steps):
        if step[0] != "acc":
            start, acc = calulate_loop_acc(switch_op(steps, index))
            if start is None:
                return acc
    return -1

def switch_op(steps, index):
    copy = steps.copy()
    new_op = "jmp" if steps[index][0] == "nop" else "nop"
    copy[index] = (new_op, steps[index][1])
    return copy

def move_next(steps, current_index, acc):
    if current_index >= len(steps):
        return (None, acc)
    instr, num = steps[current_index]
    signedNum = int(num)

    if instr == "nop":
        return (current_index + 1, acc)
    elif instr == "acc":
        return (current_index + 1, acc + signedNum)
    else:
        return (current_index + signedNum, acc)
    
steps = []
with open("data.txt") as file:
    for x in file.readlines():
        steps.extend(re.findall(r"(.{3}) ([+-]\d+)", x))
    print(calulate_loop_acc(steps)[1])
    print(fix_program(steps))
