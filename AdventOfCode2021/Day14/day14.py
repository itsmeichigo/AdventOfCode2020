def parse_input(file_name):
    with open(file_name) as file:
        template, rules = file.read().split("\n\n")
        rule_map = {}
        for rule in rules.splitlines():
            pair, element = rule.split(" -> ")
            rule_map[pair] = pair[0] + element + pair[1]
        return (template, rule_map)

def execute_insertion(template, rules, step_count) -> str:
    current = template
    for _ in range(step_count):
        new_groups = []
        for i in range(len(current) - 1):
            substring = current[i:i+2]
            if substring in rules:
                new_groups.append(rules[substring])
        updated = ""
        for group in new_groups:
            if len(updated) == 0: updated = group
            else:
                updated = updated[:-1] + group
        current = updated
    return current

def count_elements(input) -> int:
    element_map = {}
    for char in input:
        if char not in element_map:
            element_map[char] = 0
        element_map[char] += 1
    counts = list(element_map.values())
    counts.sort()
    return counts[-1] - counts[0]

test_template, test_rules = parse_input("test.txt")
test_output_10 = execute_insertion(test_template, test_rules, 10)
assert count_elements(test_output_10) == 1588
test_output_40 = execute_insertion(test_template, test_rules, 40)
assert count_elements(test_output_40) == 2188189693529

template, rules = parse_input("data.txt")
after_step_10 = execute_insertion(template, rules, 10)
print("Part 1: ", count_elements(after_step_10))