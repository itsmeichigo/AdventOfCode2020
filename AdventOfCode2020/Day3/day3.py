from functools import reduce

def count_tree(input, right, down):
    total_trees = 0
    current_row, current_index = down, 0
    
    while current_row < len(input):
        row = input[current_row]
        current_index = (current_index + right) % len(row)
        if row[current_index] == "#":
            total_trees += 1
        current_row += down

    return total_trees

def count_tree_patterns(input):
    patterns = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    return reduce(lambda x, y: x*y, [count_tree(input, i[0], i[1]) for i in patterns])

file = open("data.txt")
input = file.read().splitlines()

q1 = count_tree(input, 3, 1)
print(q1)

q2 = count_tree_patterns(input)
print(q2)
