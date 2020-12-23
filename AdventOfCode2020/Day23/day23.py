def play_cups(starting, rounds):
    cups = [int(c) for c in list(starting)]
    current_round = 0
    while current_round < rounds:
        cups = move_next_round(cups)
        current_round += 1

    # part 1
    one_index = cups.index(1)
    result = []
    if one_index == len(cups) - 1: result = cups[:len(cups)]
    else: result = cups[(one_index + 1):] + cups[:one_index]
    return "".join([str(i) for i in result])
    
def move_next_round(cups):
    current = cups[0]
    pickups = cups[1:4]
    destination = current
    while True:
        destination -= 1
        if destination < min(cups):
            destination = max(cups)
        if destination not in pickups: break
    # remove pickups
    new_cups = [cups[0]] + cups[4:]
    # get index of destination
    des_index = new_cups.index(destination)
    # insert pickups after destination
    new_cups = new_cups[:des_index+1] + pickups + new_cups[(des_index+1):]
    new_current_index = new_cups.index(current)
    # if current not at end of list, get following items and add reverse of preceeding items
    # to make sure that the next current item is at index 0 of list
    if new_current_index < len(cups) - 1: 
        new_cups = new_cups[(new_current_index + 1):] + (new_cups[:(new_current_index + 1)])[::-1]
    return new_cups

assert(play_cups("389125467", 10)) == "92658374"
assert(play_cups("389125467", 100)) == "67384529"
print(play_cups("789465123", 100))
