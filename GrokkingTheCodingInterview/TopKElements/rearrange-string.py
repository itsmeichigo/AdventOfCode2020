# Given a string, find if its letters can be rearranged in such a way that 
# no two same characters come next to each other.

# Example:
# Input: "aappp"
# Output: "papap"
# Explanation: In "papap", none of the repeating characters come next to each other.

from heapq import heappop, heappush

def rearrange_string(input):
    frequency_map = {} # N space
    max_heap = []
    for char in input:
        frequency_map[char] = frequency_map.get(char, 0) + 1
    
    for char, frequency in frequency_map.items(): # Nlog(N) times
        heappush(max_heap, (-frequency, char))

    chars = []
    while max_heap:
        frequency, char = heappop(max_heap)
        chars += char
        frequency += 1 # reverse of -frequency -= 1
        while max_heap and -frequency > 0: # look for next char to append between current char
            next_frequency, next_char = heappop(max_heap)
            while -next_frequency > 0 and -frequency > 0:
                chars += [next_char, char]
                next_frequency += 1
                frequency += 1
            if -frequency > 0:
                return ""
            if -next_frequency > 0:
                heappush(max_heap, (next_frequency, next_char))

    return "".join(chars)


def main():
    print("Rearranged string:  " + rearrange_string("aappp"))
    print("Rearranged string:  " + rearrange_string("Programming"))
    print("Rearranged string:  " + rearrange_string("aapa"))

main()