class Solution:

    def __init__(self, w: List[int]):
        self.w = w
		# 1. calculate relative frequency
        denom = sum(self.w)
        for i in range(len(self.w)):
            self.w[i] = self.w[i] / denom
        # 2. put relative frequencies on the number line between 0 and 1
		# Note self.w[-1] = 1
        for i in range(1,len(self.w)):
            self.w[i] += self.w[i-1]

    def pickIndex(self) -> int:
        N = random.uniform(0, 1)

        for index, weight in enumerate(self.w):
            if N <= weight:
                return index

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()