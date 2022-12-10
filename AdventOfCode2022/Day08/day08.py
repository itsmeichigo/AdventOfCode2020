def check_tree(x, y, trees):
    if x == 0 or y == 0 or x == len(trees[0]) - 1 or y == len(trees) - 1:
        return (True, 0)
    visible_left, visible_right, visible_top, visible_bottom = True, True, True, True
    count_left, count_right, count_top, count_bottom = 0, 0, 0, 0
    for i in reversed(range(x)):
        count_left = x - i
        if trees[i][y] >= trees[x][y]:
            visible_left = False
            break
    for i in range(x + 1, len(trees[0])):
        count_right = i - x
        if trees[i][y] >= trees[x][y]:
            visible_right = False
            break
    for j in reversed(range(y)):
        count_top = y - j
        if trees[x][j] >= trees[x][y]:
            visible_top = False
            break
    for j in range(y + 1, len(trees)):
        count_bottom = j - y
        if trees[x][j] >= trees[x][y]:
            visible_bottom = False
            break

    scenic_score = count_top * count_bottom * count_left * count_right
    is_visible = visible_left or visible_right or visible_top or visible_bottom
    return (is_visible, scenic_score)

with open("input.txt") as file:
    lines = file.read().splitlines()
    trees = [list(l) for l in lines]
    results = [check_tree(x, y, trees) for x in range(0, len(trees[0])) for y in range(0, len(trees))]
    visible_trees = sum(1 if r[0] == True else 0 for r in results)
    print(visible_trees)
    max_scenic_score = max(r[1] for r in results)
    print(max_scenic_score)
