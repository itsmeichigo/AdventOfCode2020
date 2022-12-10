def move_knots(steps, tail_count):
    start, head = (0, 0), (0, 0)
    tails = [start for i in range(tail_count)]
    tail_positions = set([start])
    for direction, count in steps:
        for i in range(int(count)):
            if direction == "R":
                head = (head[0] + 1, head[1])
            elif direction == "L":
                head = (head[0] - 1, head[1])
            elif direction == "U":
                head = (head[0], head[1] - 1)
            elif direction == "D":
                head = (head[0], head[1] + 1)

            new_tails = []
            next_head = head
            for tail in tails:
                next_head = move_tail(next_head, tail)
                new_tails.append(next_head)
            tail_positions.add(next_head)
            tails = new_tails
            # print("Head: " + str(head) + " - Tail: (" + str(tail))
    return tail_positions

def move_tail(head, tail):
    if head[0] == tail[0] and head[1] - 1 > tail[1]:
        tail = (tail[0], tail[1] + 1)
    elif head[0] == tail[0] and head[1] + 1 < tail[1]:
        tail = (tail[0], tail[1] - 1)
    elif head[1] == tail[1] and head[0] - 1 > tail[0]:
        tail = (tail[0] + 1, tail[1])
    elif head[1] == tail[1] and head[0] + 1 < tail[0]:
        tail = (tail[0] - 1, tail[1])
    elif head[0] != tail[0] and head[1] != tail[1]:
        if head[1] - 1 > tail[1]:
            tail = (head[0], tail[1] + 1)
        elif head[1] + 1 < tail[1]:
            tail = (head[0], tail[1] - 1)
        elif head[0] - 1 > tail[0]:
            tail = (tail[0]+ 1, head[1])
        elif head[0] + 1 < tail[0]:
            tail = (tail[0] - 1, head[1])
    return tail

with open("input.txt") as file:
    steps = [l.split(" ") for l in file.read().splitlines()]
    # print(len(move_knots(steps, 1)))
    print(len(move_knots(steps, 9)))
