# Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

# You may return the answer in any order.

 

# Example 1:

# Input: n = 4, k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
# Example 2:

# Input: n = 1, k = 1
# Output: [[1]]


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def backtrack(start,comb):
            if len(comb) == k:
                res.append(comb[:])
                return
            
            for i in range(start, n+1):
                comb.append(i)
                backtrack(i+1, comb)
                comb.pop()
        backtrack(1,[])
        return res

Success
Details 
Runtime: 476 ms, faster than 53.00% of Python3 online submissions for Combinations.
Memory Usage: 15.6 MB, less than 93.21% of Python3 online submissions for Combinations.
