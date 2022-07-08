Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

 

Example 1:


Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
Example 2:


Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]

Success
Details 
Runtime: 777 ms, faster than 78.00% of Python3 online submissions for 01 Matrix.
Memory Usage: 17.6 MB, less than 24.08% of Python3 online submissions for 01 Matrix.

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        ROWS, COLS = len(mat), len(mat[0])
        visited = set()
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] ==0:
                    q.append([r,c])
                    visited.add((r,c))
                else:
                    mat[r][c] = math.inf
    
        
        
        dist =0
        while q:
            dist+=1
            for i in range(len(q)):
                r,c = q.popleft()
                
                for dr,dc in [[1,0],[0,1], [-1,0], [0,-1]]:
                    row, col = r+ dr, c +dc
                    
                    if (0<=row < ROWS) and (0<=col < COLS) and (row,col) not in visited and dist < mat[row][col]:
                        q.append([row,col])
                        visited.add((row,col))
                        mat[row][col] = dist
        return mat
