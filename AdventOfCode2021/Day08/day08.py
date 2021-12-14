def parse_input(file_name):
    with open(file_name) as file:
        parsed = []
        for line in file.read().splitlines():
            patterns_str, digits_str = line.split(" | ")
            patterns = patterns_str.split(" ")
            digits = digits_str.split(" ")
            parsed.append((patterns, digits))
        return parsed

def calculate_total_output(input):
    total = 0
    for (patterns, digits) in input:
        map = decode_pattern_map(patterns)
        decoded_digits = []
        for d in digits:
            candidates = [p for p in map.keys() if len(p) == len(d)]
            if len(candidates) == 1:
                decoded_digits.append(str(map[candidates[0]]))
                continue
            for p in candidates:
                if set(list(d)) == set(list(p)):
                    decoded_digits.append(str(map[p]))
                    break
        total += int("".join(decoded_digits))
    return total

def decode_pattern_map(patterns):
    pmap = {}
    one = [p for p in patterns if len(p) == 2][0]
    pmap[one] = 1
    right_strokes = set(list(one))

    five_char_patterns, six_char_patterns = set(), set()
    top_left_and_mid_strokes = set()
    for p in patterns:
        length = len(p)
        if length == 3: pmap[p] = 7
        elif length == 4: 
            pmap[p] = 4
            top_left_and_mid_strokes = set([s for s in list(p) if s not in right_strokes])
        elif length == 7: pmap[p] = 8
        elif length == 5: five_char_patterns.add(p)
        elif length == 6: six_char_patterns.add(p)
    for p in five_char_patterns:
        chars = set(list(p))
        if right_strokes.issubset(chars):
            pmap[p] = 3
        elif top_left_and_mid_strokes.issubset(chars):
            pmap[p] = 5
        else: pmap[p] = 2
    for p in six_char_patterns:
        chars = set(list(p))
        if right_strokes.issubset(chars) and top_left_and_mid_strokes.issubset(chars):
            pmap[p] = 9
        elif top_left_and_mid_strokes.issubset(chars):
            pmap[p] = 6
        else: pmap[p] = 0
    return pmap
            

def count_digits_with_unique_number_of_segments(input):
    total = 0
    for (_, digits) in input:
        total += len([d for d in digits if len(d) in [2, 4, 3, 7]])
    return total

test = parse_input("test.txt")
assert count_digits_with_unique_number_of_segments(test) == 26
assert calculate_total_output(test) == 61229

data = parse_input("data.txt")
print("Part 1: ", count_digits_with_unique_number_of_segments(data))
print("Part 2: ", calculate_total_output(data))