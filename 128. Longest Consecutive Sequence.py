Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109

Success
Details 
Runtime: 300 ms, faster than 59.67% of Python3 online submissions for Longest Consecutive Sequence.
Memory Usage: 27.6 MB, less than 55.08% of Python3 online submissions for Longest Consecutive Sequence.



class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num_set, max_value = set(nums), 0
        
        for num in num_set:
            if num-1 not in num_set:
                curr = num
                curr_streak =1
                
                while curr +1 in num_set:
                    curr+=1
                    curr_streak +=1
                max_value = max(max_value, curr_streak)
        return max_value
