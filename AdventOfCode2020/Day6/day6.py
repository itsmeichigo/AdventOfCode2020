def count_total_yes(groups, count_method):
    return sum(count_method(x) for x in groups)

def count_unique_answers(group):
    return len(set.union(*map(set, group.splitlines())))

def count_same_answers(group):
    return len(set.intersection(*map(set, group.splitlines())))

file = open("data.txt")
groups = file.read().split("\n\n")

q1 = count_total_yes(groups, count_unique_answers)
print(q1)

q2 = count_total_yes(groups, count_same_answers)
print(q2)