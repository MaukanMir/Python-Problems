Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
 

Constraints:

3 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-104 <= target <= 104


Success
Details 
Runtime: 412 ms, faster than 40.29% of Python3 online submissions for 3Sum Closest.
Memory Usage: 13.9 MB, less than 70.84% of Python3 online submissions for 3Sum Closest.


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        minValue = float('inf')
        nums.sort()
        for i in range(len(nums)-2):
            left, right = i +1, len(nums)-1
            
            while left < right:
                total = nums[left] + nums[right] + nums[i]
                if abs(target-total) < abs(minValue):
                    minValue = target - total
                if total < target:
                    left +=1
                else:
                    right -=1
 
        return target-minValue
