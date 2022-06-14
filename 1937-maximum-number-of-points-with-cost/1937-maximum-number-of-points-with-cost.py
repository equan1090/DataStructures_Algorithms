class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        M, N = len(points), len(points[0])
        left = [0] * N
        right = [0] * N
        dp = points[0]
        for i in range(1, M):
            # process from left to right
            for j in range(N):
                if j == 0:
                    left[0] = dp[0]
                else:
                    left[j] = max(dp[j], left[j-1]-1)
            # process from right to left
            for j in range(N-1,-1,-1):
                if j == N-1:
                    right[N-1] = dp[N-1]
                else:
                    right[j] = max(dp[j], right[j+1]-1)
            # set the new max points at each column based on the max of going
            # left to right vs right to left
            for j in range(N):
                dp[j] = points[i][j] + max(left[j], right[j])
        return max(dp)