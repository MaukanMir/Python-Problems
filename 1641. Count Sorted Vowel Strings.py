Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.

A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.

 

Example 1:

Input: n = 1
Output: 5
Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].
Example 2:

Input: n = 2
Output: 15
Explanation: The 15 sorted strings that consist of vowels only are
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.
Example 3:

Input: n = 33
Output: 66045

Success
Details 
Runtime: 7603 ms, faster than 5.00% of Python3 online submissions for Count Sorted Vowel Strings.
Memory Usage: 13.8 MB, less than 94.04% of Python3 online submissions for Count Sorted Vowel Strings.


class Solution:
    def countVowelStrings(self, n: int) -> int:
        
        total =0
        def backtrack(n,total):
            if n <= 0:
                return 1
            
            result =0
            
            for i in range(total,5+1):
                result += backtrack(n-1, i)
            
            return result
        
            
        
        return backtrack(n,1)
