Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

Success
Details 
Runtime: 57 ms, faster than 69.33% of Python3 online submissions for Valid Anagram.
Memory Usage: 14.4 MB, less than 97.47% of Python3 online submissions for Valid Anagram.



class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        counter = [0] * 26
        
        for i in range(len(s)):
            counter[ord(s[i]) - ord('a')]+=1
            counter[ ord(t[i]) - ord('a')] -=1
        
        print(counter)
        for i in counter:
            if i !=0:
                return False
        return True
