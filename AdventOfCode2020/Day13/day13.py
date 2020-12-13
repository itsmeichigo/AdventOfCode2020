def find_earliest_bus(pickup, buses):
    remainder, bus = max((pickup%b, b) for b in buses)
    return bus * (bus - remainder)

# couldnt solve this myself
def find_subsequent_timestamp(buses):
    time, period = 0, 1
    for i, bus in enumerate(buses):
        while (time + i) % bus: 
            time += period
        period *= bus
    return time

def test_input():    
    pickup, buses = parse_input("""939
7,13,x,x,59,x,31,19""")
    assert(find_earliest_bus(pickup, buses)) == 295
    assert(find_subsequent_timestamp(buses)) == 1068781

def parse_input(str):
    input = str.splitlines()
    return int(input[0]), [int(i) for i in input[1].replace("x", "1").split(",")]

if __name__ == "__main__":
    test_input()
    with open("data.txt") as file:
        pickup, buses = parse_input(file.read())
        print(find_earliest_bus(pickup, buses))
        print(find_subsequent_timestamp(buses))
