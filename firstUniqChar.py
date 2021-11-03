

# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

# Example 1:

# Input: s = "leetcode"
# Output: 0
# Example 2:

# Input: s = "loveleetcode"
# Output: 2
# Example 3:

# Input: s = "aabb"
# Output: -1
 

# Constraints:

# 1 <= s.length <= 105
# s consists of only lowercase English letters.


# Runtime: 120 ms, faster than 67.42% of Python3 online submissions for First Unique Character in a String.
# Memory Usage: 14.5 MB, less than 45.25% of Python3 online submissions for First Unique Character in a String.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        for idx, i in enumerate(s):
            if i not in s[:idx] and i not in s[idx+1:]:return idx
        return -1
