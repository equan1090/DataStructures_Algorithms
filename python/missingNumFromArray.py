'''
Given an array nums of n integers where nums[i] is in the range [1, n],
return an array of all the integers in the range [1, n] that do not appear in nums.
'''
def findDisappearedNumbers(nums):
 
    for i in range(len(nums)):
        idx = abs(nums[i]) - 1
        nums[idx] = -abs(nums[idx])
    return [i + 1 for i in range(len(nums)) if nums[i] > 0]
