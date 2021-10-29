
# 9. Palindrome Number
# Easy

# 4255

# 1895

# Add to List

# Share
# Given an integer x, return true if x is palindrome integer.

# An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

 

# Example 1:

# Input: x = 121
# Output: true
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# Example 4:

# Input: x = -101
# Output: false
 

# Constraints:

# -231 <= x <= 231 - 1













# Success
# Details 
# Runtime: 60 ms, faster than 78.36% of Python3 online submissions for Palindrome Number.
# Memory Usage: 14.3 MB, less than 16.80% of Python3 online submissions for Palindrome Number.



# class Solution:
#     def isPalindrome(self, x: int) -> bool:
        
#         check = str(x)[::-1]
#         if check[-1] =="-":return False
#         return int(check) == x
