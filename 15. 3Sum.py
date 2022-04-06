Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
 

Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105

Success
Details 
Runtime: 904 ms, faster than 73.64% of Python3 online submissions for 3Sum.
Memory Usage: 18.2 MB, less than 44.73% of Python3 online submissions for 3Sum.


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] >0:
                break
            if i ==0 or nums[i-1] != nums[i]:
                self.twoSum(nums, i, result)
        return result
        
        
    def twoSum(self,nums,i, result):
        lo, hi = i+1, len(nums)-1
        
        while lo < hi:
            total = nums[lo] + nums[i] + nums[hi]
            
            if total <0:
                lo+=1
            elif total >0:
                hi-=1
            else:
                result.append([nums[i], nums[lo],nums[hi]])
                lo+=1
                hi-=1
                while lo < hi and nums[lo] == nums[lo-1]:
                    lo+=1
