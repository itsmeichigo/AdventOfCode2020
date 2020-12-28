def group_anagrams(input):
    char_map = {}
    for word in input:
        chars = tuple(sorted(word))
        if chars not in char_map: 
            char_map[chars] = [word]
        else:
            char_map[chars].append(word)
    return list(char_map.values())

print(group_anagrams([""]))
print(group_anagrams(["eat","tea","tan","ate","nat","bat"])) 
