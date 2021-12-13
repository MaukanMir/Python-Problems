# Given an array nums of integers, return how many of them contain an even number of digits.

 

# Example 1:

# Input: nums = [12,345,2,6,7896]
# Output: 2
# Explanation: 
# 12 contains 2 digits (even number of digits). 
# 345 contains 3 digits (odd number of digits). 
# 2 contains 1 digit (odd number of digits). 
# 6 contains 1 digit (odd number of digits). 
# 7896 contains 4 digits (even number of digits). 
# Therefore only 12 and 7896 contain an even number of digits.
# Example 2:

# Input: nums = [555,901,482,1771]
# Output: 1 
# Explanation: 
# Only 1771 contains an even number of digits.

Success
Details 
Runtime: 48 ms, faster than 92.39% of Python3 online submissions for Find Numbers with Even Number of Digits.
Memory Usage: 14.5 MB, less than 11.67% of Python3 online submissions for Find Numbers with Even Number of Digits.


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return len([n for n in nums if len(str(n)) %2 ==0])
