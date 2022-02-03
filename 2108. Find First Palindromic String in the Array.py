Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".

A string is palindromic if it reads the same forward and backward.

 

Example 1:

Input: words = ["abc","car","ada","racecar","cool"]
Output: "ada"
Explanation: The first string that is palindromic is "ada".
Note that "racecar" is also palindromic, but it is not the first.
Example 2:

Input: words = ["notapalindrome","racecar"]
Output: "racecar"
Explanation: The first and only string that is palindromic is "racecar".
Example 3:

Input: words = ["def","ghi"]
Output: ""
Explanation: There are no palindromic strings, so the empty string is returned.

Success
Details 
Runtime: 69 ms, faster than 74.44% of Python3 online submissions for Find First Palindromic String in the Array.
Memory Usage: 13.9 MB, less than 98.79% of Python3 online submissions for Find First Palindromic String in the


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        
        for i in words:
            if i == i[::-1]:return i
        return ""
