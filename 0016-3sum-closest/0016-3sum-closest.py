class Solution(object):
    def threeSumClosest(self, nums, target):
	    # sort array in ascending order 
        nums.sort()
        closestSum = float('inf')
        for i in range(len(nums)-2):

            left = i+1
            right = len(nums)-1

            while left < right:

                currSum = nums[i] + nums[left] + nums[right]

                if abs(target - closestSum) > abs(target - currSum):
                    closestSum = currSum  
                if currSum > target:
                    right -=1

                elif currSum < target:
                    left +=1

                else:
                    return target

        return closestSum
               
        