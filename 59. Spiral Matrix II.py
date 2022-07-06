
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

 

Example 1:


Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:

Input: n = 1
Output: [[1]]
 

Constraints:

1 <= n <= 20

Success
Details 
Runtime: 43 ms, faster than 67.10% of Python3 online submissions for Spiral Matrix II.
Memory Usage: 14 MB, less than 36.05% of Python3 online submissions for Spiral Matrix II.

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for j in range(n)] for i in range(n)]
        
        start =1
        startRow, endRow = 0, len(matrix)-1
        startCol, endCol = 0, len(matrix[0])-1
        
        while startRow <= endRow and startCol <= endCol:
            
            for row in range(startRow,endRow+1):
                matrix[startCol][row] = start
                start+=1
            
            
            for col in range(startCol+1, endCol+1):
                matrix[col][endRow] = start
                start+=1
            
            for row in reversed(range(startRow,endRow)):
                if endCol == startCol:
                    break
                matrix[endCol][row] = start
                start+=1
            
            for row in reversed(range(startCol+1,endCol)):
                
                if startRow == endRow:
                    break
                
                matrix[row][startCol] = start
                start+=1
            
            
            endCol-=1
            endRow -=1
            startRow +=1
            startCol +=1
        return matrix
