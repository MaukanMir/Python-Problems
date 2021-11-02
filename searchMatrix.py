


# 74. Search a 2D Matrix
# Medium

# 4911

# 224

# Add to List

# Share
# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
 

# Example 1:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# Example 2:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104





# Success
# Details 
# Runtime: 44 ms, faster than 74.33% of Python3 online submissions for Search a 2D Matrix.
# Memory Usage: 14.6 MB, less than 86.72% of Python3 online submissions for Search a 2D Matrix.



class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i in range(len(matrix)):
            col = (matrix[i])
            if target in col:
                return True
        return False
