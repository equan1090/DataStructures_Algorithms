class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        startRow, endRow = 0, len(matrix) - 1
        startCol, endCol = 0, len(matrix[0]) - 1
        res = []
        while startRow <= endRow and startCol <= endCol:
            
            for col in range(startCol, endCol + 1):
                res.append(matrix[startRow][col])
            
            for row in range(startRow + 1, endRow + 1):
                res.append(matrix[row][endCol])
                
            for col in reversed(range(startCol, endCol)):
                if startRow >= endRow:
                    break
                res.append(matrix[endRow][col])
                
            
            for row in reversed(range(startRow + 1, endRow)):
                if startCol >= endCol:
                    break
                res.append(matrix[row][startCol])

            startRow += 1
            endRow -= 1
            startCol += 1
            endCol -= 1
        return res