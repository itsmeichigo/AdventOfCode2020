def get_letter_combinations(input):
    letter_map = {
        1: "", 2: "abc", 3: "def", 4: "ghi", 5: "jkl",
        6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz", 0: ""
    }
    results = [""]
    values = [letter_map[int(char)] for char in input if len(letter_map[int(char)]) > 0]
    for value in values:
        updated = []
        for prefix in results:
            for char in value:
                updated.append(prefix + char)
        results = updated
    return results

assert(get_letter_combinations("12")) == ["a", "b", "c"]
assert(get_letter_combinations("23")) == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
