        Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.

 

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: The substring is "aa" with length 2.
 

Constraints:

1 <= s.length <= 5 * 104
0 <= k <= 50

Success
Details 
Runtime: 197 ms, faster than 6.91% of Python3 online submissions for Longest Substring with At Most K Distinct Characters.
Memory Usage: 14.1 MB, less than 93.73% of Python3 online submissions for Longest Substring with At Most K Distinct Characters.


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
        left,right, maxAmount,counter = 0,0,0,Counter()
        
        while right < len(s):
            counter[s[right]] +=1
            right+=1
            
            while len(counter)>k:
                counter[s[left]] -=1
                if not counter[s[left]]:
                    del counter[s[left]]
                left +=1
            maxAmount = max(maxAmount, right-left)
        return maxAmount
        
        
        
