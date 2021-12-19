# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:

# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".

# Success
# Details 
# Runtime: 112 ms, faster than 82.10% of Python3 online submissions for Find All Anagrams in a String.
# Memory Usage: 14.9 MB, less than 99.92% of Python3 online submissions for Find All Anagrams in a String.

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []
        
        pCount,sCount = {},{}
        
        for i in range(len(p)):
            pCount[p[i]] = 1 + pCount.get(p[i],0)
            sCount[s[i]] = 1 + sCount.get(s[i],0)
            
        res = [0] if sCount == pCount else []
        leftPointer =0
           
        for r in range(len(p), len(s)):
            sCount[s[r]] =1 + sCount.get(s[r],0)
            sCount[s[leftPointer]] -=1
    
            if sCount[s[leftPointer]] ==0:
                sCount.pop(s[leftPointer])
            leftPointer +=1
            if sCount == pCount:
                    res.append(leftPointer)
        return res
           
