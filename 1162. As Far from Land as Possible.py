
Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return -1.

The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

 

Example 1:


Input: grid = [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.
Example 2:


Input: grid = [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation: The cell (2, 2) is as far as possible from all the land with distance 4.

Success
Details 
Runtime: 1517 ms, faster than 10.73% of Python3 online submissions for As Far from Land as Possible.
Memory Usage: 14.8 MB, less than 53.22% of Python3 online submissions for As Far from Land as Possible.


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        ans,q = -1, deque()
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    grid[x][y] = -1
                    q.append([x,y])
        
        
        while q:
            x,y = q.popleft()
            
            for dr,dc in [[1,0], [-1,0], [0,-1], [0,1]]:
                row,col = x+dr, y + dc
                
                if not (0<= row < len(grid)) or not(0<= col < len(grid[0])) or grid[row][col] != 0:
                    continue
                grid[row][col] = grid[x][y] +2 if grid[x][y] == -1 else grid[x][y] +1
                ans = max(ans, grid[row][col])
                q.append([row,col])

        return ans
