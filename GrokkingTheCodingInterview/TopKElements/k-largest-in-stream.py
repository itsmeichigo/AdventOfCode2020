# Design a class to efficiently find the Kth largest element in a stream of numbers.
# The class should have the following two things:
# - The constructor of the class should accept an integer array containing initial 
#   numbers from the stream and an integer ‘K’.
# - The class should expose a function add(int num) which will store the given number 
#   and return the Kth largest number.

# Example:
# Input: [3, 1, 5, 12, 2, 11], K = 4
# 1. Calling add(6) should return '5'.
# 2. Calling add(13) should return '6'.
# 2. Calling add(4) should still return '6'.

from heapq import heappush, heappop

class Stream:
    min_heap = []

    def __init__(self, arr, k):
        self.k = k
        for n in arr:
            self.add(n)

    def add(self, num):
        heappush(self.min_heap, num) # log(K) times
        if len(self.min_heap) > self.k:
            heappop(self.min_heap)
        return self.min_heap[0]

def main():
    stream = Stream([3, 1, 5, 12, 2, 11], 4)
    assert(stream.add(6)) == 5
    assert(stream.add(13)) == 6
    assert(stream.add(4)) == 6

main()