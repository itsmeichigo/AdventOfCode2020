# Given an array of numbers which is sorted in ascending order and is rotated 
# ‘k’ times around a pivot, find ‘k’.
# You can assume that the array does not have any duplicates.

# Example:
# Input: [10, 15, 1, 3, 8]
# Output: 2
# Explanation: The array has been rotated 2 times.

# check for index of minimum number
# i.e the only item that has arr[i - 1] > arr[i]
# this will be the number of rotations
def count_rotations(arr):
    start, end = 0, len(arr) - 1
    min_index = -1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] > arr[start] and arr[mid] < arr[end]:
            return 0

        if mid > start and arr[mid] < arr[mid - 1]:
            min_index = mid
        
        if mid < end and arr[mid] > arr[mid + 1]:
            min_index = mid + 1

        # left side is sorted then check right side and vice versa
        if arr[start] < arr[mid]: 
            start = mid + 1
        else:
            end = mid - 1
    return min_index

# if array contains duplicate, it's important to check before increasing start 
# and decreasing end - i.e check if arr[start] > arr[start+1] and arr[end] < arr[end-1]
# also make sure to check for equality of mid and start / end when switching sides

def main():
    print(count_rotations([10, 15, 1, 3, 8]))
    print(count_rotations([3, 4, 5, 7, 9, 10, -1, 2]))
    print(count_rotations([1, 3, 8, 10]))

main()