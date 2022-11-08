class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.dfs(candidates, target, [], [])
        
    def dfs(self, candidates, target, path, res):
        if target == 0:
            res.append(path)
        
        if target < 0:
            return
        
        for i in range(len(candidates)):
            self.dfs(candidates[i:], target - candidates[i], path+[candidates[i]], res)
        path = []
        return res