def parse_input(file_name):
    with open(file_name) as file:
        template, rules = file.read().split("\n\n")
        rule_map = {}
        for rule in rules.splitlines():
            pair, element = rule.split(" -> ")
            rule_map[pair] = element
        return (template, rule_map)

def count_elements(template, rules, step_count) -> int:
    element_map = {}
    for char in template:
        if char not in element_map:
            element_map[char] = 0
        element_map[char] += 1
    pairs = []
    for i in range(len(template) - 1):
        pairs.append(template[i:i+2])
    for pair in pairs:
        count_after_insertion(pair, step_count, rules, element_map)
    counts = list(element_map.values())
    counts.sort()
    return counts[-1] - counts[0]

def count_after_insertion(pair, step_count, rules, element_map):
    if pair not in rules or step_count == 0:
        return
    inserted_char = rules[pair]
    if inserted_char not in element_map:
        element_map[inserted_char] = 0
    element_map[inserted_char] += 1
    count_after_insertion(pair[0] + inserted_char, step_count - 1, rules, element_map)
    count_after_insertion(inserted_char + pair[1], step_count - 1, rules, element_map)

test_template, test_rules = parse_input("test.txt")
assert count_elements(test_template, test_rules, 10) == 1588
# assert count_elements(test_template, test_rules, 40) == 2188189693529

template, rules = parse_input("data.txt")
print("Part 1: ", count_elements(template, rules, 10))