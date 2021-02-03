# Given a set of distinct numbers, find all of its permutations.
# Permutation is defined as the re-arranging of the elements of the set. 
# For example, {1, 2, 3} has the following six permutations:
# {1, 2, 3}
# {1, 3, 2}
# {2, 1, 3}
# {2, 3, 1}
# {3, 1, 2}
# {3, 2, 1}
# If a set has ‘n’ distinct elements it will have 
# n
# !
# n! permutations.

from collections import deque

def find_permutations(nums):
    result = []
    permutations = deque()
    permutations.append([])
    for n in nums:
        for _ in range(len(permutations)):
            current = permutations.popleft()
            for i in range(len(current) + 1):
                updated = list(current)
                updated.insert(i, n)
                if len(updated) == len(nums):
                    result.append(updated)
                else:
                    permutations.append(updated)
    return result

def main():
    print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))
main()