from pydoc import cli


'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''


class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1: 1, 2: 2}

        def dp(n, memo):
            if n in memo:
                return memo[n]

            memo[n] = dp(n - 1, memo) + dp(n-2, memo)

            return memo[n]

        return dp(n, memo)
