
# Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

# Example 1:

# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
# Example 2:

# Input: nums = [1,0,1,1,0,1]
# Output: 2

# Success
# Details 
# Runtime: 328 ms, faster than 98.97% of Python3 online submissions for Max Consecutive Ones.
# Memory Usage: 14.4 MB, less than 76.92% of Python3 online submissions for Max Consecutive Ones.


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        
        max_value =0
        curr =0
        
        for i in nums:
            if i ==1:
                curr +=1
            elif i !=1:
                max_value = max(curr,max_value)
                curr =0
        
        return max(curr,max_value)
