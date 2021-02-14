# Given a set of positive numbers, find if we can partition it into two 
# subsets such that the sum of elements in both subsets is equal.

# Example:
# Input: {1, 2, 3, 4}
# Output: True
# Explanation: The given set can be partitioned into two subsets with 
# equal sum: {1, 4} & {2, 3}

def can_partition(nums):
    total_sum = sum(nums)
    n = len(nums)
    if total_sum % 2 != 0 or n == 0: 
        return False
    target_sum = total_sum // 2
    cache = [[None for x in range(target_sum + 1)] for y in range(len(nums))]
    return check_partition(nums, 0, target_sum, cache)

def check_partition(nums, current_index, target_sum, cache):
    if target_sum == 0 and current_index < len(nums):
        return True
    elif current_index >= len(nums):
        return False

    if cache[current_index][target_sum]:
        return cache[current_index][target_sum]

    left_side = False
    if nums[current_index] <= target_sum:
        left_side = check_partition(nums, current_index + 1, target_sum - nums[current_index], cache)
    right_side = check_partition(nums, current_index + 1, target_sum, cache)

    result = left_side or right_side
    cache[current_index][target_sum] = result
    return result

def can_partition_bottom_up(nums):
    n = len(nums)
    total_sum = sum(nums)
    if total_sum % 2 != 0 or n == 0: 
        return False
    
    target_sum = total_sum // 2
    dp = [[False for x in range(target_sum + 1)] for y in range(n)]

    for i in range(n):
        dp[i][0] = True

    for s in range(target_sum + 1):
        dp[0][s] = nums[0] == s

    for i in range(1, n):
        for s in range(1, target_sum + 1):
            if dp[i-1][s]:
                dp[i][s] = dp[i-1][s]
            elif nums[i] <= s:
                dp[i][s] = dp[i-1][s - nums[i]]
    
    return dp[n-1][target_sum]

def main():
    print("Can partition: " + str(can_partition_bottom_up([1, 2, 3, 4, 100])))
    print("Can partition: " + str(can_partition_bottom_up([1, 1, 3, 4, 7])))
    print("Can partition: " + str(can_partition_bottom_up([2, 3, 4, 6])))

main()