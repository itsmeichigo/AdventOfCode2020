# Given an array of numbers sorted in an ascending order, find the ceiling of 
# a given number ‘key’. The ceiling of the ‘key’ will be the smallest element 
# in the given array greater than or equal to the ‘key’.

# Write a function to return the index of the ceiling of the ‘key’. If there 
# isn’t any ceiling return -1.

# Example:
# Input: [4, 6, 10], key = 6
# Output: 1
# Explanation: The smallest number greater than or equal to '6' is '6' having index '1'.

def search_ceiling_of_a_number(arr, key):
    index = len(arr) // 2
    last_greater_index = -1
    while index >= 0 and index < len(arr):
        if arr[index] == key:
            return index
        if arr[index] < key:
            if last_greater_index > -1:
                return last_greater_index
            index += 1
        else:
            last_greater_index = index
            index -= 1
    return last_greater_index

def search_ceiling_of_a_number_two_pointers(arr, key):
    if key > arr[-1]: return -1
    start, end = 0, len(arr)-1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] > key:
            end = mid - 1
        elif arr[mid] < key:
            start = mid + 1
        else:
            return mid
    return start

def main():
    print(search_ceiling_of_a_number_two_pointers([4, 6, 10], 6))
    print(search_ceiling_of_a_number_two_pointers([1, 3, 8, 10, 15], 12))
    print(search_ceiling_of_a_number_two_pointers([4, 6, 10], 17))
    print(search_ceiling_of_a_number_two_pointers([4, 6, 10], -1))

main()