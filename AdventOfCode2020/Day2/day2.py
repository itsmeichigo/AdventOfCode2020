def count_valid_passwords(arr, func):
    transform = [1 if func(x) else 0 for x in arr]
    return sum(i for i in transform)

def check_valid(pattern):
    min, max, char, password = parse(pattern)
    count = len([x for x in password if x == char])
    return count >= min and count <= max

def check_valid2(pattern):
    i, j, char, password = parse(pattern)
    c1, c2 = password[i-1], password[j-1]
    return len([x for x in [c1, c2] if x == char]) == 1

def parse(pattern):
    inputs = pattern.split()
    i, j = list(int(x) for x in inputs[0].split("-"))
    char, password = inputs[1][0], inputs[2]
    return (i, j, char, password)

file = open("data.txt")
data = file.read().splitlines()
q1 = count_valid_passwords(data, check_valid)
print(q1)

q2 = count_valid_passwords(data, check_valid2)
print(q2)
