# Given ‘M’ sorted arrays, find the K’th smallest number among all the arrays.

# Example:
# Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4], K=5
# Output: 4
# Explanation: The 5th smallest number among all the arrays is 4, 
# this can be verified from the merged list of all the arrays: 
# [1, 2, 3, 3, 4, 6, 6, 7, 8]

from heapq import heappush, heappop
from collections import deque

def find_Kth_smallest(lists, k):
    min_heap = []
    lists = [deque(l) for l in lists]
    for queue in lists:
        top = queue.popleft()
        heappush(min_heap, (top, queue)) 

    index = 0
    while min_heap and index < k: # O(Klog(M)) times
        num, queue = heappop(min_heap) 
        if index == k - 1:
            return num
        if queue:
            next_num = queue.popleft()
            heappush(min_heap, (next_num, queue))
        index += 1
    
    return None

# Other solution: use lists as arrays and keep track of visited index

def main():
    print("Kth smallest number is: " +
        str(find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5)))
    print("Kth smallest number is: " +
        str(find_Kth_smallest([[5, 8, 9], [1, 7]], 3)))


main()