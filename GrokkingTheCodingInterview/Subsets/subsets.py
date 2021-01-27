# Given a set with distinct elements, 
# find all of its distinct subsets.

# bruteforce - O(N^2)
def find_subsets(nums):
    subsets = []
    subsets.append([])
    for i in range(1, len(nums)+1):
        j = 0
        for j in range(len(nums)):
            s = nums[j:j+i]
            if len(s) < i: break
            subsets.append(s)
    return subsets

# BFS - O(N*2^N)
def find_subsets_bfs(nums):
    subsets = []
    subsets.append([])
    for n in nums:
        for i in range(len(subsets)):
            new_set = list(subsets[i]) + [n]
            subsets.append(new_set)
    return subsets

def main():
    print("Here is the list of subsets: " + str(find_subsets_bfs([1, 3])))
    print("Here is the list of subsets: " + str(find_subsets_bfs([1, 5, 3])))

main()