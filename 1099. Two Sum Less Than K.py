Given an array nums of integers and integer k, return the maximum sum such that there exists i < j with nums[i] + nums[j] = sum and sum < k. If no i, j exist satisfying this equation, return -1.

 

Example 1:

Input: nums = [34,23,1,24,75,33,54,8], k = 60
Output: 58
Explanation: We can use 34 and 24 to sum 58 which is less than 60.
Example 2:

Input: nums = [10,20,30], k = 15
Output: -1
Explanation: In this case it is not possible to get a pair sum less that 15.




class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        
        maxValue, leftPointer, rightPointer = float('-inf'), 0, len(nums)-1
        nums.sort()
        
        while leftPointer < rightPointer:
            if nums[leftPointer] + nums[rightPointer] < k:
                maxValue = max(maxValue, nums[leftPointer] + nums[rightPointer])
                leftPointer +=1
                
            if nums[leftPointer] + nums[rightPointer] >= k:
                rightPointer -=1
                
            
        
                
        
        
        
        
        
        return -1 if maxValue == float('-inf') else maxValue

Success
Details 
Runtime: 52 ms, faster than 67.59% of Python3 online submissions for Two Sum Less Than K.
Memory Usage: 13.8 MB, less than 92.62% of Python3 online submissions for Two Sum Less Than K.
