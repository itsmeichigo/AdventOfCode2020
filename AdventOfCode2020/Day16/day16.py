import re

def check_nearby_ticket_error_rate(tickets, ranges):
    error_rate = 0
    for t in tickets:
        for num in t:
            if check_invalid_num(num, ranges):
                error_rate += num
                break
    
    return error_rate

def check_invalid_num(num, ranges):
    invalid_count = 0
    for r in ranges:
        if num < r[0] or num > r[3] or (num > r[1] and num < r[2]):
            invalid_count += 1
    return invalid_count == len(ranges)

def test_input():
    test1 = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""
    ranges, mine, tickets = parse_input(test1)
    assert(check_nearby_ticket_error_rate(tickets, ranges)) == 71

def parse_input(input):
    rules, my_ticket, nearby = input.split("\n\n")
    ranges = [parse_range(r) for r in rules.splitlines()]
    mine = [int(i) for i in my_ticket.splitlines()[-1].split(",")]
    tickets = [[int(i) for i in l.split(",")] for l in nearby.splitlines()[1:]]
    return ranges, mine, tickets

def parse_range(r):
    return [int(i) for i in re.match(r".+: (\d+)-(\d+) or (\d+)-(\d+)", r).group(1, 2, 3, 4)]

if __name__ == "__main__":
    test_input()
    with open("data.txt") as file:
        ranges, mine, tickets = parse_input(file.read())
        print(check_nearby_ticket_error_rate(tickets, ranges))