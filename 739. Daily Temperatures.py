Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100


Success
Details 
Runtime: 1248 ms, faster than 84.79% of Python3 online submissions for Daily Temperatures.
Memory Usage: 25.1 MB, less than 50.89% of Python3 online submissions for Daily Temperatures.


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack,res = [], [0] * len(temperatures)
        
        for idx,temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                t,index = stack.pop()
                res[index] = idx - index
            stack.append([temp,idx])
        return res
                
