# Given an unsorted array containing numbers, 
# find the smallest missing positive number in it.

def find_first_missing_positive(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if j < 0 or j >= len(nums) or nums[i] == nums[j]: 
            i += 1
            continue
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
    for i in range(len(nums)):
        if nums[i] != i+1: return i + 1
    return None

assert(find_first_missing_positive([-3, 1, 5, 4, 2])) == 3
assert(find_first_missing_positive([3, -2, 0, 1, 2])) == 4
assert(find_first_missing_positive([3, 2, 5, 1])) == 4