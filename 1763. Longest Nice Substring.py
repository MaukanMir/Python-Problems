# A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase. For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b' appears, but 'B' does not.

# Given a string s, return the longest substring of s that is nice. If there are multiple, return the substring of the earliest occurrence. If there are none, return an empty string.

 

# Example 1:

# Input: s = "YazaAay"
# Output: "aAa"
# Explanation: "aAa" is a nice string because 'A/a' is the only letter of the alphabet in s, and both 'A' and 'a' appear.
# "aAa" is the longest nice substring.
# Example 2:

# Input: s = "Bb"
# Output: "Bb"
# Explanation: "Bb" is a nice string because both 'B' and 'b' appear. The whole string is a substring.
# Example 3:

# Input: s = "c"
# Output: ""
# Explanation: There are no nice substrings.

# Success
# Details 
# Runtime: 144 ms, faster than 37.32% of Python3 online submissions for Longest Nice Substring.
# Memory Usage: 14.3 MB, less than 63.64% of Python3 online submissions for Longest Nice Substring.



class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        key, end = "",len(s)
        
        for i in range(end):
            for j in range(i, end):
                if all(check.swapcase() in s[i:j+1] for check in s[i:j+1]):
                    if len(s[i:j+1]) > len(key):
                        key = s[i:j+1]
        return key
