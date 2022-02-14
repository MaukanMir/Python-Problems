Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.

 

Example 1:

Input: s = "ab-cd"
Output: "dc-ba"
Example 2:

Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"

Success
Details 
Runtime: 24 ms, faster than 97.87% of Python3 online submissions for Reverse Only Letters.
Memory Usage: 14 MB, less than 71.47% of Python3 online submissions for Reverse Only Letters.


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        
        s = list(s)
        leftPointer, rightPointer = 0, len(s)-1
        
        while leftPointer < rightPointer:
            if not s[leftPointer].isalpha() and not s[rightPointer].isalpha():
                leftPointer +=1
                rightPointer -=1
                continue
            if not s[leftPointer].isalpha():
                leftPointer +=1
                continue
            if not s[rightPointer].isalpha():
                rightPointer -=1
                continue
            if s[leftPointer].isalpha() and s[rightPointer].isalpha( ):
                s[leftPointer], s[rightPointer] = s[rightPointer], s[leftPointer]
                leftPointer +=1
                rightPointer -=1
                
            
            
        
        return "".join(s)
