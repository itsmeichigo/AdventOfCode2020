import re

def find_sum_values(rules):
    memory_map = {}
    for r in rules:
        if r[0:4] != "mask": r = "mask" + r
        mask = re.match(r"mask = ([X01]{36})", r).group(1)
        for i in re.findall(r"mem\[(\d+)\] = (\d+)", r):
            bin_str = bin(int(i[1])).replace("0b", "")
            updated = ["0"]*(len(mask) - len(bin_str)) + list(bin_str)
            for j, char in enumerate(mask):
                if char != "X": updated[j] = char
            memory_map[i[0]] = int("".join(updated), 2)
    return sum(v for v in memory_map.values())

def test_input_data():
    input = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""
    assert(find_sum_values([input])) == 165

if __name__ == "__main__":
    # test_input_data()
    with open("data.txt") as file:
        rules = re.split(r"\nmask", file.read())
        print(find_sum_values(rules))
    
    
