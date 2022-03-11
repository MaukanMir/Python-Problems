# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

# You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with newColor.

# Return the modified image after performing the flood fill.

 

# Example 1:


# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
# Example 2:

# Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2
# Output: [[2,2,2],[2,2,2]]

# Success
# Details 
# Runtime: 76 ms, faster than 74.87% of Python3 online submissions for Flood Fill.
# Memory Usage: 14.5 MB, less than 26.61% of Python3 online submissions for Flood Fill.



class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        
        
        ROWS,COLS = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor: return image

        def dfs(r,c):

            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1: dfs(r-1, c)
                if r+1 < ROWS: dfs(r+1, c)
                if c >= 1: dfs(r, c-1)
                if c+1 < COLS: dfs(r, c+1)
                
            
            
        
        

        dfs(sr,sc)
        return image
       
    class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        if image[sr][sc] == newColor:
            return image
        color = image[sr][sc]
        ROWS,COLS = len(image), len(image[0])
        
        def dfs(r,c):
            if r<0 or r>=ROWS or c<0 or c>= COLS or image[r][c] != color:
                return
            
            image[r][c] = newColor
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        
        dfs(sr,sc)
        return image
Runtime: 80 ms, faster than 83.96% of Python3 online submissions for Flood Fill.
Memory Usage: 14.2 MB, less than 38.12% of Python3 online submissions for Flood Fill.

