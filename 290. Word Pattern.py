
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false

Success
Details 
Runtime: 42 ms, faster than 61.87% of Python3 online submissions for Word Pattern.
Memory Usage: 13.9 MB, less than 73.45% of Python3 online submissions for Word Pattern.


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        if len(s) != len(pattern):
            return False
        map_index = {}
        for i in range(len(s)):
            one,two = s[i], pattern[i]
            
            char_letter = 'char' + one
            char_word = 'word' + two
            
            if char_letter not in map_index:
                map_index[char_letter] = i
            if char_word not in map_index:
                map_index[char_word] = i
            
            if map_index[char_letter] != map_index[char_word]:
                return False
        
        return True
