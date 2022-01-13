Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.

Success
Details 
Runtime: 32 ms, faster than 85.10% of Python3 online submissions for Subsets.
Memory Usage: 14.5 MB, less than 52.49% of Python3 online submissions for Subsets.


class Solution:
    def subsets(self, nums: List[int], idx = None) -> List[List[int]]:
        
        if idx == None:
            idx = len(nums)-1
        if idx <0:return [[]]
        
        got = nums[idx]
        
        powersets = self.subsets(nums,idx-1)
        
        for i in range(len(powersets)):
            currentSub = powersets[i]
            powersets.append(currentSub + [got])
        
        return powersets
        
