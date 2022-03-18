
Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in any order.

 

Example 1:

Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
Example 2:

Input: s = "3z4"
Output: ["3z4","3Z4"]
 

Constraints:

1 <= s.length <= 12
s consists of lowercase English letters, uppercase English letters, and digits.


Success
Details 
Runtime: 66 ms, faster than 75.80% of Python3 online submissions for Letter Case Permutation.
Memory Usage: 15.7 MB, less than 8.37% of Python3 online submissions for Letter Case Permutation.


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        ans = [[]]
        
        for letter in s:
            size = len(ans)
            if letter.isalpha():
                for i in range(size):
                    ans.append(ans[i][:])
                    ans[i].append(letter.lower())
                    ans[size+i].append(letter.upper())
            else:
                    for i in range(size):
                        ans[i].append(letter)
                        
        return map("".join, ans)
        
