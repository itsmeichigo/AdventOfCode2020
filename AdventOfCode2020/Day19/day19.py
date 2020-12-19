import re

def count_match(input):
    rules, messages = input.split("\n\n")
    pattern = re.compile(build_regex_pattern(rules))
    return sum(1 for m in messages.splitlines() if pattern.match(m))

def build_regex_pattern(rules):
    pattern = "^"
    pattern_map = {}
    for l in rules.splitlines():
        key, content = re.match(r"(\d+): (.+)", l).group(1,2)
        pattern_map[key] = content
    for rule in pattern_map["0"].split():
        pattern += find_rule_content(pattern_map, rule)
    return pattern + "$"

def find_rule_content(pattern_map, rule):
    if re.compile(r"\"([ab]+)\"").match(pattern_map[rule]): # e.g "a"
        return pattern_map[rule].replace("\"", "")
    pattern = "("
    needs_wrapping = False
    for s in pattern_map[rule].split():
        if s == "|": 
            pattern += ")|("
            needs_wrapping = True
        elif s.isdigit(): pattern += find_rule_content(pattern_map, s)
        else: raise ValueError("Uncaught exception for rule: ", s)
    pattern += ")"
    return pattern if not needs_wrapping else "(" + pattern + ")"

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
        print(count_match(file.read()))