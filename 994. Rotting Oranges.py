You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.


Success
Details 
Runtime: 67 ms, faster than 63.96% of Python3 online submissions for Rotting Oranges.
Memory Usage: 14 MB, less than 60.99% of Python3 online submissions for Rotting Oranges.


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS, fresh = len(grid), len(grid[0]), 0
        stack = deque()
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] ==2:
                    stack.append((r,c))
                if grid[r][c] ==1:
                    fresh +=1
        
        stack.append((-1,-1))
        minutes, directions = -1, [[1,0], [-1,0], [0,-1], [0,1]]
        
        while stack:
            r,c = stack.popleft()
            
            if r ==-1:
                minutes +=1
                if stack:
                    stack.append((-1,-1))
            
            else:
                
                for R,C in directions:
                    rR, cC = r + R, c +C
                    
                    if rR >=0 and rR < ROWS and cC >=0 and cC < COLS:
                        if grid[rR][cC] ==1:
                            grid[rR][cC] =2
                            fresh -=1
                            stack.append((rR,cC))
        
        return minutes if fresh ==0 else -1
       

Success
Details 
Runtime: 54 ms, faster than 87.06% of Python3 online submissions for Rotting Oranges.
Memory Usage: 13.9 MB, less than 46.21% of Python3 online submissions for Rotting Oranges.
 class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh,time = 0,0
        q = deque()
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] ==2:
                    q.append([r,c])
                if grid[r][c]==1:
                    fresh+=1
        
        directions =[[1,0], [-1,0], [0,-1], [0,1]]
        while q and fresh >0:
            for i in range(len(q)):
                r,c = q.popleft()
                for dr,dc in directions:
                    row, col = dr+r, dc + c
                    
                    if row <0 or col <0 or col== COLS or row == ROWS or grid[row][col] !=1:
                        continue
                    grid[row][col] = 2
                    q.append([row,col])
                    fresh -=1
            
            time +=1
        
        
        return time if fresh == 0 else -1
