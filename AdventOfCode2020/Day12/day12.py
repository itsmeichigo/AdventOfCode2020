def move_ship(steps):
    location = {"E": 0, "W": 0, "S": 0, "N": 0}
    current_direction = directions[0]
    for step in steps:
        i, value = step[0], int(step[1:])
        if i == "F":
            move_forward(current_direction, value, location)
        elif i in directions:
            move_forward(i, value, location)
        elif i in ["L", "R"]:
            current_direction = find_direction(current_direction, i, value)
    return sum(i for i in location.values())

def move_forward(direction, distance, location):
    opposite = find_direction(direction, "", 180)
    location[direction] += max(0, distance - location[opposite])
    location[opposite] = max(0, location[opposite] - distance)

def find_direction(current, turning, degree):
    current_index = directions.index(current)
    if degree == 180:
        return directions[(current_index + 2)%len(directions)]
    elif turning == "L":
        return directions[current_index - int(degree / 90)]
    elif turning == "R":
        return directions[(current_index + int(degree / 90)) % len(directions)]

def move_ship_by_waypoint(steps):
    ship = {"E": 0, "W": 0, "S": 0, "N": 0}
    waypoint = {"E": 10, "W": 0, "S": 0, "N": 1}
    for step in steps:
        i, value = step[0], int(step[1:])
        if i == "F":
            for k, v in waypoint.items():
                if v == 0: continue
                move_forward(k, v*value, ship)
        elif i in directions:
            move_forward(i, value, waypoint)
        elif i in ["L", "R"]:
            copy = waypoint.copy()
            for k, v in waypoint.items():
                new_direction = find_direction(k, i, value)
                copy[new_direction] = v
            waypoint = copy
    return sum(i for i in ship.values())

with open("data.txt") as file:
    steps = file.read().splitlines()
    directions = ["E", "S", "W", "N"] # clockwise direction list
    print(move_ship(steps))
    print(move_ship_by_waypoint(steps))