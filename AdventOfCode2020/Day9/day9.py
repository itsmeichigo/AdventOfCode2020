def find_odd_one_out(numbers, pre_length):
    for i in range(pre_length, len(numbers)):
        if not check_valid(numbers[i], numbers[i - pre_length:i], pre_length):
            return numbers[i]
    return None

def check_valid(num, pre_arr, pre_length):
    for x in pre_arr:
        if (num - x) in pre_arr:
            return True
    return False

def find_encryption_weakness(numbers, target):
    current_arr = []
    for num in numbers:
        current_arr.append(num)
        while sum(i for i in current_arr) > target:
            current_arr = current_arr[1:]
        if sum(i for i in current_arr) == target:
            break

    return min(current_arr) + max(current_arr)

with open("data.txt") as file:
    numbers = [int(x) for x in file.read().splitlines()]

    q1 = find_odd_one_out(numbers, 25)
    print(q1)

    q2 = find_encryption_weakness(numbers, q1)
    print(q2)