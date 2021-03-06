Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

 

Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
Example 2:

Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.


Success
Details 
Runtime: 157 ms, faster than 74.38% of Python3 online submissions for Missing Number.
Memory Usage: 15.7 MB, less than 7.55% of Python3 online submissions for Missing Number.


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_set =set(nums)
    
        for i in num_set:
            if i ==1 and i-1 not in num_set:
                return i-1
            if i +1 not in num_set:
                return i+1
