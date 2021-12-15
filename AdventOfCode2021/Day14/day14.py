from collections import Counter

def parse_input(file_name):
    with open(file_name) as file:
        template, rules = file.read().split("\n\n")
        rule_map = {}
        for rule in rules.splitlines():
            pair, element = rule.split(" -> ")
            rule_map[pair] = element
        return (template, rule_map)

def count_elements(template, rules, step_count) -> int:
    pair_count, letter_count = Counter(), Counter()
    for i in range(len(template) - 1):
        pair = template[i:i+2]
        pair_count[pair] += 1
    
    for letter in template:
        letter_count[letter] += 1

    for _ in range(step_count):
        updated = Counter()
        for pair, count in pair_count.items():    
            if pair not in rules: continue        
            letter = rules[pair]
            updated[pair[0] + letter] += count
            updated[letter + pair[1]] += count
            if letter in letter_count:
                letter_count[letter] += count
            else:
                letter_count[letter] = 1
        pair_count = updated

    result = letter_count.most_common()[0][1] - letter_count.most_common()[-1][1]
    return result

test_template, test_rules = parse_input("test.txt")
assert count_elements(test_template, test_rules, 10) == 1588
assert count_elements(test_template, test_rules, 40) == 2188189693529

template, rules = parse_input("data.txt")
print("Part 1: ", count_elements(template, rules, 10))
print("Part 1: ", count_elements(template, rules, 40))