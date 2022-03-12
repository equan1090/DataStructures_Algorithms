'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
'''
def singleNumber(nums):
    result = 0
    for num in nums:
        #we use the XOR operator because (2 ^ 2), (3 ^ 3), (4 ^ 4) ... (n ^ n) == 0
        result ^= num
    return result
