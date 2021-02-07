# Given an array of numbers and a number ‘K’, we need to remove ‘K’ numbers 
# from the array such that we are left with maximum distinct numbers.

# Example:
# Input: [3, 5, 12, 11, 12], and K=3
# Output: 2
# Explanation: We can remove one occurrence of 12, after which all numbers will become distinct. Then 
# we can delete any two numbers which will leave us 2 distinct numbers in the result.

from heapq import heappop, heappush

def find_maximum_distinct_elements(nums, k):
    frequency_map = {} # N space
    for n in nums:
        frequency_map[n] = frequency_map.get(n, 0) + 1
    
    min_heap = [] # N space
    count = 0
    for number, frequency in frequency_map.items(): # N times
        if frequency == 1:
            count += 1
        else:
            heappush(min_heap, (frequency, number)) # worst case: log(N) times

    while k > 0 and len(min_heap) > 0: # K times
        frequency, number = heappop(min_heap) # log(N) times
        k -= frequency - 1
        if k >= 0:
            count += 1

    if k > 0:
        count -= k
    return count

# => can optimize using max heap of size K

def main():
    print("Maximum distinct numbers after removing K numbers: " +
            str(find_maximum_distinct_elements([7, 3, 5, 8, 5, 3, 3], 2)))
    print("Maximum distinct numbers after removing K numbers: " +
            str(find_maximum_distinct_elements([3, 5, 12, 11, 12], 3)))
    print("Maximum distinct numbers after removing K numbers: " +
            str(find_maximum_distinct_elements([1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], 2)))

main()