def maxSubArray(nums):
    #Initalize maxSub because we know it is non empty and there might be negative numbers
    maxSub = nums[0]
    curSum = 0

    for n in nums:
        #if the currentSum is negative then we know we dont need it since we are looking for max
        if curSum < 0:
            #reset curSum if curSum ever goes negative
            curSum = 0
        curSum += n
        maxSub = max(maxSub, curSum)
    return maxSub
