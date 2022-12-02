score_map = {"X": 1, "Y": 2, "Z": 3}
outcome_map = {"A": {"X": 3, "Y": 6, "Z": 0}, "B": {"X": 0, "Y": 3, "Z": 6}, "C": {"X": 6, "Y": 0, "Z": 3}}

def calculate_points_part1(item):
    oponent, me = item.split(" ")
    return score_map[me] + outcome_map[oponent][me]

def calculate_points_part2(item):
    oponent, result = item.split(" ")
    choices = outcome_map[oponent]
    result_map = {"X": 0, "Y": 3, "Z": 6}
    choice = list(i for i in choices if choices[i] == result_map[result])[0]
    return score_map[choice] + result_map[result]

with open("input.txt") as input:
    rounds = input.read().splitlines()
    part1_score = sum([calculate_points_part1(r) for r in rounds])
    print(part1_score)
    part2_score = sum([calculate_points_part2(r) for r in rounds])
    print(part2_score)