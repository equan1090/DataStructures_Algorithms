class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        r1 = grid[0]
        invert = [1 - val for val in grid[0]]
        
        for i in range(1, len(grid)):
            if r1 != grid[i] and invert != grid[i]:
                return False
        return True