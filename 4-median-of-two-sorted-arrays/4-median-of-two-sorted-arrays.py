class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        short = nums1
        long = nums2
        total = (len(nums1) + len(nums2))
        half = total // 2
        
        if len(short) > len(long):
            short, long = long, short
        
        l = 0
        r = len(short) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2
            
            shortLeft = short[i] if i >= 0 else float('-inf')
            shortRight = short[i + 1] if (i + 1) < len(short) else float('inf')
            longLeft = long[j] if j >= 0 else float('-inf')
            longRight = long[j + 1] if (j + 1) < len(long) else float('inf')
            
            if shortLeft <= longRight and longLeft <= shortRight:
                
                if total % 2:
                    return min(shortRight, longRight)
                
                return (max(shortLeft, longLeft) + min(shortRight, longRight)) / 2
            
            elif shortLeft > longRight:
                r = i - 1
            else:
                l = i + 1
                

            
            
            