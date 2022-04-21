# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.


# Success
# Details 
# Runtime: 108 ms, faster than 83.58% of Python3 online submissions for Longest Repeating Character Replacement.
# Memory Usage: 14.3 MB, less than 80.56% of Python3 online submissions for Longest Repeating Character Replacement.

  
  
  class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        
        res =0
        leftPointer =0
        maxCount =0
        
        for rightPointer in range(len(s)):
            count[s[rightPointer]] = 1 + count.get(s[rightPointer],0)
            maxCount = max(count[s[rightPointer]],maxCount)
            
            while(rightPointer - leftPointer +1) - maxCount > k:
                count[s[leftPointer]] -=1
                leftPointer +=1
            
            res = max(res,rightPointer -leftPointer +1)
        return res

       
# Success
# Details 
# Runtime: 140 ms, faster than 76.32% of Python3 online submissions for Longest Repeating Character Replacement.
# Memory Usage: 13.9 MB, less than 94.18% of Python3 online submissions for Longest Repeating Character Replacement.       
class Solution:
def characterReplacement(self, s: str, k: int) -> int:
        
        count,res, left, maxValue ={}, 0,0,0
        
        for right in range(len(s)):
            count[s[right]] = count.get(s[right],0) +1
            maxValue = max(maxValue,count[s[right]])
            
            if (right - left +1) - maxValue >k:
                count[s[left]] -=1
                left+=1
            
            res = max(res, (right-left+1))
        return res
