def get_highest_seatid(inputs):
    return max(get_seatid(x) for x in inputs)

def find_missing_seat(inputs):
    all_seats = [get_seatid(x) for x in inputs]
    all_seats.sort()
    for i in range(len(all_seats) - 1):
        if all_seats[i] + 1 != all_seats[i+1]:
            return all_seats[i] + 1
    return -1

def get_seatid(input):
    row = decode_position("F", 128, input[:7])
    column = decode_position("L", 8, input[7:])
    return row * 8 + column

def decode_position(first_half, length, encoded):
    current_range = (0, length)
    for char in encoded:
        half_length = int((current_range[1] - current_range[0]) / 2)
        if char == first_half:
            current_range = (current_range[0], current_range[0] + half_length)
        else:
            current_range = (current_range[1] - half_length, current_range[1])

    return current_range[0]

inputs = open("data.txt").read().splitlines()

q1 = get_highest_seatid(inputs)
print(q1)

q2 = find_missing_seat(inputs)
print(q2)