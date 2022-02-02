Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        
        maxAmount, windowStart, check = float('-inf'), 0, {}
        
        for windowEnd in range(len(nums)):
            if nums[windowEnd] not in check:
                check[nums[windowEnd]] =0
            
            check[nums[windowEnd]] +=1
            
            while 0 in check and check[0] >1:
                check[nums[windowStart]] -=1
                windowStart +=1
            
            maxAmount = max(maxAmount, windowEnd- windowStart)
        return maxAmount
