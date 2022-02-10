You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

 

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.

Success
Details 
Runtime: 109 ms, faster than 15.50% of Python3 online submissions for Min Cost Climbing Stairs.
Memory Usage: 14 MB, less than 96.09% of Python3 online submissions for Min Cost Climbing Stairs.


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one,two = 0,0
        
        for i in range(2, len(cost)+1):
            store = one
            one = min(one + cost[i-1], two + cost[i-2])
            two = store
        return one
