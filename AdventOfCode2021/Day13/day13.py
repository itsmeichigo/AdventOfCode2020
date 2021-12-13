def parse_input(file_name):
    with open(file_name) as file:
        dots, instructions = file.read().split("\n\n")
        sanited_dots = [tuple([int(i) for i in line.split(",")]) for line in dots.splitlines()]
        folds = []
        for content in instructions.splitlines():
            axis, value = content.replace("fold along ", "").split("=")
            if axis == "y":
                folds.append((0, int(value)))
            elif axis == "x":
                folds.append((int(value), 0))
        return (sanited_dots, folds)

def visualize(dots):
    max_x = max([dot[0] for dot in dots])
    max_y = max([dot[1] for dot in dots])
    lines = [["." for i in range(max_x + 1)] for j in range(max_y + 1)]
    for dot in dots:
        x, y = dot
        lines[y][x] = "#"
    return "\n".join(["".join(line) for line in lines])

def fold_paper(initial_dots, folds, first_only):
    current_dots = initial_dots.copy()
    for i in range(len(folds)):
        current_dots = fold(current_dots, folds[i])
        if first_only and i == 0:
            return current_dots
    return current_dots

def fold(initial_dots, fold):
    x, y = fold
    for i in range(len(initial_dots)):
        if initial_dots[i][1] > y and x == 0 and y > 0: # fold horizontally
            initial_dots[i] = (initial_dots[i][0], abs(initial_dots[i][1] - y - y))
        elif initial_dots[i][0] > x and x > 0 and y == 0: # fold vertically
            initial_dots[i] = (abs(initial_dots[i][0] - x - x), initial_dots[i][1])
    return list(set(initial_dots))

test_dots, test_folds = parse_input("test.txt")
test_fold_1 = fold_paper(test_dots, test_folds, first_only=True)
assert len(test_fold_1) == 17

dots, folds = parse_input("data.txt")
after_fold_1 = fold_paper(dots, folds, first_only=True)
print("Part 1: ", len(after_fold_1))
after_all = fold_paper(dots, folds, first_only=False)
print("Part 2:")
print(visualize(after_all))