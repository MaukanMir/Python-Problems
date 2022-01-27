# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.

# Success
# Details 
# Runtime: 336 ms, faster than 63.77% of Python3 online submissions for Number of Islands.
# Memory Usage: 25.8 MB, less than 5.99% of Python3 online submissions for Number of Islands.

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS, COLS, visited = len(grid), len(grid[0]), set()
        
        def dfs(r,c):
            if r <0 or r>= ROWS or c<0 or c >=COLS or (r,c) in visited or grid[r][c] =='0':
                return False
            
            visited.add((r,c))
            return (
                dfs(r+1,c), dfs(r-1,c), dfs(r,c+1), dfs(r,c-1)
            )
        
        area =0
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in visited:
                    continue
                if grid[r][c] == '1' and dfs(r,c):
                    area+=1
        return area

       
 # Success
# Details 
# Runtime: 320 ms, faster than 72.65% of Python3 online submissions for Number of Islands.
# Memory Usage: 21.6 MB, less than 23.47% of Python3 online submissions for Number of Islands.



class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS, COLS, visited= len(grid), len(grid[0]), set()
        
        def bfs(r,c):
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            queue = deque()
            queue.append((r,c))
    
            while queue:
                X,Y = queue.popleft()
                
                for x,y in directions:
                    sideX, sideY = x+X, y+Y
                    
                    if sideX >=0 and sideX < ROWS and sideY>=0 and sideY < COLS and grid[sideX][sideY] =='1' and  (sideX,sideY) not in visited:
                        queue.append([sideX,sideY])
                        visited.add((sideX,sideY))
                         
            
            
        area =0
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited and grid[r][c] == '1':
                     bfs(r,c)
                     area+=1
        return area
