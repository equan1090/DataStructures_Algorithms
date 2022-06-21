# Time complexity = O(n) for constructor and O(logn) for pickIndex
# Space complexity = O(n) for constructor and O(1) for pickIndex

class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        self.total_sum = 0
        
        for weight in w:
            self.total_sum += weight
            self.prefix_sums.append(self.total_sum)

    def pickIndex(self) -> int:
        random_target = self.total_sum * random.random()
        
        left, right = 0, len(self.prefix_sums)
        
        while left < right:
            middle = left + (right - left) // 2
            if self.prefix_sums[middle] >= random_target:
                right = middle
            else:
                left = middle + 1
        
        return left
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()