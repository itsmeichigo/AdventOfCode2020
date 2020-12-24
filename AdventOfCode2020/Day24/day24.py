def find_final_tile(input):
    current = [0, 0, 0]
    direction_map = {
        "ne": [1, 0, -1], "nw": [0, 1, -1], "w": [-1, 1, 0],
        "sw": [-1, 0, 1], "se": [0, -1, 1], "e": [1, -1, 0]
    }
    for d in parse_directions(input):
        current = [sum(x) for x in zip(current, direction_map[d])]
    return tuple(current)

def parse_directions(input) -> list:
    i, directions = 0, []
    while i < len(input):
        if input[i] in ["s", "n"]:
            directions.append(input[i:i+2])
            i += 2
        else:
            directions.append(input[i])
            i += 1
    return directions

def count_black_tiles(input):
    tile_map = {}
    directions = input.splitlines()
    for d in directions:
        tile = find_final_tile(d)
        if tile not in tile_map: tile_map[tile] = 1
        else: tile_map[tile] += 1
    return sum([1 for v in tile_map.values() if v%2 == 1])

if __name__ == "__main__":
    with open("test.txt") as test_file:
        assert(count_black_tiles(test_file.read())) == 10

    with open("data.txt") as file:
        print(count_black_tiles(file.read()))