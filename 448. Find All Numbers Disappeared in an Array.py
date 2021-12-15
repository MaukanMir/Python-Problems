

  
  
#   Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
# Example 2:

# Input: nums = [1,1]
# Output: [2]
 

# Constraints:

# n == nums.length
# 1 <= n <= 105
# 1 <= nums[i] <= n


# Success
# Details 
# Runtime: 363 ms, faster than 51.41% of Python3 online submissions for Find All Numbers Disappeared in an Array.
# Memory Usage: 23.4 MB, less than 45.92% of Python3 online submissions for Find All Numbers Disappeared in an Array.

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        keys = {}
        
        for i in nums:
            keys[i] =1
        
        seen = []
        for i in range(1, len(nums)+1):
            if i not in keys: seen.append(i)
        
        return seen
      
      
      
#  Success
# Details 
# Runtime: 348 ms, faster than 64.21% of Python3 online submissions for Find All Numbers Disappeared in an Array.
# Memory Usage: 23.2 MB, less than 46.86% of Python3 online submissions for Find All Numbers Disappeared in an Array.
  
  
  class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        keys = Counter(nums)
        
        seen = []
        for i in range(1, len(nums)+1):
            if i not in keys: seen.append(i)
        
        return seen
  
  

