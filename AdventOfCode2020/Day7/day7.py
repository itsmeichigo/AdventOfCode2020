import re

def count_bags(rules, item, is_container):
    input = {}
    for x in rules:
        input.update(parse(x))

    if is_container:
        return count_contents(input, item)
    else:
        return sum(1 for x in input.keys() if has_item(input, x, item) and x != item)

def has_item(input, container, item):
    if container == item:
        return True
    return any([has_item(input, x, item) for x in input[container]])

def count_contents(input, container):
    total = 0
    for k, v in input[container].items():
        total += (v + v * count_contents(input, k))
    return total

def parse(rule):
    container = re.match("(.+?) bags", rule).group(1)
    contents = {}
    for i in re.findall("(\d+) (.+?) bag", rule):
        contents[i[1]] = int(i[0])
    return {container: contents}

file = open("data.txt")
rules = file.read().splitlines()

q1 = count_bags(rules, "shiny gold", False)
print(q1)

q2 = count_bags(rules, "shiny gold", True)
print(q2)