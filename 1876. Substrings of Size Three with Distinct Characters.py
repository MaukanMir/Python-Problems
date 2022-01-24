# A string is good if there are no repeated characters.

# Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.

# Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

# A substring is a contiguous sequence of characters in a string.

 

# Example 1:

# Input: s = "xyzzaz"
# Output: 1
# Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
# The only good substring of length 3 is "xyz".
# Example 2:

# Input: s = "aababcabc"
# Output: 4
# Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
# The good substrings are "abc", "bca", "cab", and "abc".
 

# Constraints:

# 1 <= s.length <= 100
# s​​​​​​ consists of lowercase English letters.

Success
Details 
Runtime: 39 ms, faster than 43.47% of Python3 online submissions for Substrings of Size Three with Distinct Characters.
Memory Usage: 14.1 MB, less than 73.51% of Python3 online submissions for Substrings of Size Three with Distinct Characters.



class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        start, count = 0, 0
        end = start+3
        
        while end<= len(s):
            if len(s[start:end]) == len(set(s[start:end])):
                count +=1
            start+=1
            end +=1
        return count
