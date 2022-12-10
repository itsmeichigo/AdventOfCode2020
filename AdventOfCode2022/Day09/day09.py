with open("input.txt") as file:
    steps = [l.split(" ") for l in file.read().splitlines()]
    start, tail, head = (0, 0), (0, 0), (0, 0)
    tail_positions = set([tail])
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
            tail_positions.add(tail)
            # print("Head: " + str(head) + " - Tail: (" + str(tail))

    # print(tail_positions)
    print(len(tail_positions))
