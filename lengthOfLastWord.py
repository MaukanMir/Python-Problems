

# 58. Length of Last Word
# Easy

# 259

# 33

# Add to List

# Share
# Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.

 

# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3:

# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.
 

# Constraints:

# 1 <= s.length <= 104
# s consists of only English letters and spaces ' '.
# There will be at least one word in s.


# Success
# Details 
# Runtime: 32 ms, faster than 68.30% of Python3 online submissions for Length of Last Word.
# Memory Usage: 14.4 MB, less than 6.61% of Python3 online submissions for Length of Last Word.




def lengthOfLastWord(self, s: str) -> int:
        if not s:return 0
        
        reversed_s = s[::-1].lstrip()
        if " " not in reversed_s: return len(reversed_s)
        return reversed_s.index(" ")
     

#      Runtime: 28 ms, faster than 86.99% of Python3 online submissions for Length of Last Word.
# Memory Usage: 14.3 MB, less than 63.90% of Python3 online submissions for Length of Last Word.

     
def lengthOfLastWord(self, s: str) -> int:
        if not s:return 0
        
        reversed_s = s[::-1].lstrip()
        for i in range(len(reversed_s)):
            if reversed_s[i] ==" ":
                return i
        return i+1
