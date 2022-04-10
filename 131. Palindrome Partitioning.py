Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.


Success
Details 
Runtime: 712 ms, faster than 81.27% of Python3 online submissions for Palindrome Partitioning.
Memory Usage: 30.4 MB, less than 34.61% of Python3 online submissions for Palindrome Partitioning.


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [],[]
        
        def backtrack(i):
            if i >= len(s):
                res.append(part[:])
                return
            
            for j in range(i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    part.append(s[i:j+1])
                    backtrack(j+1)
                    part.pop()
                    
        
        backtrack(0)
        
        return res
