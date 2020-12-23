def play_cups(starting, rounds, p2=False):
    numbers = [int(c) for c in list(starting)]
    if p2: numbers += [i for i in range(10, 1000001)]

    next = dict(zip(numbers, (numbers[1:] + [numbers[0]])))

    round = 0
    current_cup = numbers[0]
    min_num, max_num = min(numbers), max(numbers)
    while round < rounds:
        move_next_round(next, current_cup, min_num, max_num)
        round += 1
        # print("Round ", round, current_cup)
        current_cup = next[current_cup]

    return get_cups_labels(next, 1, True)

def get_cups_labels(next, starting, exclusive=False):
    result = []
    if not exclusive: result.append(starting)
    current = next[starting]
    while True:
        result.append(current)
        current = next[current]
        if current == starting: break
    return result

def move_next_round(next, current_cup, min_num, max_num):
    c1 = next[current_cup]
    c2 = next[c1]
    c3 = next[c2]
    
    destination = current_cup
    while True:
        destination -= 1
        if destination < min_num:
            destination = max_num
        if destination not in [c1, c2, c3]: break
    # print(get_cups_labels(next, current_cup), c1, c2, c3, destination)
    
    next[current_cup] = next[c3]
    old = next[destination]
    next[destination] = c1
    next[c3] = old

# part 1
assert("".join([str(i) for i in play_cups("389125467", 10)])) == "92658374"
assert("".join([str(i) for i in play_cups("389125467", 100)])) == "67384529"
print("".join([str(i) for i in play_cups("789465123", 100)]))

#part 2
result = play_cups("789465123", 10000000, True)
print(int(result[0]) * int(result[1])) 