

  
  
 Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

Success
Details 
Runtime: 36 ms, faster than 76.51% of Python3 online submissions for Valid Parentheses.
Memory Usage: 13.8 MB, less than 74.55% of Python3 online submissions for Valid Parentheses.
  
  class Solution:
    def isValid(self, s: str) -> bool:
        stack, matches = [], {')':'(','}':'{',']':'['}
        
        for bracket in s:
            if bracket in matches and stack == []:
                return False
            elif bracket not in matches:
                stack.append(bracket)
            elif bracket in matches and matches[bracket] != stack[-1]:
                return False
            elif bracket in matches and matches[bracket] == stack[-1]:
                stack.pop()
        
        return stack == []
