# Given a string, find all of its permutations preserving the 
# character sequence but changing case.
# Example:
# Input: "ad52"
# Output: "ad52", "Ad52", "aD52", "AD52"

def find_letter_case_string_permutations(input):
    permutations = []
    permutations.append(input)
    for i, char in enumerate(input):
        if char.isdigit():
            continue
        for j in range(len(permutations)):
            updated = list(permutations[j])
            updated[i] = updated[i].swapcase()
            permutations.append("".join(updated))
    return permutations

def main():
    print("String permutations are: " +
        str(find_letter_case_string_permutations("ad52")))
    print("String permutations are: " +
        str(find_letter_case_string_permutations("ab7c")))

main()