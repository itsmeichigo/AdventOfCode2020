import re

def calulate_loop_acc(steps):
    left, left_acc = 0, 0
    right, right_acc = find_loop_start(steps)
    while True:
        left, left_acc = move_next(steps, left, left_acc)
        right, right_acc = move_next(steps, right, right_acc)
        if left == right:
            break
    return right_acc

def fix_program(steps):
    for index, step in enumerate(steps):
        if step[0] != "acc":
            start, acc = find_loop_start(switch_op(steps, index))
            if start is None:
                return acc
    return -1

def switch_op(steps, index):
    copy = steps.copy()
    new_op = "jmp" if steps[index][0] == "nop" else "nop"
    copy[index] = (new_op, steps[index][1])
    return copy

def find_loop_start(steps):
    slow, fast, slow_acc, fast_acc = 0, 0, 0, 0
    while True and fast is not None:
        slow, slow_acc = move_next(steps, slow, slow_acc)
        fast, fast_acc = move_next(steps, fast, fast_acc)
        if fast is None:
            break
        fast, fast_acc = move_next(steps, fast, fast_acc)
        if slow == fast:
            break
    if fast is None:
        return (None, fast_acc)
    return (slow, slow_acc)

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
    print(calulate_loop_acc(steps))
    print(fix_program(steps))
