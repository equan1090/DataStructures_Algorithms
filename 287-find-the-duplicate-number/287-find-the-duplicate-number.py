class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]
        firstCycle = True
        
        while slow != fast or firstCycle:
            firstCycle = False
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        res = nums[0]
        while res != slow:
            res = nums[res]
            slow = nums[slow]
        return res
        