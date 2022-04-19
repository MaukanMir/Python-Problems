A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.


Success
Details 
Runtime: 49 ms, faster than 82.00% of Python3 online submissions for Valid Palindrome.
Memory Usage: 19.2 MB, less than 9.81% of Python3 online submissions for Valid Palindrome.


class Solution:
    def isPalindrome(self, s: str) -> bool:
        check = "".join([n.lower() for n in s if n.isalnum()])
        return True if check[::-1] == check or check =="" else False
