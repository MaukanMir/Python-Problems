# 169. Majority Element
# Easy

# 6962

# 295

# Add to List

# Share
# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
 

# Success
# Details 
# Runtime: 163 ms, faster than 81.58% of Python3 online submissions for Majority Element.
# Memory Usage: 15.5 MB, less than 53.89% of Python3 online submissions for Majority Element.

  
  
  
  
  class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = collections.Counter(nums)
        return max(dict,key = dict.get)
      
      
Success
Details 
Runtime: 148 ms, faster than 99.62% of Python3 online submissions for Majority Element.
Memory Usage: 15.6 MB, less than 11.98% of Python3 online submissions for Majority Element.

      
      

      class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
