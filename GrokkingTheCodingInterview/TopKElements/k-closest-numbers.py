# Given a sorted number array and two integers ‘K’ and ‘X’, find ‘K’ closest 
# numbers to ‘X’ in the array. Return the numbers in the sorted order. ‘X’ is 
# not necessarily present in the array.

# Example:
# Input: [5, 6, 7, 8, 9], K = 3, X = 7
# Output: [6, 7, 8]

from heapq import heappush, heappop
from collections import deque

def find_closest_elements(arr, K, X):
    max_heap = [] # K space
    for n in arr: # N times
        heappush(max_heap, (-abs(n - X), n)) # log(K) times
        if len(max_heap) > K:
            heappop(max_heap)
    result = [i[1] for i in max_heap]
    result.sort() # Klog(K) times
    return result

def find_closest_elements_binary_search(arr, K, X):
    found_index = binary_search(arr, X) # log(N) times
    start = max(found_index - K, 0)
    end = min(found_index + K, len(arr) - 1)

    min_heap = [] # 2K space
    for i in range(start, end + 1): # 2K times
        heappush(min_heap, (abs(arr[i] - X), arr[i])) # log(K) times

    result = [] # K space
    while len(result) < K:
        result.append(heappop(min_heap)[1])
    
    result.sort() # Klog(K) times
    return result

def find_closest_elements_queue(arr, K, X):
    found_index = binary_search(arr, X) # log(N) times
    left, right = found_index, found_index + 1
    result = deque() # K space
    for _ in range(K): # K times
        if left >= 0 and right < len(arr):
            left_diff = abs(arr[left] - X)
            right_diff = abs(arr[right] - X)
            if left_diff < right_diff:
                result.appendleft(arr[left])
                left -= 1
            else:
                result.appendleft(arr[right])
                right += 1
        elif left >= 0:
            result.appendleft(arr[left])
            left -= 1
        else:
            result.append(arr[right])
            right += 1
    return result

def binary_search(arr, X):
    start, end = 0, len(arr) - 1
    while start < end:
        mid = start + (end - start) // 2
        if arr[mid] == X: 
            return mid
        elif arr[mid] > X:
            end = mid - 1
        else:
            start = mid + 1
    return end

def main():
    print("'K' closest numbers to 'X' are: " +
            str(find_closest_elements_queue([5, 6, 7, 8, 9], 3, 7)))
    print("'K' closest numbers to 'X' are: " +
            str(find_closest_elements_queue([2, 4, 5, 6, 9], 3, 6)))
    print("'K' closest numbers to 'X' are: " +
            str(find_closest_elements_queue([2, 4, 5, 6, 9], 3, 10)))

main()