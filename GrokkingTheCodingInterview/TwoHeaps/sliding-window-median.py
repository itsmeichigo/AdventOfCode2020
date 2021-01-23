# Given an array of numbers and a number ‘k’, find the median of all 
# the ‘k’ sized sub-arrays (or windows) of the array.

from heapq import heappop, heappush, heapify

class SlidingWindowMedian:
    max_heap, min_heap = [], []

    def find_sliding_window_median(self, nums, k):
        result = [0.0 for i in range(len(nums) - k + 1)]
        for i in range(len(nums)):
            if len(self.max_heap) == 0 or nums[i] <= -self.max_heap[0]:
                heappush(self.max_heap, -nums[i])
            else:
                heappush(self.min_heap, nums[i])
            self.rebalance_heaps()

            if i - k + 1 >= 0:
                if len(self.max_heap) > len(self.min_heap):
                    result[i-k+1] = -self.max_heap[0]
                else:
                    result[i-k+1] = (-self.max_heap[0] + self.min_heap[0]) / 2.0
                item_to_remove = nums[i-k+1]
                if item_to_remove <= -self.max_heap[0]:
                    self.remove_item(-item_to_remove, self.max_heap)
                else:
                    self.remove_item(item_to_remove, self.min_heap)
                self.rebalance_heaps()

        return result

    def remove_item(self, item, heap):
        index = heap.index(item)
        heap[index] = heap[-1]
        del heap[-1]
        heapify(heap)
        return

    def rebalance_heaps(self):
        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.max_heap) < len(self.min_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

def main():
    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median(
        [1, 2, -1, 3, 5], 2)
    print("Sliding window medians are: " + str(result))

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median(
        [1, 2, -1, 3, 5], 3)
    print("Sliding window medians are: " + str(result))


main()