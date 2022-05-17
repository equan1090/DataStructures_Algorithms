class Solution:
    def numSimilarGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        group = 0 
        visited = set()
        for string_ in A:
            if(string_ in visited): continue
            visited.add(string_)
            self.dfs(string_,A,visited)
            group += 1
        return group

    def dfs(self,string_,A,visited):
        for i in range(len(A)):
            if(A[i] in visited): continue
            if(self.similar(A[i],string_)):
                visited.add(A[i])
                self.dfs(A[i],A,visited)

    def similar(self,A,B):
        diff = 0 
        for i in range(len(B)):
            if(A[i] != B[i]):
                diff+= 1
            if (diff > 2): return False
        return True