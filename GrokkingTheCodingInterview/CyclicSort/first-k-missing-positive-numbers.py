# Given an unsorted array containing numbers and a number ‘k’, 
# find the first ‘k’ missing positive numbers in the array.

def find_first_k_missing_positive(nums, k):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if j < 0 or j >= len(nums) or nums[i] == nums[j]:
            i += 1
        else:
            nums[i], nums[j] = nums[j], nums[i]

    missing, largest = [], 0
    for i in range(len(nums)):
        if len(missing) == k: break
        elif nums[i] != i+1:
            missing.append(i + 1)
            largest = max(largest, nums[i])

    while len(missing) < k:
        if largest > missing[-1] + 1 and len(nums) < k:
            missing.append(missing[-1] + 1)
        else:
            missing.append(largest + 1)
            largest += 1
    return missing

assert(find_first_k_missing_positive([3, -1, 4, 5, 5], 3)) == [1, 2, 6]
assert(find_first_k_missing_positive([2, 3, 4], 3)) == [1, 5, 6]
assert(find_first_k_missing_positive([-2, -3, 4], 2)) == [1, 2]
assert(find_first_k_missing_positive([-2, -3, 4], 5)) == [1, 2, 3, 5, 6]