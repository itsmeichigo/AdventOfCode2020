from math import prod
from re import match, compile

class Tile:
    def __init__(self, lines: list, tile_id: int, matching: list = []):
        self.lines = lines
        self.tile_id = tile_id
        self.matching = matching
    
    def all_edges(self) -> list:
        return [self.top_edge(), self.bottom_edge(), self.left_edge(), self.right_edge(),
        self.top_edge()[::-1], self.bottom_edge()[::-1], self.left_edge()[::-1], self.right_edge()[::-1]]

    def top_edge(self) -> str:
        return self.lines[0]

    def bottom_edge(self) -> str:
        return self.lines[-1]

    def left_edge(self) -> str:
        return "".join([l[0] for l in self.lines])

    def right_edge(self) -> str:
        return "".join([l[-1] for l in self.lines])

    def matching_variants(self) -> list:
        v = []
        for m in self.matching:
            v += m.variants()
        return v

    def remove_edges(self):
        updated = self.lines[1:len(self.lines)-1]
        updated = [l[1:len(l)-1] for l in updated]
        self.lines = updated

    def variants(self) -> list:
        tiles = [self]
        current_lines = self.lines.copy()
        for _ in range(3):
            current_lines = rotate(current_lines)
            tiles.append(Tile(current_lines, self.tile_id, self.matching.copy()))
        current_lines = flip(current_lines)
        tiles.append(Tile(current_lines, self.tile_id, self.matching.copy()))
        for _ in range(3):
            current_lines = rotate(current_lines)
            tiles.append(Tile(current_lines, self.tile_id, self.matching.copy()))
        return tiles

def flip(lines):
    return ([l[::-1] for l in lines])
    
def rotate(lines):
    reversed_lines = [l[::-1] for l in lines]
    return ["".join([l[i] for l in reversed_lines]) for i in range(len(reversed_lines))]

def play_jigsaw(input):
    tiles, corners = [], []
    for item in input.split("\n\n"):
        tile_id, content = match(r'Tile (\d+):\n((.+\n?)+)', item).group(1,2)
        tiles.append(Tile(content.splitlines(), int(tile_id)))
    for tile in tiles:
        top, left, right, bottom = tile.top_edge(), tile.left_edge(), tile.right_edge(), tile.bottom_edge()
        tile.matching = []
        for other in tiles:
            if other.tile_id == tile.tile_id: continue
            all_other_edges = other.all_edges()
            if top in all_other_edges or bottom in all_other_edges or left in all_other_edges or right in all_other_edges: 
                tile.matching.append(other)
        if len(tile.matching) == 2: corners.append(tile)
    
    image_map = assemble_image(tiles, corners)
    # print([[y.tile_id for y in x] for x in image_map])
    final_rows = []
    for row in image_map:
        for i in range(len(row[0].lines)):
            final_rows.append("".join(item.lines[i] for item in row))
    # print("\n".join(final_rows))

    monster_lines = open("sea-monster.txt").read().splitlines()
    all_monsters = count_all_monsters(final_rows, monster_lines)
    monster_sharp_count = count_sharps(monster_lines) * all_monsters
    image_sharp_count =  count_sharps(final_rows)
    sea_roughness = image_sharp_count - monster_sharp_count
    # print(all_monsters, sea_roughness)
    return prod([c.tile_id for c in corners]), sea_roughness

def count_sharps(lines):
    return sum([sum([1 for c in list(line) if c == "#"]) for line in lines])

def count_all_monsters(lines, monster_lines):
    patterns = [l.replace(" ", ".") for l in monster_lines]
    total = find_sea_monster(lines, patterns)
    for _ in range(3):
        lines = rotate(lines)
        total += find_sea_monster(lines, patterns)
    lines = flip(lines)
    total += find_sea_monster(lines, patterns)
    for _ in range(3):
        lines = rotate(lines)
        total += find_sea_monster(lines, patterns)
    return total

def find_sea_monster(lines, patterns):
    total = 0
    for x in range(len(lines[0]) - len(patterns[0]) + 1):
        for y in range(len(lines) - len(patterns) + 1):
            match = True
            match_lines = []
            for i in range(len(patterns)):
                line = "".join(lines[y + i][x:x+len(patterns[0])])
                if not compile(patterns[i]).match(line): 
                    match = False
                    break
                else: match_lines.append(line)
            if match: 
                total += 1
                print("Found monster at coordinate: ", x, y)
                print("\n".join(match_lines))
    return total

def assemble_image(tiles, corners) -> list:
    size = int(len(tiles) ** 0.5)
    top_left = corners[0]
    for v in top_left.variants():
        found_right_match, found_bottom_match = False, False
        for match in v.matching_variants():
            if match.top_edge() == v.bottom_edge():
                found_bottom_match = True
            elif match.left_edge() == v.right_edge():
                found_right_match = True
        if found_right_match and found_bottom_match:
            top_left = v
            break

    image_map = [[top_left for x in range(size)] for y in range(size)]
    for i in range(size):
        for j in range(size):
            if i == 0 and j == 0: continue
            elif i > 0 and j == 0:
                target = image_map[i-1][j]
                for match in target.matching_variants():
                    if match.top_edge() == target.bottom_edge():
                        image_map[i][j] = match
                        break
            else:
                target = image_map[i][j-1]
                for match in target.matching_variants():
                    if match.left_edge() == target.right_edge():
                        image_map[i][j] = match
                        break
    [[tile.remove_edges() for tile in line] for line in image_map]
    return image_map

def test_input():
    with open("test.txt") as file:
        assert(play_jigsaw(file.read())) == (20899048083289, 273)

if __name__ == "__main__":
    test_input()
    with open("data.txt") as file:
        print(play_jigsaw(file.read()))