# Given an array of numbers which is sorted in ascending order and also 
# rotated by some arbitrary number, find if a given ‘key’ is present in it.

# Write a function to return the index of the ‘key’ in the rotated array. 
# If the ‘key’ is not present, return -1. You can assume that the given 
# array does not have any duplicates.

# Example:
# Input: [4, 5, 7, 9, 10, -1, 2], key = 10
# Output: 4
# Explanation: '10' is present in the array at index '4'.

def search_rotated_array(arr, key):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == key:
            return mid
    
        # first half is sorted asc
        if arr[start] < arr[mid]: 
            # if largest number is less than key -> move to next half
            if arr[mid] < key: 
                start = mid + 1
            else: 
                # search on this half
                end = mid - 1
        else:
            if arr[end] < key:
                end = mid - 1 # move to first half
            else:
                # search on this half
                start = mid + 1
    return -1

# if array contains duplicates, above solution fails if arr[start] == arr[mid] == arr[end]
# e.g: [3, 7, 3, 3, 3], key = 7
# in that case, move start += 1 and end -= 1

def main():
    print(search_rotated_array([10, 15, 1, 3, 8], 15))
    print(search_rotated_array([4, 5, 7, 9, 10, -1, 2], 10))

main()
