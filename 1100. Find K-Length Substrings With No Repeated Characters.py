Given a string s and an integer k, return the number of substrings in s of length k with no repeated characters.

 

Example 1:

Input: s = "havefunonleetcode", k = 5
Output: 6
Explanation: There are 6 substrings they are: 'havef','avefu','vefun','efuno','etcod','tcode'.
Example 2:

Input: s = "home", k = 5
Output: 0
Explanation: Notice k can be larger than the length of s. In this case, it is not possible to find any substring.

Success
Details 
Runtime: 64 ms, faster than 55.01% of Python3 online submissions for Find K-Length Substrings With No Repeated Characters.
Memory Usage: 14.1 MB, less than 94.86% of Python3 online submissions for Find K-Length Substrings With No Repeated Characters.


class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        
        values = Counter(s[:k])
        result =1 if len(values) == k else 0
        
        for i in range(k,len(s)):
            values[s[i]] +=1
            values[s[i-k]] -=1
            if values[s[i-k]] ==0: del values[s[i-k]]
            if len(values) == k: result+=1
        return result
