Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30

Success
Details 
Runtime: 92 ms, faster than 55.31% of Python3 online submissions for Combination Sum II.
Memory Usage: 14.1 MB, less than 94.69% of Python3 online submissions for Combination Sum II.


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        values = []
        
        def backtrack(current, pos, target):
            if target ==0:
                values.append(current[:])
            if target <0:
                return 
            prev = None
            for i in range(pos,len(candidates)):
                if candidates[i] == prev:
                    continue
                current.append(candidates[i])
                backtrack(current, i+1, target - candidates[i])
                current.pop()
                prev = candidates[i]
        
        backtrack([], 0, target)
        
        return values
