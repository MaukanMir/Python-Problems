# Given a string s, return the longest palindromic substring in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.
# Accepted
# 1,593,442
# Submissions
# 5,051,266

Success
Details 
Runtime: 1220 ms, faster than 51.83% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 14.2 MB, less than 93.56% of Python3 online submissions for Longest Palindromic Substring.


class Solution:
    def longestPalindrome(self, s: str) -> str:
        res =""
        resLen =0
        
        for i in range(len(s)):
            l,r = i,i
            while l>=0 and r< len(s) and s[l] == s[r]:
                if (r-l +1) > resLen:
                    res = s[l:r+1]
                    resLen = r-l +1
                l-=1
                r+=1
                
        
            l,r, = i, i+1
            while l >=0 and r < len(s) and s[l] == s[r]:
                if(r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = r- l +1
                l-=1
                r+=1
        return res
       
       

Success
Details 
Runtime: 960 ms, faster than 79.05% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 14 MB, less than 91.03% of Python3 online submissions for Longest Palindromic Substring.
 
 
 class Solution:
    def longestPalindrome(self, s: str) -> str:
        currentLongest = [0,1]
        
        for i in range(1,len(s)):
            odd = find(s, i-1, i+1)
            even = find(s,i-1, i)
            longest = max(odd, even, key = lambda x: x[1]- x[0])
            currentLongest = max(longest, currentLongest, key = lambda x: x[1]- x[0])
        
        return s[currentLongest[0]: currentLongest[1]]

def find(s, left, right):
    while left >=0 and right < len(s):
        if s[left] != s[right]:
            break
        
        left -=1
        right +=1
    return [left+1, right]
