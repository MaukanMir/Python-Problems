Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
 

Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.


Success
Details 
Runtime: 32 ms, faster than 82.32% of Python3 online submissions for Backspace String Compare.
Memory Usage: 13.8 MB, less than 93.53% of Python3 online submissions for Backspace String Compare.

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        seen, seen2 = [], []
        
        for i in s:
            if i != "#":
                seen.append(i)
            elif i == "#" and len(seen) >0: seen.pop()
        
        for i in t:
            if i != "#":
                seen2.append(i)
            elif i == "#" and len(seen2) >0: seen2.pop()
        
        return seen == seen2
