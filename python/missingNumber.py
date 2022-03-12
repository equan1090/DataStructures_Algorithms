'''
Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.
'''
def missingNumber(nums):
    fullRange = 0
    for i in range(len(nums) + 1):
        fullRange += i

    return fullRange - sum(nums)
