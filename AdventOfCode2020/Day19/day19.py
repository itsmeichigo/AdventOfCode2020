import re

def count_match(input):
    rules, messages = input.split("\n\n")
    pattern = re.compile(build_regex_pattern(rules))
    return sum(1 for m in messages.splitlines() if pattern.match(m))

def build_regex_pattern(rules):
    pattern_map, cache = {}, {}
    for l in rules.splitlines():
        key, content = re.match(r"(\d+): (.+)", l).group(1,2)
        pattern_map[key] = content
    return "^" + find_rule_content(pattern_map, "0", cache) + "$"

def find_rule_content(pattern_map, rule, cache, depth = 0):
    if rule in cache: return cache[rule]
    result = ""
    if re.compile(r"\"([ab]+)\"").match(pattern_map[rule]): # e.g "a"
        result = pattern_map[rule].replace("\"", "")
    else:
        pattern = "("
        pipe_index = None
        for i, s in enumerate(pattern_map[rule].split()):
            if s == "|": 
                pattern += ")|("
                pipe_index = i
            elif s.isdigit(): 
                if s == rule and pipe_index is not None: # found loop
                    depth += 1
                    if depth != 10: # hardcoding max depth
                        pattern += find_rule_content(pattern_map, s, cache, depth)
                else: pattern += find_rule_content(pattern_map, s, cache)
            else: raise ValueError("Uncaught exception for rule: ", s)
        pattern += ")"
        result = pattern if pipe_index is None else "(" + pattern + ")"
    cache[rule] = result
    return result

def test_input():
    test1 = """0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb"""
    assert(count_match(test1)) == 2

if __name__ == "__main__":
    test_input()
    with open("data.txt") as file:
        original = file.read()
        print(count_match(original))
        updated = original.replace("8: 42", "8: 42 | 42 8")
        updated = updated.replace("11: 42 31", "11: 42 31 | 42 11 31")
        print(count_match(updated))