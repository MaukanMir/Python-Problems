# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.

 

# Example 1:

# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.
# Example 2:

# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
# Example 3:

# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 

  
# Success
# Details 
# Runtime: 52 ms, faster than 58.30% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
# Memory Usage: 14.1 MB, less than 66.03% of Python3 online submissions for Find Minimum in Rotated Sorted Array.




class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        res = float('inf')
        
        while left<= right:
            mid = (left +right)//2
            
            if nums[left] < nums[right]:
                res = min(res,nums[left])
                break
            res = min(res,nums[mid])
            if nums[mid] >= nums[left]:
                left = mid+1
            else:
                right = mid-1
        
        return res
