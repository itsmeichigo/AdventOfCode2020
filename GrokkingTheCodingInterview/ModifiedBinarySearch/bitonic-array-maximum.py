# Find the maximum value in a given Bitonic array. An array is considered 
# bitonic if it is monotonically increasing and then monotonically decreasing. 
# Monotonically increasing or decreasing means that for any index i in the 
# array arr[i] != arr[i+1].

# Example:
# Input: [1, 3, 8, 12, 4, 2]
# Output: 12
# Explanation: The maximum number in the input bitonic array is '12'.

def find_max_in_bitonic_array(arr):
    if len(arr) == 0: return -1
    elif len(arr) == 1: return arr[0]

    start, end = 0, len(arr) - 1
    while start < end:
        mid = start + (end - start) // 2
        if arr[mid] > arr[mid+1]:
            end = mid
        elif arr[mid] < arr[mid+1]:
            start = mid + 1

    return arr[start]


def main():
    print(find_max_in_bitonic_array([1, 3, 8, 12, 4, 2]))
    print(find_max_in_bitonic_array([3, 8, 3, 1]))
    print(find_max_in_bitonic_array([1, 3, 8, 12]))
    print(find_max_in_bitonic_array([10, 9, 8]))


main()