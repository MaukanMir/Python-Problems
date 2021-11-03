# 20. Valid Parentheses
# Easy

# 9614

# 381

# Add to List

# Share
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false
# Example 4:

# Input: s = "([)]"
# Output: false
# Example 5:

# Input: s = "{[]}"
# Output: true

  
#  Success
# Details 
# Runtime: 24 ms, faster than 96.95% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 14.2 MB, less than 86.84% of Python3 online submissions for Valid Parentheses.

  class Solution:
    def isValid(self, s: str) -> bool:
        
        opening = "[{("
        closing = "]})"
        match ={"]":"[",")":"(","}":"{"}
        stack = []
        
        for i in s:
            if i in closing and stack ==[]:return False
            elif i in opening:
                stack.append(i)
            elif i in closing:
                if match[i] != stack[-1]:return False
                
                elif match[i] == stack[-1]:
                    stack.pop()
    
        return len(stack) ==0
  
  
  
