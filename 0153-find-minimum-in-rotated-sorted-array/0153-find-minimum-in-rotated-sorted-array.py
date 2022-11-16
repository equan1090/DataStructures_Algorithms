class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        l = 0
        r = len(num) - 1
        while l < r:
            m = (l + r) // 2
            if num[m] > num[r]:
                l = m + 1
            else:
                r = m
        return num[l]