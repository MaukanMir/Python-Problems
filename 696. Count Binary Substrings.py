
Give a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

 

Example 1:

Input: s = "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
Notice that some of these substrings repeat and are counted the number of times they occur.
Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
Example 2:

Input: s = "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
 

Constraints:

1 <= s.length <= 105
s[i] is either '0' or '1'.


Success
Details 
Runtime: 216 ms, faster than 58.92% of Python3 online submissions for Count Binary Substrings.
Memory Usage: 14.5 MB, less than 89.73% of Python3 online submissions for Count Binary Substrings.

  
  class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        
        ans, prev, cur = 0,0,1
        
        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                ans += min(prev,cur)
                prev, cur = cur,1
            else:
                cur +=1
        return ans + min(prev, cur)

