Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

 

Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 
Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 
Example 3:

Input: s = "abc"
Output: 1



Success
Details 
Runtime: 360 ms, faster than 37.19% of Python3 online submissions for Number of Substrings Containing All Three Characters.
Memory Usage: 14.2 MB, less than 94.04% of Python3 online submissions for Number of Substrings Containing All Three Characters.


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        check, charCount,windowStart, matched, total = "abc", Counter("abc"), 0, 0, 0
        
        
        for windowEnd in range(len(s)):
            charRight = s[windowEnd]
            charCount[charRight]-=1
            if charCount[charRight] ==0:
                matched +=1
            
            
            while matched == len(check):
                if matched == len(charCount):
                    total += len(s)- windowEnd
                charLeft = s[windowStart]
                if charCount[charLeft] ==0:
                    matched -=1
                charCount[charLeft] +=1
                windowStart+=1

        return total
