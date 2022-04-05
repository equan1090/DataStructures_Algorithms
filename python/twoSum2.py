'''
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1]
and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2]
of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.
'''

def twoSum(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        curSum = nums[left] + nums[right]
        if curSum == target:
            return [left + 1, right + 1]
        elif curSum < target:
            left += 1
        else:
            right -= 1
    return -1

numbers = [2,7,11,15]
print(twoSum(numbers, 9))
