# In a non-empty array of numbers, every number appears exactly twice except 
# two numbers that appear only once. Find the two numbers that appear only once.

# Example:
# Input: [1, 4, 2, 1, 3, 5, 6, 2, 3, 5]
# Output: [4, 6]

def find_single_numbers(nums):
    x = nums[0]
    for i in range(1, len(nums)):
        x ^= nums[i]

    # result of x will be n1 ^ n2. As n1 != n2 they have at least 1 different bit,
    # causing that bit to be 1 in x
    # So find that rightmost bit with value of 1 using bitwise AND of x & 1
    # and gradually shift to left until reaching 1 
    rightmost_diff_bit = 1
    while (rightmost_diff_bit & x) == 0:
        rightmost_diff_bit = rightmost_diff_bit << 1
    
    # then separate nums into 2 groups - one with similar bit to rightmost diff bit,
    # and one without. n1 and n2 will be in different group
    # using XOR on each group will help find them 🤯
    n1, n2 = 0, 0
    for n in nums:
        if n & rightmost_diff_bit:
            n1 ^= n
        else:
            n2 ^= n
    return [n1, n2]


def main():
    print('Single numbers are:' +
            str(find_single_numbers([1, 4, 2, 1, 3, 5, 6, 2, 3, 5])))
    print('Single numbers are:' + str(find_single_numbers([2, 1, 3, 2])))

main()