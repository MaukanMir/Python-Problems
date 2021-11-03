# 242. Valid Anagram
# Easy

# 3496

# 188

# Add to List

# Share
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

# Success
# Details 
# Runtime: 36 ms, faster than 95.66% of Python3 online submissions for Valid Anagram.
# Memory Usage: 14.6 MB, less than 31.79% of Python3 online submissions for Valid Anagram.





class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        one = collections.Counter(s)
        two = collections.Counter(t)
        
        for key in one:
            if key not in t:return False
            elif two[key] < one[key]: return False
        
        for key in two:
            if key not in s:return False
            elif two[key] > one[key]:return False

        return True
