class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        
        visited = set()
        q = deque([])
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    visited.add((r, c))
                    q.append((r, c))
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nR = r + dr
                nC = c + dc
                rowbounds = 0 <= nR < len(matrix)
                colbounds = 0 <= nC < len(matrix[0])
                
                if rowbounds and colbounds and (nR, nC) not in visited:
                    matrix[nR][nC] = matrix[r][c] + 1
                    visited.add((nR, nC))
                    q.append((nR, nC))
        return matrix
