
'''
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that
each unique element appears only once. The relative order of the elements should be kept the same.
'''
def removeDuplicates(nums):

    '''
    Input: nums = [0,0,1,1,1,2,2,3,3,4]
    Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
    '''
    left = 0
    right = 1
    while right < len(nums):
        if nums[left] != nums[right]:
            left += 1
            nums[left] = nums[right]
        right += 1
    return left + 1
