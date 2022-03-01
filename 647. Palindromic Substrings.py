Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.

Success
Details 
Runtime: 124 ms, faster than 88.75% of Python3 online submissions for Palindromic Substrings.
Memory Usage: 13.9 MB, less than 69.72% of Python3 online submissions for Palindromic Substrings.


class Solution:
    def countSubstrings(self, s: str) -> int:
        
        palis =0
        
        for i in range(len(s)):
            palis += findPali(s,i,i)
            palis += findPali(s,i,i+1)
        
        
        return palis
    
def findPali(string,lo, high):
    
    total =0
    
    while lo >=0 and high < len(string):
        if string[lo] != string[high]:
            break
        lo , high = lo-1, high +1
        
        total +=1
    
    return total
