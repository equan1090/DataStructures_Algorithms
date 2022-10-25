class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        color = image[sr][sc]
        self.dfs(image, sr, sc, newColor, color)
        
        return image
    def dfs(self, image, sr, sc, newColor, color):
        rowbounds = 0 <= sr < len(image)
        colbounds = 0 <= sc < len(image[0])
        if not rowbounds or not colbounds or image[sr][sc] == newColor or image[sr][sc] != color:
            return
        image[sr][sc] = newColor

        self.dfs(image, sr + 1, sc, newColor, color)
        self.dfs(image, sr - 1, sc, newColor, color)
        self.dfs(image, sr, sc + 1, newColor, color)
        self.dfs(image, sr, sc - 1, newColor, color)

    
        