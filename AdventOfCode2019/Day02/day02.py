from operator import add, mul

def run_program(input, replacements=[]):
    intcodes = [int(s) for s in input.split(",")]
    for i, v in replacements:
        intcodes[i] = v
    opcode_indexes = [c for c in range(len(intcodes)) if c%4 == 0]
    opcode_map = {1: add, 2: mul, 99: None}
    for index in opcode_indexes:
        code = intcodes[index]
        if opcode_map[code] is None or index > len(intcodes) - 4: 
            break
        next_indexes = intcodes[index+1:index+4]
        intcodes[next_indexes[2]] = opcode_map[code](intcodes[next_indexes[0]], intcodes[next_indexes[1]])
    return intcodes

test1 = "1,1,1,4,99,5,6,0,99"
assert(",".join([str(c) for c in run_program(test1)])) == "30,1,1,4,2,5,6,0,99"

test2 = "2,4,4,5,99,0"
assert(",".join([str(c) for c in run_program(test2)])) == "2,4,4,5,99,9801"

# part 1:
with open("data.txt") as file:
    data = file.read()
    result = run_program(data, [(1,12), (2,2)])
    print(result[0])

    # part 2 - ambiguous AF
    for x in range(100):
        for y in range(100):
            if run_program(data, [(1, x), (2, y)])[0] == 19690720:
                print(100*x+y)
                break
