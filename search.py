# 704. Binary Search
# Easy

# 2528

# 79

# Add to List

# Share
# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Example 2:

# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1


# Success
# Details 
# Runtime: 224 ms, faster than 97.89% of Python3 online submissions for Binary Search.
# Memory Usage: 15.4 MB, less than 99.25% of Python3 online submissions for Binary Search.

  
  
  class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums)-1
        
        while left<=right:
            pivot = (left + right) //2
            
            if nums[pivot] == target: return pivot
            elif nums[pivot]  < target: left = pivot +1
            elif nums[pivot]  > target: right = pivot -1
        return -1
        
