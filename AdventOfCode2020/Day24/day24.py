direction_map = {
    "ne": [1, 0, -1], "nw": [0, 1, -1], "w": [-1, 1, 0],
    "sw": [-1, 0, 1], "se": [0, -1, 1], "e": [1, -1, 0]
}

def find_final_tile(input):
    current = [0, 0, 0]
    for d in parse_directions(input):
        current = [sum(x) for x in zip(current, direction_map[d])]
    return tuple(current)

def parse_directions(input):
    i, directions = 0, []
    while i < len(input):
        if input[i] in ["s", "n"]:
            directions.append(input[i:i+2])
            i += 2
        else:
            directions.append(input[i])
            i += 1
    return directions

def find_neighbors(tile):
    neighbors = []
    for v in direction_map.values():
        new_tile = tuple(sum(x) for x in zip(tile, v))
        neighbors.append(new_tile)
    return neighbors

def count_black_tiles(tile_map):
    return sum([1 for v in tile_map.values() if v])

def layout_lobby(input):
    tile_map = {}
    directions = input.splitlines()
    for d in directions:
        tile = find_final_tile(d)
        if tile not in tile_map: tile_map[tile] = True
        else: tile_map[tile] = not tile_map[tile]
    initial_black_count = count_black_tiles(tile_map)

    for _ in range(100):
        new_map = {}
        for tile in list(tile_map):
            for n in find_neighbors(tile):
                if n not in tile_map: tile_map[n] = False
        for tile, is_black in tile_map.items():
            black_neighbors = len([n for n in find_neighbors(tile) if tile_map.get(n, False)])
            if is_black and (black_neighbors == 0 or black_neighbors > 2):
                new_map[tile] = False
            elif not is_black and black_neighbors == 2:
                new_map[tile] = True
            else: new_map[tile] = is_black
        tile_map = new_map

    day100_black_count = count_black_tiles(tile_map)
    return initial_black_count, day100_black_count

if __name__ == "__main__":
    with open("test.txt") as test_file:
        assert(layout_lobby(test_file.read())) == (10, 2208)

    with open("data.txt") as file:
        print(layout_lobby(file.read()))