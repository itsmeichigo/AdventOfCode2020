# Given two sorted arrays in descending order, find ‘K’ pairs with the largest sum 
# where each pair consists of numbers from both the arrays.

# Example:
# Input: L1=[9, 8, 2], L2=[6, 3, 1], K=3
# Output: [9, 3], [9, 6], [8, 6] 
# Explanation: These 3 pairs have the largest sum. No other pair has a sum larger than any of these.

from heapq import heappush, heappop

def find_k_largest_pairs(nums1, nums2, k):
    arr1, arr2 = nums1[:k], nums2[:k]
    min_heap = [] # O(K) space
    for num1 in arr1: # O(N*M*log(K)) ~ O(K^2log(K)) times
        for num2 in arr2:
            total = num1 + num2
            if len(min_heap) < k:
                heappush(min_heap, (total, [num1, num2]))
            else:
                if min_heap[0][0] > total:
                    break
                else:
                    heappop(min_heap) # need to remove smallest sum to make place for larger one
                    heappush(min_heap, (total, [num1, num2]))

    return [item[1] for item in min_heap]


def main():
    print("Pairs with largest sum are: " +
        str(find_k_largest_pairs([9, 8, 2], [6, 3, 1], 3)))
    print("Pairs with largest sum are: " +
        str(find_k_largest_pairs([5, 2, 1], [2, -1], 3)))

main()