from copy import deepcopy

def count_final_seats(original, max_occupied, immediate_adj_only):
    while True:
        changes, original = apply_rules(original, max_occupied, immediate_adj_only)
        if changes == 0:
            return len([x for x in "".join(["".join(x) for x in original]) if x == "#"])
    return changes

def apply_rules(original, max_occupied, immediate_adj_only):
    updated = deepcopy(original)
    changes = 0
    for i, row in enumerate(updated):
        for j, item in enumerate(row):
            if item == empty and count_vacant_adjacents(original, i, j, immediate_adj_only) == 0:
                updated[i][j] = vacant
                changes += 1
            elif item == vacant and count_vacant_adjacents(original, i, j, immediate_adj_only) >= max_occupied:
                updated[i][j] = empty
                changes += 1
    return changes, updated

def count_vacant_adjacents(seats, i, j, immediate_only):
    if immediate_only:
        return len([seats[i+a][j+b] for a,b in adjacent_indexes if mini <= i+a <= maxi and minj <= j+b <= maxj and seats[i+a][j+b] == vacant])
    adjacents = 0
    for a,b in adjacent_indexes:
        for c in range(1,len(seats)):
            if mini <= i+a*c <= maxi and minj <= j+b*c <= maxj:
                if seats[i+a*c][j+b*c] == empty:
                    break
                elif seats[i+a*c][j+b*c] == vacant:
                    adjacents += 1
                    break
    return adjacents


with open("data.txt") as file:
    seats = [list(x) for x in file.read().splitlines()]
    empty, vacant, floor = "L", "#", "."
    mini, minj, maxi, maxj = 0, 0, len(seats)-1, len(seats[0])-1
    adjacent_indexes = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    print(count_final_seats(seats, 4, True))
    print(count_final_seats(seats, 5, False))