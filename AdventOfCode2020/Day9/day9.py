def find_odd_one_out(numbers, pre_length):
    for i in range(pre_length, len(numbers)):
        if not check_valid(numbers[i], numbers[i - pre_length:i]):
            return numbers[i]
    return None

def check_valid(num, pre_arr):
    for x in pre_arr:
        if (num - x) in pre_arr:
            return True
    return False

def find_encryption_weakness(numbers, target):
    start, end = 0, 0
    current_sum = numbers[end]
    while end < len(numbers) - 1:
        end += 1
        current_sum += numbers[end]
        while current_sum > target and start < end - 1:
            current_sum -= numbers[start]
            start += 1
        if current_sum == target:
            current_arr = numbers[start:end+1]
            return min(current_arr) + max(current_arr)
    return None
    

with open("data.txt") as file:
    numbers = [int(x) for x in file.read().splitlines()]

    q1 = find_odd_one_out(numbers, 25)
    print(q1)

    q2 = find_encryption_weakness(numbers, q1)
    print(q2)