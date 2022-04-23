# Evaluate the value of an arithmetic expression in Reverse Polish Notation.

# Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

# Note that division between two integers should truncate toward zero.

# It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.

 

# Example 1:

# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# Example 2:

# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
# Example 3:

# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22

Success
Details 
Runtime: 72 ms, faster than 78.94% of Python3 online submissions for Evaluate Reverse Polish Notation.
Memory Usage: 14.3 MB, less than 59.59% of Python3 online submissions for Evaluate Reverse Polish Notation.


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        for item in tokens:
            if item == '/':
                a,b = stack.pop(), stack.pop()
                stack.append( int(b  / a) )
            elif item =='*':
                a,b = stack.pop(), stack.pop()
                stack.append(b * a)
            elif item =='-':
                a,b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif item =="+":
                a,b = stack.pop(), stack.pop()
                stack.append(a + b)
            else:
                stack.append(int(item))
        return stack[0]
