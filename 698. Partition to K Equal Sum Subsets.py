# Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.

 

# Example 1:

# Input: nums = [4,3,2,3,5,2,1], k = 4
# Output: true
# Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
# Example 2:

# Input: nums = [1,2,3,4], k = 3
# Output: false
 

# Constraints:

# 1 <= k <= nums.length <= 16
# 1 <= nums[i] <= 104
# The frequency of each element is in the range [1, 4].

# Success
# Details 
# Runtime: 36 ms, faster than 89.45% of Python3 online submissions for Partition to K Equal Sum Subsets.
# Memory Usage: 14.2 MB, less than 93.50% of Python3 online submissions for Partition to K Equal Sum Subsets.


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) %k:
            return False
        nums.sort(reverse = True)
        target = sum(nums)/k
        
        used = [False] * len(nums)
        
        def backtrack(i,k , subsetSum):
            if k== 0: return True
            
            if subsetSum == target:
                return backtrack(0,k-1,0)
            
            for j in range(i, len(nums)):
                if used[j] or subsetSum + nums[j] > target:
                    continue
                
                used[j] = True
                
                if backtrack(j+1, k, subsetSum + nums[j]):
                    return True
                used[j] = False
            return False
        
        return backtrack(0,k,0)
