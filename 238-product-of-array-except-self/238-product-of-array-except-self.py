class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        product = [1, 1, 1, 1]
        left = [1, 1, 2, 6]
        Input: nums = [1,2,3,4]
        Output: [24,12,8,6]
        '''
        product = [1] * len(nums)
        
        left = 1
        for i in range(len(nums)):
            product[i] = left
            left *= nums[i]
        
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            product[i] *= right
            right *= nums[i]
        return product