
Success
Details 
Runtime: 772 ms, faster than 87.16% of Python3 online submissions for Container With Most Water.
Memory Usage: 27.5 MB, less than 58.32% of Python3 online submissions for Container With Most Water.


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, maxArea = 0, len(height)-1, float('-inf')
        
        while left < right:
            maxArea = max(maxArea, min(height[left], height[right]) * (right-left))
            
            if height[left] < height[right]:
                left+=1
            else:
                right -=1
        return maxArea
      
      
      You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
