Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109



Success
Details 
Runtime: 475 ms, faster than 83.40% of Python3 online submissions for Contains Duplicate.
Memory Usage: 25.9 MB, less than 72.99% of Python3 online submissions for Contains Duplicate.


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        keys = {}
        for i in range(len(nums)):
            keys[nums[i]] = keys.get(nums[i],0) +1
            if keys[nums[i]] ==2:
                return True
        return False

       
Success
Details 
Runtime: 457 ms, faster than 91.42% of Python3 online submissions for Contains Duplicate.
Memory Usage: 26 MB, less than 31.63% of Python3 online submissions for Contains Duplicate.
 
 class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return True if len(nums) != len(set(nums)) else False
