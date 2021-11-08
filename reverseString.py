# 344. Reverse String
# Easy

# 3280

# 845

# Add to List

# Share
# Write a function that reverses a string. The input string is given as an array of characters s.

 

# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
 

# Constraints:

# 1 <= s.length <= 105
# s[i] is a printable ascii character.



Success
Details 
Runtime: 192 ms, faster than 92.39% of Python3 online submissions for Reverse String.
Memory Usage: 18.5 MB, less than 82.99% of Python3 online submissions for Reverse String.
  
  
  class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead
        """
        
        left, right = 0,len(s)-1
        
        while left < right:
            s[right], s[left], = s[left],s[right]
            left +=1
            right -=1
