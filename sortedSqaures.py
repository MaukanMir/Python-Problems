# 977. Squares of a Sorted Array
# Easy

# 3740

# 128

# Add to List

# Share
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# Example 2:

# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

Success
Details 
Runtime: 228 ms, faster than 72.68% of Python3 online submissions for Squares of a Sorted Array.
Memory Usage: 16.4 MB, less than 12.37% of Python3 online submissions for Squares of a Sorted Array.
  
  
  class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([n**2 for n in nums])

Runtime: 220 ms, faster than 83.83% of Python3 online submissions for Squares of a Sorted Array.
Memory Usage: 15.9 MB, less than 91.16% of Python3 online submissions for Squares of a Sorted Array.
 
 
 class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)):
            nums[i] = nums[i]**2
        
        return sorted(nums)
