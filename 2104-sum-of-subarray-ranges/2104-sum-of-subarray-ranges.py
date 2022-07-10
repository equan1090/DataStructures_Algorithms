class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
       
        dec_stack = []
        inc_stack = []
        
        sum = 0
        for i in range(len(nums) + 1):
            sum += self.pushToStack(dec_stack, nums, i, dec=True) - self.pushToStack(inc_stack, nums, i, dec=False)
        
        return sum
    

    def pushToStack(self, stack, nums, i, dec):
        sum = 0

        while stack and (i == len(nums) or self.popFromStack(stack, nums, i, dec)):
            pop_i = stack.pop()
            prev_i = -1 if not stack else stack[-1]
            

            sum += (pop_i - prev_i) * (i - pop_i) * nums[pop_i]
            
        stack.append(i)
        return sum
    

    def popFromStack(self, stack, nums, i, dec):
        # Return True if we need to pop from the stack to push the next index, else return False
        return (nums[stack[-1]] < nums[i] and dec) or (nums[stack[-1]] > nums[i] and not dec)