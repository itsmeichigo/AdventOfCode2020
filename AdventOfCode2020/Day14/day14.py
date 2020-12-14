import re

def find_sum_values_v1(rules):
    memory_map = {}
    for r in rules:
        mask, mem_info = parse_rule(r)
        for m in mem_info:
            updated = list(format(int(m[1]), "036b"))
            for j, char in enumerate(mask):
                if char != "X": updated[j] = char
            memory_map[m[0]] = int("".join(updated), 2)
    return sum(memory_map.values())

def find_sum_values_v2(rules):
    memory_map = {}
    for r in rules: 
        mask, mem_info = parse_rule(r)
        options = [format(x, "0{}b".format(mask.count("X"))) for x in range(pow(2, mask.count("X")))]
        for m in mem_info:
            raw = list(format(int(m[0]), "036b"))
            for j, char in enumerate(mask):
                if char != "0": raw[j] = char

            for o in options:
                o_chars = list(o)
                copy = raw.copy()
                for k, char in enumerate(copy):
                    if char == "X": 
                        copy[k] = o_chars[0]
                        o_chars = o_chars[1:]
                memory_map[int("".join(copy), 2)] = int(m[1])
    return sum(memory_map.values())
        
def parse_rule(r):
    if r[0:4] != "mask": r = "mask" + r
    mask = re.match(r"mask = ([X01]{36})", r).group(1)
    mem_info = re.findall(r"mem\[(\d+)\] = (\d+)", r)
    return mask, mem_info

def test_input_data():
    input1 = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""
    assert(find_sum_values_v1([input1])) == 165

    input2 = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""
    rules = re.split(r"\nmask", input2)
    assert(find_sum_values_v2(rules)) == 208

if __name__ == "__main__":
    test_input_data()
    with open("data.txt") as file:
        rules = re.split(r"\nmask", file.read())
        print(find_sum_values_v1(rules))
        print(find_sum_values_v2(rules))