# 283. Move Zeroes
# Easy

# 7088

# 197

# Add to List

# Share
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]
 

# Constraints:

# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1

Runtime: 160 ms, faster than 72.26% of Python3 online submissions for Move Zeroes.
Memory Usage: 15.3 MB, less than 89.80% of Python3 online submissions for Move Zeroes.

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        
        for i in range(len(nums)):
            if nums[i]!= 0:
                nums[index] = nums[i]
                index+=1
        
        for i in range(index,len(nums)):
            nums[i] =0
