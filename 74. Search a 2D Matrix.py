Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Success
Details 
Runtime: 92 ms, faster than 8.07% of Python3 online submissions for Search a 2D Matrix.
Memory Usage: 14.3 MB, less than 90.87% of Python3 online submissions for Search a 2D Matrix.


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ROWS, COLS = 0, len(matrix[0])-1
        
        while ROWS < len(matrix) and COLS >=0:
            if matrix[ROWS][COLS] > target:
                COLS-=1
            elif matrix[ROWS][COLS] < target:
                ROWS+=1
            else:
                return True

        return False
