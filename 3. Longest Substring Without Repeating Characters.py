# 3. Longest Substring Without Repeating Characters
# Medium

# 18624

# 853

# Add to List

# Share
# Given a string s, find the length of the longest substring without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
# Example 4:

# Input: s = ""
# Output: 0



Success
Details 
Runtime: 60 ms, faster than 81.58% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 14.3 MB, less than 80.52% of Python3 online submissions for Longest Substring Without Repeating Characters.
Next challenges:
  
  
  
  
  
  
  class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        ans = 0
        i = 0
        seen = {}
        
        for j in range(len(s)):
            check = s[j]
            if check in seen:
                i = max(seen[check],i)
            
            ans = max(ans, j-i+1)
            seen[check] = j+1
        return ans
       

     
     
     
#      Runtime: 52 ms, faster than 92.16% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 14.5 MB, less than 25.11% of Python3 online submissions for Longest Substring Without Repeating Characters.
#    class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l =0
        result =0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            result = max(result,r-l+1)
        return result
       
       
  Success
Details 
Runtime: 52 ms, faster than 95.36% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 14.1 MB, less than 93.81% of Python3 online submissions for Longest Substring Without Repeating Characters.
 
 
 class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:return 0
        
        longest, seen, startIdx = [0,1], {}, 0
        
        for i, char in enumerate(s):
            if char in seen:
                startIdx = max(startIdx, seen[char]+1)
            if longest[1] - longest[0] < i +1 - startIdx:
                longest = [startIdx,i+1]
            seen[char] =i
        
        return longest[1] - longest[0]
