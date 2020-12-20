from math import prod
from re import match

def find_corners(input):
    tiles_map, corners = {}, []
    for tile in input.split("\n\n"):
        tile_id, content = match(r'Tile (\d+):\n((.+\n?)+)', tile).group(1,2)
        tiles_map[tile_id] = content
    for k, v in tiles_map.items():
        if count_matching(tiles_map.values(), v) == 2: 
            corners.append(int(k))
    return corners

def count_matching(tiles, v):
    top, bottom, left, right = parse_sides(v)
    matches = 0
    for item in tiles:
        if item == v: continue
        t, b, l, r = parse_sides(item)
        options = [t, b, t[::-1], b[::-1], l, r, l[::-1], r[::-1]]
        if top in options or bottom in options or left in options or right in options: matches += 1
    return matches

def parse_sides(tile):
    lines = tile.splitlines()
    return [
        lines[0],
        lines[-1],
        "".join([l[0] for l in lines]),
        "".join([l[-1] for l in lines])
    ]

def test_input():
    with open("test.txt") as file:
        assert(prod(find_corners(file.read()))) == 20899048083289

if __name__ == "__main__":
    test_input()
    with open("data.txt") as file:
        print(prod(find_corners(file.read())))