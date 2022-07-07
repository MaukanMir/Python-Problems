You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

 

Example 1:


Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.
Example 2:


Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: All 1s are either on the boundary or can reach the boundary.

Success
Details 
Runtime: 950 ms, faster than 46.83% of Python3 online submissions for Number of Enclaves.
Memory Usage: 17.1 MB, less than 19.84% of Python3 online submissions for Number of Enclaves.

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited, islands = set(), 0
        
        def dfs(r,c):
            if not (0<= r < ROWS) or not (0<=c < COLS) or grid[r][c] != 1 or (r,c) in visited:
                return
            
            visited.add((r,c))
            
            grid[r][c] = 0
            
            dfs(r+1,c),
            dfs(r-1,c),
            dfs(r,c+1),
            dfs(r,c-1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] ==1 and (r in [0,ROWS-1] or c in [0,COLS-1]):
                    dfs(r,c)
        
        
        for r in range(ROWS):
            islands += sum(grid[r])
        
        return islands

       
       Success
Details 
Runtime: 550 ms, faster than 94.18% of Python3 online submissions for Number of Enclaves.
Memory Usage: 15.5 MB, less than 69.57% of Python3 online submissions for Number of Enclaves.
 
 class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited, islands = set(), 0
        
        def bfs(r,c):
            q = deque([])
            q.append([r,c])
            
            directions = [ [1,0], [0,1], [-1,0], [0,-1] ]
            grid[r][c] = 0
            visited.add((r,c))
            while q:
                r,c = q.popleft()
                for dr,dc in directions:
                    row,col = r+dr,c+dc

                    if not (0<=row < ROWS) or not (0<=col <COLS) or grid[row][col] != 1 or (row,col) in visited:
                        continue

                    visited.add((row,col))
                    q.append([row,col])
                    grid[row][col] = 0
        
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] ==1 and (r in [0,ROWS-1] or c in [0,COLS-1]):
                    bfs(r,c)
        
        for r in range(ROWS):
            islands += sum(grid[r])
        return islands
