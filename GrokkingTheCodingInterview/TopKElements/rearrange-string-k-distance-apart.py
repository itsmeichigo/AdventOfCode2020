# Given a string and a number ‘K’, find if the string can be rearranged such that 
# the same characters are at least ‘K’ distance apart from each other.

# Example:
# Input: "mmpp", K=2
# Output: "mpmp" or "pmpm"
# Explanation: All same characters are 2 distance apart.

from heapq import heappush, heappop
from collections import deque

def reorganize_string(str, k):
    frequency_map = {}
    for char in str:
        frequency_map[char] = frequency_map.get(char, 0) + 1

    max_heap = []
    for char, frequency in frequency_map.items():
        heappush(max_heap, (-frequency, char))

    previous_chars = deque()
    new_string = ""
    while max_heap:
        frequency, char = heappop(max_heap)
        if len(previous_chars) >= k - 1:
            previous_char, previous_frequency = previous_chars.popleft()
            if -previous_frequency > 0:
                heappush(max_heap, (previous_frequency, previous_char))
        new_string += char
        frequency += 1
        previous_chars.append((char, frequency))

    return new_string if len(new_string) == len(str) else ""

def main():
    print("Reorganized string: " + reorganize_string("mmpp", 2))
    print("Reorganized string: " + reorganize_string("Programming", 3))
    print("Reorganized string: " + reorganize_string("aab", 2))
    print("Reorganized string: " + reorganize_string("aapa", 3))

main()