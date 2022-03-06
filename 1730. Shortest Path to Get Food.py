You are starving and you want to eat food as quickly as possible. You want to find the shortest path to arrive at any food cell.

You are given an m x n character matrix, grid, of these different types of cells:

'*' is your location. There is exactly one '*' cell.
'#' is a food cell. There may be multiple food cells.
'O' is free space, and you can travel through these cells.
'X' is an obstacle, and you cannot travel through these cells.
You can travel to any adjacent cell north, east, south, or west of your current location if there is not an obstacle.

Return the length of the shortest path for you to reach any food cell. If there is no path for you to reach food, return -1.

 

Example 1:


Input: grid = [["X","X","X","X","X","X"],["X","*","O","O","O","X"],["X","O","O","#","O","X"],["X","X","X","X","X","X"]]
Output: 3
Explanation: It takes 3 steps to reach the food.
Example 2:


Input: grid = [["X","X","X","X","X"],["X","*","X","O","X"],["X","O","X","#","X"],["X","X","X","X","X"]]
Output: -1
Explanation: It is not possible to reach the food.
Example 3:


Input: grid = [["X","X","X","X","X","X","X","X"],["X","*","O","X","O","#","O","X"],["X","O","O","X","O","O","X","X"],["X","O","O","O","O","#","O","X"],["X","X","X","X","X","X","X","X"]]
Output: 6
Explanation: There can be multiple food cells. It only takes 6 steps to reach the bottom food.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 200
grid[row][col] is '*', 'X', 'O', or '#'.
The grid contains exactly one '*'.

Success
Details 
Runtime: 593 ms, faster than 73.22% of Python3 online submissions for Shortest Path to Get Food.
Memory Usage: 20.1 MB, less than 32.20% of Python3 online submissions for Shortest Path to Get Food.


class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        
        ROWS,COLS,visited,directions = len(grid), len(grid[0]), set(), [(-1,0),(0,-1),(1,0),(0,1)]
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] =='*':
                    queue =deque([[r,c,0]])
                    break
        while queue:
            r,c,dist = queue.popleft()
            
            if grid[r][c] =='#':
                return dist
            
            for R, C in directions:
                newR,newC = r+R, c+C
                
                if newR >=0 and newR< ROWS and newC>=0 and newC< COLS and (newR,newC) not in visited and grid[newR][newC] != "X":
                    queue.append([newR,newC,dist+1])
                    visited.add((newR,newC))
        
        return -1
                
