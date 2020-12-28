# We are given an unsorted array containing numbers taken 
# from the range 1 to ‘n’. The array can have duplicates, 
# which means some numbers will be missing. 
# Find all those missing numbers.

def find_missing_numbers(nums):
    duplicate_indexes = []
    for i in range(len(nums)):
        while nums[i] != i + 1:
            current = nums[i]
            if current == nums[current - 1]:
                duplicate_indexes.append(i) 
                break
            nums[i], nums[current - 1] = nums[current - 1], nums[i]
            if (current - 1) in duplicate_indexes: 
                duplicate_indexes.remove((current - 1))
    return [i + 1 for i in duplicate_indexes]

assert(find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1])) == [4, 6, 7]
assert(find_missing_numbers([2, 4, 1, 2])) == [3]
assert(find_missing_numbers([2, 3, 2, 1])) == [4]