from math import inf

def parse_coordinates(path):
    steps = [(p[0], int(p[1:])) for p in path.split(",")]
    coordinates = []
    current = (0,0)
    for step in steps:
        if step[0] == "R": current = (current[0] + step[1], current[1])
        elif step[0] == "L": current = (current[0] - step[1], current[1])
        elif step[0] == "U": current = (current[0], current[1] + step[1])
        elif step[0] == "D": current = (current[0], current[1] - step[1])
        coordinates.append(current)
    return coordinates

def manage_wires(input):
    wire1, wire2 = [parse_coordinates(l) for l in input.splitlines()]
    w1_steps, w2_steps = [[int(p[1:]) for p in l.split(",")] for l in input.splitlines()]
    closest, shortest = inf, inf
    for i in range(len(wire1) - 1):
        c1, c2 = wire1[i], wire1[i+1]
        if c1[0] == c2[0]:
            crosses = [j for j in range(len(wire2)-1) if
                        c1[0] in range(min(wire2[j][0], wire2[j+1][0]), max(wire2[j][0], wire2[j+1][0])) and
                        wire2[j][1] == wire2[j+1][1] and
                        wire2[j][1] in range(min(c1[1], c2[1]), max(c1[1], c2[1]))]
            for c in crosses:
                closest = min(closest, abs(c1[0]) + abs(wire2[c][1]))
                w1_steps_taken = sum(w1_steps[:i+1]) + abs(c1[1] - wire2[c][1])
                w2_steps_taken = sum(w2_steps[:c+1]) + abs(wire2[c][0] - c1[0])
                shortest = min(shortest, w1_steps_taken + w2_steps_taken)
        elif c1[1] == c2[1]:
            crosses = [j for j in range(len(wire2)-1) if
                        c1[1] in range(min(wire2[j][1], wire2[j+1][1]), max(wire2[j][1], wire2[j+1][1])) and
                        wire2[j][0] == wire2[j+1][0] and
                        wire2[j][0] in range(min(c1[0], c2[0]), max(c1[0], c2[0]))]
            for c in crosses:
                closest = min(closest, abs(wire2[c][0]) + abs(c1[1]))
                w1_steps_taken = sum(w1_steps[:i+1]) + abs(c1[0] - wire2[c][0])
                w2_steps_taken = sum(w2_steps[:c+1]) + abs(wire2[c][1] - c1[1])
                shortest = min(shortest, w1_steps_taken + w2_steps_taken)
    return closest, shortest

test1 = """R8,U5,L5,D3
U7,R6,D4,L4"""
assert(manage_wires(test1)) == (6, 30)

test2 = """R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83"""
assert(manage_wires(test2)) == (159, 610)

test3 = """R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"""
assert(manage_wires(test3)) == (135, 410)

input = open("data.txt").read()
print(manage_wires(input))