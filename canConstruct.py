# 383. Ransom Note
# Easy

# 1255

# 269

# Add to List

# Share
# Given two stings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

 

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true
 

# Constraints:

# 1 <= ransomNote.length, magazine.length <= 105
# ransomNote and magazine consist of lowercase English letters.



# Success
# Details 
# Runtime: 40 ms, faster than 93.93% of Python3 online submissions for Ransom Note.
# Memory Usage: 14.4 MB, less than 64.16% of Python3 online submissions for Ransom Note.
# Next challenges:


 class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        one = collections.Counter(ransomNote)
        two = collections.Counter(magazine)
        match =""
        for i in ransomNote:
            if i not in two:return False
            if i in two and two[i]>0:
                two[i] -=1
                
                match += i
        
        return match == ransomNote
