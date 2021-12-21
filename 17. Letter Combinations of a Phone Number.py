# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



 

# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:

# Input: digits = ""
# Output: []
# Example 3:

# Input: digits = "2"
# Output: ["a","b","c"]
 

# Constraints:

# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].


# Success
# Details 
# Runtime: 28 ms, faster than 85.95% of Python3 online submissions for Letter Combinations of a Phone Number.
# Memory Usage: 14.2 MB, less than 86.58% of Python3 online submissions for Letter Combinations of a Phone Number.


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        
        digitsToChar = {"2":"abc",
                       "3":"def",
                        "4":"ghi",
                        "5":"jkl",
                        "6":"mno",
                        "7":"qprs",
                        "8":"tuv",
                        "9": "wxyz"}
        
        def backTrack(i,curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            
            for c in digitsToChar[digits[i]]:
                print(c)
                print(curStr)
                backTrack(i+1, curStr +c)
                
            
        if digits:
                backTrack(0,"")
            
        return res
