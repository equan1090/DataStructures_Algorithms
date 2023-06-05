class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked = {}
        
        for i, n in enumerate(nums):
            compliment = target - n
            if compliment in checked:
                return [i, checked[compliment]]
            
            checked[n] = i
        return [-1, -1]