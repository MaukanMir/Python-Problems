Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

 

Example 1:

Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Example 2:

Input: s = "abcd", k = 2
Output: "bacd"

Success
Details 
Runtime: 38 ms, faster than 64.84% of Python3 online submissions for Reverse String II.
Memory Usage: 13.9 MB, less than 97.81% of Python3 online submissions for Reverse String II.

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans = list(s)
        
        for i in range(0,len(s), 2*k):
            ans[i:i+k] = reversed(ans[i:i+k])
        return "".join(ans)
