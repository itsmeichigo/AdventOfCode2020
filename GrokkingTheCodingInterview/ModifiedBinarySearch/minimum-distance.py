# Given an array of numbers sorted in ascending order, find the element in 
# the array that has the minimum difference with the given ‘key’.

# Example:
# Input: [4, 6, 10], key = 7
# Output: 6
# Explanation: The difference between the key '7' and '6' is minimum than 
# any other number in the array 

def search_min_diff_element(arr, key):
    if arr[0] > key: return arr[0]
    elif arr[-1] < key: return arr[-1]
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] > key:
            end = mid - 1
        elif arr[mid] < key:
            start = mid + 1
        else:
            return arr[mid]
    if abs(arr[start] - key) < abs(arr[end] - key):
        return arr[start]
    return arr[end]

def main():
    print(search_min_diff_element([4, 6, 10], 7))
    print(search_min_diff_element([4, 6, 10], 4))
    print(search_min_diff_element([1, 3, 8, 10, 15], 12))
    print(search_min_diff_element([4, 6, 10], 17))

main()