Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104

Success
Details 
Runtime: 46 ms, faster than 93.68% of Python3 online submissions for Search Insert Position.
Memory Usage: 14.7 MB, less than 69.37% of Python3 online submissions for Search Insert Position.

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        
        while left<= right:
            mid = left + (right-left)//2
            if nums[mid] == target:return mid
            elif nums[left] < target: left +=1
            elif nums[right] > target: right-=1
        
        return left
