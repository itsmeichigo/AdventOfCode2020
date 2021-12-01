def num_of_increases(depths):
    count = 0
    previous = None
    for i in depths:
        if previous and i > previous:
            count += 1
        previous = i
    return count

def sliding_window_measurements(depths):
    windows = []
    current_sum = 0
    current_index = 0
    while current_index < len(depths):
        current_sum += depths[current_index]
        if current_index >= 2:
            windows.append(current_sum)
            current_sum -= depths[current_index - 2]
        current_index += 1
    return windows

with open("test.txt") as file:
    input = file.read()
    depths = [int(i) for i in input.splitlines()]

    assert num_of_increases(depths) == 7
    assert num_of_increases(sliding_window_measurements(depths)) == 5

with open("data.txt") as file:
    input = file.read()
    depths = [int(i) for i in input.splitlines()]

    print(num_of_increases(depths))
    print(num_of_increases(sliding_window_measurements(depths)))