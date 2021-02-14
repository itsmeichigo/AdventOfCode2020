# Given a set of positive numbers, determine if a subset exists whose sum is 
# equal to a given number ‘S’.

# Example:
# Input: {1, 2, 3, 7}, S=6
# Output: True
# The given set has a subset whose sum is '6': {1, 2, 3}

def can_partition(nums, target_sum):
  n = len(nums)
  if target_sum > sum(nums): 
    return False

  dp = [False for x in range(target_sum + 1)]

  dp[0] = True

  for s in range(1, target_sum+1):
    dp[s] = nums[0] == s

  for i in range(1, n):
    for s in range(target_sum, -1, -1):
      if not dp[s] and nums[i] <= s:
        dp[s] = dp[s - nums[i]]
  
  return dp[target_sum]  

def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 7], 6)))
  print("Can partition: " + str(can_partition([1, 2, 7, 1, 5], 10)))
  print("Can partition: " + str(can_partition([1, 3, 4, 8], 6)))

main()
