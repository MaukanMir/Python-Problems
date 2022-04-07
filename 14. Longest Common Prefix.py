Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
Accepted
1,515,648
Submissions
3,860,677

Success
Details 
Runtime: 43 ms, faster than 67.95% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 13.8 MB, less than 90.80% of Python3 online submissions for Longest Common Prefix.


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        res = []
        
        for letter in zip(*strs):
            if len(set(letter)) ==1:
                res.append(letter[0])
            else:
                break
        return "".join(res)
        
