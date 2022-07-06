Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
 

Example 1:


Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true
Example 2:


Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false


Success
Details 
Runtime: 257 ms, faster than 49.87% of Python3 online submissions for Search a 2D Matrix II.
Memory Usage: 20.3 MB, less than 84.60% of Python3 online submissions for Search a 2D Matrix II.


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ROWS, COLS = 0, len(matrix[0])-1
        
        while ROWS < len(matrix) and COLS >=0:
            if matrix[ROWS][COLS] > target:
                COLS -=1
            elif matrix[ROWS][COLS] < target:
                ROWS +=1
            else:
                return True
        return False
