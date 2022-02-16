Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

 

Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
Example 2:

Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it was not in the typed output.
 

Constraints:

1 <= name.length, typed.length <= 1000
name and typed consist of only lowercase English letters.

Success
Details 
Runtime: 33 ms, faster than 71.93% of Python3 online submissions for Long Pressed Name.
Memory Usage: 13.8 MB, less than 93.09% of Python3 online submissions for Long Pressed Name.



class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        
        
        nameL, typedL = 0,0
        
        while nameL < len(name) and typedL < len(typed):
            
            if name[nameL] == typed[typedL]: 
                typedL +=1
                nameL +=1
            elif nameL >0 and name[nameL-1] == typed[typedL]: typedL +=1
            
            else:
                return False
            

        while typedL < len(typed):
            if name[nameL-1] != typed[typedL]: return False
            else:
                typedL +=1
        
        return  False if nameL < len(name) else True
