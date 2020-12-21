import re

def find_nonallergens(input):
    data = {}
    ing_count = {}
    for line in input.splitlines():
        ings, als = re.match(r"(.+)\(contains (.+)\)", line).group(1,2)
        for ing in ings.split():
            if ing not in ing_count: ing_count[ing] = 1
            else: ing_count[ing] += 1
        for al in als.split(", "):
            if al not in data: data[al] = set(ings.split())
            else: data[al] = set.intersection(data[al], set(ings.split()))
    
    safe = set(ing_count.keys()) - set.union(*map(set, data.values()))
    return sum(v for k, v in ing_count.items() if k in safe)

def test_input():
    test1 = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)"""
    assert(find_nonallergens(test1)) == 5

if __name__ == "__main__":
    test_input()
    with open("data.txt") as file:
        print(find_nonallergens(file.read()))