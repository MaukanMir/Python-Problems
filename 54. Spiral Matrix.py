


Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]



Success
Details 
Runtime: 45 ms, faster than 54.62% of Python3 online submissions for Spiral Matrix.
Memory Usage: 13.9 MB, less than 82.58% of Python3 online submissions for Spiral Matrix.


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        startRow, endRow = 0, len(matrix)-1
        startCol, endCol = 0, len(matrix[0])-1
        res = []
        while startCol <= endCol and startRow <= endRow:
            
            for row in range(startCol,endCol+1):
                res.append(matrix[startRow][row])
            
            for row in range(startRow+1, endRow+1):
                res.append(matrix[row][endCol])
                
            
            for row in reversed(range(startCol,endCol)):
                
                if startRow == endRow:
                    break
                res.append(matrix[endRow][row])
                
            for row in reversed(range(startRow+1,endRow)):
                
                if startCol == endCol:
                    break
                res.append(matrix[row][startCol])
                
            
            
            startCol +=1
            startRow +=1
            endCol -=1
            endRow -=1
        return res
