import re

def assess_allergens(input):
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
    safe_count = sum(v for k, v in ing_count.items() if k in safe)
    allergen_map = {}
    while len(allergen_map) < len(data):
        for k, v in data.items():
            if len(v) == 1:
                ingredient = list(v)[0]
                allergen_map[k] = ingredient
                for other in data:
                    if ingredient in data[other]:
                        data[other].remove(ingredient)
                        
    allergens = ",".join([allergen_map[k] for k in sorted(list(allergen_map.keys()))])
    return safe_count, allergens

def test_input():
    test1 = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)"""
    assert(assess_allergens(test1)) == (5, "mxmxvkd,sqjhc,fvjkl")

if __name__ == "__main__":
    test_input()
    with open("data.txt") as file:
        print(assess_allergens(file.read()))