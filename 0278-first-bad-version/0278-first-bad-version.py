# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        r = n
        l = 0
        while(l<=r):
            mid = l + (r-l)//2
            if isBadVersion(mid)==False:
                l = mid+1
            else:
                r = mid-1
        return l