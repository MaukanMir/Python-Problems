# Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

 

# Example 1:

# Input: nums = [3,2,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2.
# The third distinct maximum is 1.
# Example 2:

# Input: nums = [1,2]
# Output: 2
# Explanation:
# The first distinct maximum is 2.
# The second distinct maximum is 1.
# The third distinct maximum does not exist, so the maximum (2) is returned instead.
# Example 3:

# Input: nums = [2,2,3,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2 (both 2's are counted together since they have the same value).
# The third distinct maximum is 1.
 

# Constraints:

# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1

Success
Details 
Runtime: 48 ms, faster than 90.18% of Python3 online submissions for Third Maximum Number.
Memory Usage: 15.5 MB, less than 38.23% of Python3 online submissions for Third Maximum Number.

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        check = set(nums)
        
        maximum = max(check)
        
        if len(check) <3:
            return maximum
        
        check.remove(maximum)
        maximum = max(check)
        check.remove(maximum)
        return max(check)
