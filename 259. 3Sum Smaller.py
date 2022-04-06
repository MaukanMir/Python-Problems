Given an array of n integers nums and an integer target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

 

Example 1:

Input: nums = [-2,0,1,3], target = 2
Output: 2
Explanation: Because there are two triplets which sums are less than 2:
[-2,0,1]
[-2,0,3]
Example 2:

Input: nums = [], target = 0
Output: 0
Example 3:

Input: nums = [0], target = 0
Output: 0


Success
Details 
Runtime: 708 ms, faster than 88.23% of Python3 online submissions for 3Sum Smaller.
Memory Usage: 14 MB, less than 16.17% of Python3 online submissions for 3Sum Smaller.
  
  
  class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        if len(set(nums)) ==1 and nums[0] ==0:return 0
        
        nums.sort()
        result =0
    
        for i in range(len(nums)-2):
            result += self.twoSum(nums,target - nums[i], i+1)
            
        return result
            
    def twoSum(self, nums, target, start): 
        result, left, right =0, start, len(nums)-1
        while left < right:
            if nums[left] + nums[right] < target:
                result += right -left
                left+=1
            else:
                right -=1
        return result
