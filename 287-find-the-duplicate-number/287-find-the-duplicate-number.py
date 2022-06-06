class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]
        firstCycle = True
        while slow != fast or firstCycle:
            slow = nums[slow]
            fast = nums[nums[fast]]
            firstCycle = False
        
        res = nums[0]
        while res != slow:
            slow = nums[slow]
            res = nums[res]
        return res