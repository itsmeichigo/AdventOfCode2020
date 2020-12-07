import re

def count_bags(rules, item, is_container):
    input = {}
    for x in rules:
        input.update(parse(x))

    results = []
    if is_container:
        find_contents(input, item, results, 1)
        return len(results)
    else:
        find_containers(input, item, results)
        return len(set(results))

def find_containers(input, content, results):
    immediate_containers = [x for x in input.keys() if content in input[x]]
    for x in immediate_containers:
        results.append(x)
        find_containers(input, x, results)

def find_contents(input, container, results, times):
    if container in input:
        for k, v in input[container].items():
            results.extend(times * v * [k])
            find_contents(input, k, results, times * v)

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