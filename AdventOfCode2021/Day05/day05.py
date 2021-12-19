def parse_input(file_name):
    with open(file_name) as file:
        points = []
        for line in file.read().splitlines():
            p1, p2 = line.split(" -> ")
            points.append((tuple([int(i) for i in p1.split(",")]), tuple([int(i) for i in p2.split(",")])))
        return points

def count_overlapped_points(input, without_diagonal=True) -> int:
    max_x, max_y = 0, 0
    for points in input:
        p1, p2 = points
        max_x = max(max_x, p1[0], p2[0])
        max_y = max(max_y, p1[1], p2[1])
    # print(max_x, max_y, input)
    fields = [[0 for i in range(max_x + 1)] for j in range(max_y + 1)]
    for points in input:
        x1, y1 = points[0]
        x2, y2 = points[1]
        if without_diagonal:
            if x1 == x2 or y1 == y2:
                mark_field(x1, y1, x2, y2, fields)
        else:
            mark_field(x1, y1, x2, y2, fields)
    total_overlaps = 0
    for i in range(max_x + 1):
        for j in range(max_y + 1):
            if fields[j][i] >= 2:
                total_overlaps += 1
    return total_overlaps

def mark_field(x1, y1, x2, y2, fields):
    while x1 != x2 or y1 != y2:
        fields[y1][x1] += 1
        x1 += 0 if x1 == x2 else 1 if x1 < x2 else -1
        y1 += 0 if y1 == y2 else 1 if y1 < y2 else -1
    fields[y2][x2] += 1

test_points = parse_input("test.txt")
assert count_overlapped_points(test_points) == 5
assert count_overlapped_points(test_points, without_diagonal=False) == 12

data = parse_input("data.txt")
print("Part 1: ", count_overlapped_points(data))
print("Part 2: ", count_overlapped_points(data, without_diagonal=False))