class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1] * len(nums)
        
        left = 1
        for i in range(len(nums)):
            products[i] = left
            left *= nums[i]
        
        right = 1
        for i in range(len(nums) -1, -1, -1):
            products[i] *= right
            right *= nums[i]
        return products