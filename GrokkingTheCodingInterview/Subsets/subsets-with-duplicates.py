# Given a set of numbers that might contain duplicates, 
# find all of its distinct subsets.

def find_subsets(nums):
    subsets = []
    subsets.append([])
    start_index, end_index = 0, 0
    nums.sort()
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            start_index = end_index + 1
        end_index = len(subsets) - 1
        for j in range(start_index,end_index+1):
            new_set = list(subsets[j])
            new_set.append(nums[i])
            subsets.append(new_set)
    return subsets

def main():
    print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))

main()