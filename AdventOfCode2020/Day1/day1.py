def product_of_pair(arr, sum):
    for num in arr:
        target = sum - num
        if target in arr:
            return target * num
    return None

def product_of_three(arr, sum):
    for (i, num) in enumerate(arr):
        target = sum - num
        found = product_of_pair(arr[i:], target)
        if found:
            return found * num
    return None

data = open("data.txt").read().splitlines()
input = list(map(lambda x: int(x), data))
q1 = product_of_pair(input, 2020)
print(q1)

q2 = product_of_three(input, 2020)
print(q2)