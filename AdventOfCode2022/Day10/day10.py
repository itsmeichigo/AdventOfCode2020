with open("input.txt") as file:
    instructions = file.read().splitlines()
    current_value, pending_value = 1, None
    instruction_index, total = 0, 0
    cycles = [20, 60, 100, 140, 180, 220]
    pixels = [["." for i in range(40)] for j in range(6)]
    for cycle in range(1, 241):
        if (cycle-1)%40 in range(current_value-1, current_value+2):
            pixels[(cycle - 1)//40][(cycle - 1)%40] = "#"
        if cycle in cycles:
            total += current_value * cycle
        if pending_value is not None:
            current_value += pending_value
            pending_value = None
            instruction_index += 1
        elif instructions[instruction_index] == "noop":
            instruction_index += 1
        else:
            i = instructions[instruction_index]
            pending_value = int(i.split(" ")[1])
    print(total)
    image = "\n".join(["".join(line) for line in pixels])
    print(image)
