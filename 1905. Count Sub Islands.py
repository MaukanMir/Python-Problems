You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.

An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.

Return the number of islands in grid2 that are considered sub-islands.

 

Example 1:


Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
Output: 3
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. There are three sub-islands.
Example 2:


Input: grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
Output: 2 
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. There are two sub-islands.
 

Constraints:

m == grid1.length == grid2.length
n == grid1[i].length == grid2[i].length
1 <= m, n <= 500
grid1[i][j] and grid2[i][j] are either 0 or 1.

Success
Details 
Runtime: 3468 ms, faster than 63.25% of Python3 online submissions for Count Sub Islands.
Memory Usage: 109.8 MB, less than 27.71% of Python3 online submissions for Count Sub Islands.


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        ROWS,COLS,visited, islands = len(grid1), len(grid1[0]), set(), 0
        
        def dfs(r,c):
            if r<0 or r >= ROWS or c < 0 or c >= COLS or (r,c) in visited or grid2[r][c] == 0 :
                return True
            
            visited.add((r,c))
            check = True
            if grid1[r][c] ==0:
                check = False
            
            
            
        
            check = dfs(r+1, c) and check
            check = dfs(r-1,c) and check
            check = dfs(r,c+1) and check
            check = dfs(r,c-1) and check
        
            return check
          
            
        
            
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid2[r][c] == 1 and (r,c) not in visited and dfs(r,c):
                    islands+=1
        return islands
