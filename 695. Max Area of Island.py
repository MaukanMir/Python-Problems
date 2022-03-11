# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0.

 

# Example 1:


# Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.
# Example 2:

# Input: grid = [[0,0,0,0,0,0,0,0]]
# Output: 0


# Success
# Details 
# Runtime: 160 ms, faster than 55.58% of Python3 online submissions for Max Area of Island.
# Memory Usage: 18 MB, less than 15.89% of Python3 online submissions for Max Area of Island.


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        
        directions = [ [1,0], [0,1], [-1,0], [0,-1]  ]
       
        visited = set()
        def isValid(r,c):
            if r>=0 and r<ROWS and c>=0 and c< COLS and grid[r][c] ==1 and (r,c) not in visited:
                visited.add((r,c))
                return True
            return False
        
        def dfs(r,c):
            
            if isValid(r,c):
                return (1 + dfs(r+1,c)+
                        dfs(r-1, c)+
                        dfs(r,c+1)+
                        dfs(r,c-1))
                        
            return 0
        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = max(area, dfs(r,c))
        return area

       
 Success
Details 
Runtime: 152 ms, faster than 81.58% of Python3 online submissions for Max Area of Island.
Memory Usage: 18 MB, less than 9.60% of Python3 online submissions for Max Area of Island.      
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        if not grid: return 0

        ROWS,COLS, visited = len(grid), len(grid[0]), set()

        def dfs(r,c):
            if r<0 or r>= ROWS or c<0 or c>=COLS or (r,c) in visited or grid[r][c] ==0:
                return 0

            visited.add((r,c))

            return (1+ dfs(r+1,c)+
                     dfs(r-1,c)+
                     dfs(r,c+1)+
                     dfs(r,c-1)
                    )

        score =0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] ==1:
                    score = max(dfs(r,c), score)

        return score
