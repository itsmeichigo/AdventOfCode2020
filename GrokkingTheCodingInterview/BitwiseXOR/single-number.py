# In a non-empty array of integers, every number appears twice except for one, 
# find that single number.

# Example:
# Input: 1, 4, 2, 1, 3, 2, 3
# Output: 4

def find_single_number(arr):
    x = arr[0]
    for i in range(1, len(arr)):
        x = x ^ arr[i]
    return x

def main():
    arr = [1, 4, 2, 1, 3, 2, 3]
    print(find_single_number(arr))

main()