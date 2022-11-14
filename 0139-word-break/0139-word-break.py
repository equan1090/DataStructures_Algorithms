class Solution:
    def wordBreak(self, s: str, wordDict: List[str],):

        return self.dfs(s, wordDict, {})

    def dfs(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
        
        if not s:
            return True
        
        for word in wordDict:
            if s[:len(word)] == word and self.dfs(s[len(word):], wordDict, memo):
                memo[s] = True
                return memo[s]
        memo[s] = False
        return memo[s]
        