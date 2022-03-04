# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# Example 2:

# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
 

# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.

Success
Details 
Runtime: 300 ms, faster than 59.46% of Python3 online submissions for Squares of a Sorted Array.
Memory Usage: 16.3 MB, less than 16.64% of Python3 online submissions for Squares of a Sorted Array.

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        left,right = 0, len(nums)-1
        result = [0] * len(nums)
        
        for i in range(right,-1,-1):
            if abs(nums[right]) > abs(nums[left]):
                square,right = nums[right], right-1
            else:
                square = nums[left]
                left +=1
            
            result[i] = square**2
        return result
