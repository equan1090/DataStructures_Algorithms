class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        arrLen = len(original)
        
        if arrLen != m*n:
            return []
        
        new = []
        
        index = 0
        
        for x in range(0, m):
            temp = []
            for y in range(0, n):
                temp.append(original[index])
                index += 1
            new.append(temp)
        
        return new