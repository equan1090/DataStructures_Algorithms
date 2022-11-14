class Solution:
    def wordBreak(self, s: str, wordDict: List[str],):
        
        
#         memo = {}
        
#         def memoize(target, wordDict):
#             if target == "":
#                 return True
#             if target in memo:
#                 return memo[target]
            
#             for word in wordDict:
#                 if target[:len(word)] == word and memoize(target[len(word):], wordDict):
#                     memo[target] = True
#                     return memo[target]
#             memo[target] = False
#             return memo[target]
        
#         return memoize(s, wordDict)
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
        