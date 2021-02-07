# Given an unsorted array of numbers, find the top ‘K’ frequently occurring 
# numbers in it.

# Example:
# Input: [1, 3, 5, 12, 11, 12, 11], K = 2
# Output: [12, 11]
# Explanation: Both '11' and '12' apeared twice.

from heapq import heappush, heappop

def find_k_frequent_numbers(nums, k):
    frequency_map = {} # N space
    for n in nums: # N times
        frequency_map[n] = frequency_map.get(n, 0) + 1
    
    min_heap = []
    for number, frequency in frequency_map.items(): # N times
        heappush(min_heap, (frequency, number)) # log(N) times
        if len(min_heap) > k:
            heappop(min_heap)

    return [i[1] for i in min_heap]


def main():
    print("Here are the K frequent numbers: " +
        str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)))

    print("Here are the K frequent numbers: " +
        str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2)))


main()