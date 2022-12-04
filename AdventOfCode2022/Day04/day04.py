def get_ranges(pair):
    start1, end1 = [int(i) for i in pair[0].split("-")]
    range1 = set(range(start1, end1+1))
    start2, end2 = [int(i) for i in pair[1].split("-")]
    range2 = set(range(start2, end2+1))
    return [range1, range2]

def check_subset(pair):
    range1, range2 = get_ranges(pair)
    return range1.issubset(range2) or range2.issubset(range1)

def check_overlap(pair):
    range1, range2 = get_ranges(pair)
    return len(range1 & range2) > 0

with open("input.txt") as file:
    pairs = [line.split(",") for line in file.readlines()]
    total_subsets = sum(1 if check_subset(p) else 0 for p in pairs)
    print(total_subsets)

    total_overlaps = sum(1 if check_overlap(p) else 0 for p in pairs)
    print(total_overlaps)