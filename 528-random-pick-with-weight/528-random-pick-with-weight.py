class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        running_sum = 0
        for weight in w:
            running_sum += weight
            self.prefix_sums.append(running_sum)
        self.total_sum = running_sum

    def pickIndex(self) -> int:
        target = random.random() * self.total_sum
        left, right = 0, len(self.prefix_sums) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if target > self.prefix_sums[mid]:
                left = mid
            else:
                right = mid
        if self.prefix_sums[left] >= target:
            return left
        return right


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()