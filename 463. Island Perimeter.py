
# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

# Example 1:


# Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image above.
# Example 2:

# Input: grid = [[1]]
# Output: 4
# Example 3:

# Input: grid = [[1,0]]
# Output: 4
 

# Constraints:

# row == grid.length
# col == grid[i].length
# 1 <= row, col <= 100
# grid[i][j] is 0 or 1.
# There is exactly one island in grid.


Success
Details 
Runtime: 736 ms, faster than 32.78% of Python3 online submissions for Island Perimeter.
Memory Usage: 22.6 MB, less than 10.13% of Python3 online submissions for Island Perimeter.


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        
        def dfs(r,c,visited):
            if (r,c) in visited:
                return 
            if r<0 or r>= len(grid) or c<0 or c>= len(grid[0]) or grid[r][c] ==0:
                self.total +=1
                return
            visited.add((r,c))
            
            for x,y in self.directions:
                dfs(x+r,y+c, visited)
        
        
        
        
        Rows,Cols = len(grid), len(grid[0])
        visited = set()
        self.total = 0
        self.directions = [(0,1),(1,0),(-1,0),(0,-1)]
        
        for r in range((Rows)):
            for c in range((Cols)):
                if grid[r][c] ==1:
                    dfs(r,c,visited)
        
        return self.total
