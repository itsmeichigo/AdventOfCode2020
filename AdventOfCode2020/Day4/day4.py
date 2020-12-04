import re

def count_valid_passports(inputs, rule_check):
    return sum([1 for x in inputs if rule_check(x)])

def check_basic_rule(input):
    required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    fields = [re.split(":", x)[0] for x in input.split()]
    return len([x for x in fields if x in required]) == len(required)

def check_strict_rule(input):
    rules = {
        "byr": "^(19[2-9][0-9])|(200[0-2])$",
        "iyr": "^(201[0-9])|(2020)$",
        "eyr": "^(202[0-9])|(2030)$",
        "hgt": "^(1[5-8][0-9]cm)|(19[0-3]cm)|(59in)|(6[0-9]in)|(7[0-6]in)$",
        "hcl": "^#[0-9a-f]{6}$",
        "ecl": "^(amb)|(blu)|(brn)|(gry)|(grn)|(hzl)|(oth)$",
        "pid": "^[0-9]{9}$"
    }

    matches = 0
    for field in input.split():
        title, value = re.split(":", field)
        if title not in rules:
            continue
        pattern = re.compile(rules[title])
        if pattern.match(value):
            matches += 1
    return matches == len(rules)

file = open("data.txt")
inputs = re.split("\n\n", file.read())

print(count_valid_passports(inputs, check_basic_rule))
print(count_valid_passports(inputs, check_strict_rule))