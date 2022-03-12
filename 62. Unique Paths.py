

Success
Details 
Runtime: 35 ms, faster than 77.39% of Python3 online submissions for Unique Paths.
Memory Usage: 13.9 MB, less than 84.73% of Python3 online submissions for Unique Paths.

  
  There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        grid = [[1] * n for i in range(m)]
        
        for r in range(1, len(grid)):
            for c in range(1, len(grid[0])):
                grid[r][c] = grid[r-1][c] + grid[r][c-1]
        
        return grid[-1][-1]
 

