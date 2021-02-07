# Given a string, sort it based on the decreasing frequency of its characters.

# Example:
# Input: "Programming"
# Output: "rrggmmPiano"
# Explanation: 'r', 'g', and 'm' appeared twice, so they need to appear before 
# any other character.

from heapq import heappop, heappush

def sort_character_by_frequency(input):
    frequency_map = {} # N space
    for char in input: # N times
        frequency_map[char] = frequency_map.get(char, 0) + 1
    
    min_heap = []
    for char, frequency in frequency_map.items(): # N times
        heappush(min_heap, (frequency, char)) # log(N) times

    new_word = ""
    while len(min_heap) > 0: # N times
        item = heappop(min_heap)
        new_word = item[1]*item[0] + new_word

    return new_word


def main():
    print("String after sorting characters by frequency: " +
        sort_character_by_frequency("Programming"))
    print("String after sorting characters by frequency: " +
        sort_character_by_frequency("abcbab"))

main()