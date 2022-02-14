Given an m x n integer matrix grid, return the maximum score of a path starting at (0, 0) and ending at (m - 1, n - 1) moving in the 4 cardinal directions.

The score of a path is the minimum value in that path.

For example, the score of the path 8 → 4 → 5 → 9 is 4.
 

Example 1:


Input: grid = [[5,4,5],[1,2,6],[7,4,6]]
Output: 4
Explanation: The path with the maximum score is highlighted in yellow. 
Example 2:


Input: grid = [[2,2,1,2,2,2],[1,2,2,2,1,2]]
Output: 2
Example 3:


Input: grid = [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
0 <= grid[i][j] <= 109

Success
Details 
Runtime: 2292 ms, faster than 34.97% of Python3 online submissions for Path With Maximum Minimum Value.
Memory Usage: 17.3 MB, less than 18.26% of Python3 online submissions for Path With Maximum Minimum Value.


class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS, visited  = len(grid), len(grid[0]), set()
        
        start, minValue = [(-grid[0][0], 0,0)], float('+inf')
        
        while start:
            distance,r,c = heapq.heappop(start)
            minValue = min(minValue, -distance)
            visited.add((r,c))
            if r == ROWS-1 and c == COLS-1:
                return minValue
            i, j = r,c
            
            possible=[(x,y) for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)] if 0<=x<len(grid) and 0<=y<len(grid[0]) and (x,y) not in visited]
            for x,y in possible:
                
                heapq.heappush(start,(-grid[x][y],x,y))
