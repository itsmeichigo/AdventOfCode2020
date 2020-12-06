def count_total_yes(groups, count_method):
    return sum(count_method(x) for x in groups)

def count_unique_answers(group):
    return len(set(group.replace("\n", "")))

def count_same_answers(group):
    people = group.splitlines()
    current_set = set(people[0])
    for i in range(1, len(people)):
        current_set = current_set.intersection(set(people[i]))
    return len(current_set)

file = open("data.txt")
groups = file.read().split("\n\n")

q1 = count_total_yes(groups, count_unique_answers)
print(q1)

q2 = count_total_yes(groups, count_same_answers)
print(q2)