Given a string s, return true if a permutation of the string could form a palindrome.

 

Example 1:

Input: s = "code"
Output: false
Example 2:

Input: s = "aab"
Output: true
Example 3:

Input: s = "carerac"
Output: true
 

Constraints:

1 <= s.length <= 5000
s consists of only lowercase English letters.


Success
Details 
Runtime: 29 ms, faster than 88.08% of Python3 online submissions for Palindrome Permutation.
Memory Usage: 13.9 MB, less than 12.09% of Python3 online submissions for Palindrome Permutation.


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        
        facts = set()
        
        for char in s:
            if char not in facts:
                facts.add(char)
            else:
                facts.remove(char)
        return len(facts) <=1
