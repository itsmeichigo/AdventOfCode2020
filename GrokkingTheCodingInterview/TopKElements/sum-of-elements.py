# Given an array, find the sum of all numbers between the K1’th and K2’th 
# smallest elements of that array.

# Example:
# Input: [1, 3, 12, 5, 15, 11], and K1=3, K2=6
# Output: 23
# Explanation: The 3rd smallest number is 5 and 6th smallest number 15. 
# The sum of numbers coming between 5 and 15 is 23 (11+12).

from heapq import heappush, heappop

def find_sum_of_elements(nums, k1, k2):
    min_heap = [] # N space
    for n in nums: # N times
        heappush(min_heap, n) # log(N) times
    
    result = 0
    for i in range(k2 - 1):
        num = heappop(min_heap)
        if i >= k1:
            result += num
    return result

def find_sum_of_elements_optimized(nums, k1, k2):
    max_heap = [] # K2 space
    for i in range(len(nums)): # Nlog(K2) times
        if i < k2 - 1:
            heappush(max_heap, -nums[i])
        elif nums[i] < -max_heap[0]:
            heappop(max_heap)
            heappush(max_heap, -nums[i])
    
    result = 0
    for _ in range(k2 - k1 - 1):
        result += -heappop(max_heap)

    return result

def main():
    print("Sum of all numbers between k1 and k2 smallest numbers: " +
        str(find_sum_of_elements_optimized([1, 3, 12, 5, 15, 11], 3, 6)))
    print("Sum of all numbers between k1 and k2 smallest numbers: " +
        str(find_sum_of_elements_optimized([3, 5, 8, 7], 1, 4)))

main()
