
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.

Success
Details 
Runtime: 58 ms, faster than 57.80% of Python3 online submissions for Intersection of Two Arrays.
Memory Usage: 14.1 MB, less than 94.39% of Python3 online submissions for Intersection of Two Arrays.


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        return set(nums1).intersection(set(nums2))
