345. Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.

 

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"

Success
Details 
Runtime: 107 ms, faster than 25.65% of Python3 online submissions for Reverse Vowels of a String.
Memory Usage: 14.8 MB, less than 93.28% of Python3 online submissions for Reverse Vowels of a String.


class Solution:
    def reverseVowels(self, s: str) -> str:
        
        leftPointer, rightPointer, vowels, s = 0, len(s)-1, "aeiouAEIOU", list(s)
        
        while leftPointer < rightPointer:
            print(s[leftPointer])
            if s[leftPointer] not in vowels and s[rightPointer] not in vowels:
                leftPointer +=1
                rightPointer -=1
                continue
            if s[leftPointer] in vowels and s[rightPointer] in vowels: 
                s[leftPointer], s[rightPointer] = s[rightPointer], s[leftPointer]
                rightPointer -=1
                leftPointer +=1
                continue
            if s[leftPointer] in vowels and s[rightPointer] not in vowels:
                rightPointer -=1
            if s[leftPointer] not in vowels:
                leftPointer +=1
                
            
        
        return "".join(s)
