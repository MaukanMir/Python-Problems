You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]


Success
Details 
Runtime: 2408 ms, faster than 46.00% of Python3 online submissions for Sliding Window Maximum.
Memory Usage: 30.5 MB, less than 41.06% of Python3 online submissions for Sliding Window Maximum.

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        left, right =0,0
        queue, output = deque(), []
        
        while right < len(nums):
            while queue and nums[queue[-1]] < nums[right]:
                queue.pop()
            queue.append(right)
            
            
            if left > queue[0]:
                queue.popleft()
            
            if (right+1) >=k:
                output.append(nums[queue[0]])
                left+=1
            
            right +=1
        
        return output
