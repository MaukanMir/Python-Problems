Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.


Success
Details 
Runtime: 148 ms, faster than 92.87% of Python3 online submissions for Maximum Number of Vowels in a Substring of Given Length.
Memory Usage: 15 MB, less than 21.38% of Python3 online submissions for Maximum Number of Vowels in a Substring of Given Length.


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        left,right, vowels = 0,0,'aeiou'
        count = sum([1 if s[i] in vowels else 0 for i in range(k) ])
        maxValue = count
        
        
        for i in range(len(s) -k):
            if s[i] in vowels:
                count -=1
            if s[i+k] in vowels:
                count +=1
            
            maxValue = max(maxValue, count)
        return maxValue
        
