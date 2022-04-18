'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
'''
def longestConsecutive(nums):
    setNums = set(nums)
    longest = 0
    for num in setNums:
        if num - 1 in setNums:
            continue

        current = 0
        while num + current in setNums:
            current += 1
        longest = max(longest, current)
    return longest
