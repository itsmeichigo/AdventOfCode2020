def parse_input(file_name):
    with open(file_name) as file:
        template, rules = file.read().split("\n\n")
        rule_map = {}
        for rule in rules.splitlines():
            pair, element = rule.split(" -> ")
            rule_map[pair] = element
        return (template, rule_map)

def execute_insertion(template, rules, step_count) -> str:
    current, updated = template, template
    for _ in range(step_count):
        added_count = 0
        for i in range(len(current) - 1):
            substring = current[i:i+2]
            if substring in rules:
                updated = updated[:i+1+added_count] + rules[substring] + updated[i+1+added_count:]
                added_count += 1
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