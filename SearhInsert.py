
# 35. Search Insert Position
# Easy

# 5278

# 330

# Add to List

# Share
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4
# Example 4:

# Input: nums = [1,3,5,6], target = 0
# Output: 0
# Example 5:

# Input: nums = [1], target = 0
# Output: 0
 

# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums contains distinct values sorted in ascending order.
# -104 <= target <= 104




Success
Details 
Runtime: 48 ms, faster than 80.31% of Python3 online submissions for Search Insert Position.
Memory Usage: 15.2 MB, less than 23.85% of Python3 online submissions for Search Insert Position.
  
  
  
  class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums)-1
        
        
        while left <= right:
            pivot = (left+right)//2
            if nums[pivot] > target:
                right -=1
            elif nums[pivot] < target:
                left +=1
            
            elif nums[pivot] == target:return pivot
        return left
