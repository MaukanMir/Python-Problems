# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

# Example 1:

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
# Example 2:

# Input: nums = [5], k = 1
# Output: 5.00000

# Success
# Details 
# Runtime: 1472 ms, faster than 51.04% of Python3 online submissions for Maximum Average Subarray I.
# Memory Usage: 26.2 MB, less than 24.38% of Python3 online submissions for Maximum Average Subarray I.


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) ==1:
            return nums[0]/1
    
        left,right = 0,0
        total , maxValue, =0, float('-inf')
        
        while left < len(nums) and right <len(nums):
            total += nums[right]
            
            if right - left >=k:
                total -= nums[left]
                left +=1
            
            if right - left == k-1:

                maxValue = max( maxValue, total/ ((right-left) +1) )
            right +=1
        return maxValue
    
    
Success
Details 
Runtime: 1248 ms, faster than 76.30% of Python3 online submissions for Maximum Average Subarray I.
Memory Usage: 25.7 MB, less than 84.02% of Python3 online submissions for Maximum Average Subarray I.
 
 
 class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        runningSum = 0
        
        for i in range(k):
            runningSum += nums[i]
            
        maxSum = runningSum
        
        for i in range(k, len(nums) ):
            runningSum += nums[i] - nums[i-k]
            maxSum = max(maxSum, runningSum)
        return maxSum/k
        

        
