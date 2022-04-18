Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.

 

Example 1:

Input: nums = [1,2,0]
Output: 3
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
 

Constraints:

1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1


Success
Details 
Runtime: 825 ms, faster than 97.31% of Python3 online submissions for First Missing Positive.
Memory Usage: 69.8 MB, less than 13.63% of Python3 online submissions for First Missing Positive.




class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        smallest = 1
        nums = list(set(nums))
        nums.sort()
        for i in nums:
            if i== 0 or i <0:
                continue
            if i!= smallest:
                return smallest
            elif i == smallest:
                smallest+=1
        return smallest
