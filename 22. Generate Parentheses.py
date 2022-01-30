Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8

Success
Details 
Runtime: 32 ms, faster than 91.23% of Python3 online submissions for Generate Parentheses.
Memory Usage: 14.2 MB, less than 98.61% of Python3 online submissions for Generate Parentheses.


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        values = []
        
        def backtrack(check, l,r):
            if len(check) == n*2:
                values.append(check)
            if l < r:
                return 
            if l < n:
                backtrack(check +"(", l+1, r)
            if l >r:
                backtrack(check + ")", l, r+1)
        backtrack("",0,0)
        return values
