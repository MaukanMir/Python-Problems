Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105

Success
Details 
Runtime: 138 ms, faster than 52.23% of Python3 online submissions for Trapping Rain Water.
Memory Usage: 15.7 MB, less than 62.11% of Python3 online submissions for Trapping Rain Water.


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        left, right, maxValue = 0, len(height)-1, 0
        leftMax,rightMax = height[left], height[right]
        
        while left < right:
            
            if leftMax < rightMax:
                left+=1
                leftMax = max(leftMax,height[left])
                maxValue += leftMax - height[left]
            else:
                right -=1
                rightMax = max(rightMax,height[right])
                maxValue += rightMax - height[right]
            
        return maxValue
