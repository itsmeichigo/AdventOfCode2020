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
    return [tuple(sum(x) for x in zip(tile, v)) for v in direction_map.values()]

def layout_lobby(input):
    black_tiles = set()
    directions = input.splitlines()
    for d in directions:
        tile = find_final_tile(d)
        if tile not in black_tiles: black_tiles.add(tile)
        else: black_tiles.remove(tile)
    initial_black_count = len(black_tiles)

    for _ in range(100):
        neighbors = {}
        for tile in black_tiles:
            for n in find_neighbors(tile):
                if n in neighbors: neighbors[n] += 1
                else: neighbors[n] = 1
        black_tiles = set(t for t, v in neighbors.items() 
            if v == 2 or 
            t in black_tiles and v == 1
        )

    day100_black_count = len(black_tiles)
    return initial_black_count, day100_black_count

if __name__ == "__main__":
    with open("test.txt") as test_file:
        assert(layout_lobby(test_file.read())) == (10, 2208)

    with open("data.txt") as file:
        print(layout_lobby(file.read()))