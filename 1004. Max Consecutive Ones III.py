Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

Success
Details 
Runtime: 994 ms, faster than 21.68% of Python3 online submissions for Max Consecutive Ones III.
Memory Usage: 14.6 MB, less than 89.11% of Python3 online submissions for Max Consecutive Ones III.



class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        windowStart, windowEnd, zeroCount, maxAmount = 0,0, 0, float('-inf')
        
        while windowEnd < len(nums):
            
            if nums[windowEnd] == 0:
                k-=1
            
            if k<0:
                if nums[windowStart] ==0: 
                    k+=1
                windowStart +=1
            
            windowEnd +=1

        return windowEnd - windowStart
