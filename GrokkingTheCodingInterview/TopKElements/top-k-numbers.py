# Given an unsorted array of numbers, find the ‘K’ largest numbers in it.

from heapq import heappush, heappop

# time complexity: N + Klog(N)
# space complexity: N
def find_k_largest_numbers(nums, k):
    max_heap = []
    for n in nums:
        heappush(max_heap, -n)
    return [-n for n in max_heap[:k]] 

# time complexity: Nlog(K)
# space complexity: K
def find_k_largest_numbers_alt(nums, k):
    min_heap = []
    for i in range(0, len(nums)):
        # add first k elements to min heap
        if i < k:
            heappush(min_heap, nums[i])
        # for every next element replace min element of the heap if it's larger
        elif nums[i] > min_heap[0]:
            heappop(min_heap)
            heappush(min_heap, nums[i])
    return min_heap

def main():
    print("Here are the top K numbers: " +
        str(find_k_largest_numbers_alt([3, 1, 5, 12, 2, 11], 3)))

    print("Here are the top K numbers: " +
        str(find_k_largest_numbers_alt([5, 12, 11, -1, 12], 3)))


main()