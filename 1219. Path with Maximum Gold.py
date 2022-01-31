

Success
Details 
Runtime: 1543 ms, faster than 63.71% of Python3 online submissions for Path with Maximum Gold.
Memory Usage: 13.8 MB, less than 99.16% of Python3 online submissions for Path with Maximum Gold.


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        
        ROWS,COLS, maxValue = len(grid), len(grid[0]), 0
        
        def dfs(r,c,current):
            if r <0 or r>= ROWS or c<0 or c >= COLS or grid[r][c] == 0:
                return current
            
            val = grid[r][c]
            grid[r][c] =0
            
            maxValue = max(
            dfs(r+1,c,current + val),
                dfs(r-1,c,current + val),
                dfs(r,c+1,current + val),
                dfs(r,c-1,current+val)
            
            )
            
            grid[r][c] = val
            
            return maxValue
        
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] != 0:
                   maxValue=  max(maxValue, dfs(r,c,0))
        return maxValue
            
