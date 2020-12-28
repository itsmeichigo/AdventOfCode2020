# We are given an unsorted array containing ‘n’ numbers 
# taken from the range 1 to ‘n’. The array has some numbers 
# appearing twice, find all these duplicate numbers 
# without using any extra space.

def find_all_duplicates(nums):
    for i in range(len(nums)):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
    return [nums[i] for i in range(len(nums)) if i != nums[i] - 1]

assert(find_all_duplicates([3, 4, 4, 5, 5])) == [4, 5]
assert(find_all_duplicates([5, 4, 7, 2, 3, 5, 3])) == [3, 5]