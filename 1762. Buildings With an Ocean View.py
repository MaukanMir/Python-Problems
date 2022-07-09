There are n buildings in a line. You are given an integer array heights of size n that represents the heights of the buildings in the line.

The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without obstructions. Formally, a building has an ocean view if all the buildings to its right have a smaller height.

Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.

 

Example 1:

Input: heights = [4,2,3,1]
Output: [0,2,3]
Explanation: Building 1 (0-indexed) does not have an ocean view because building 2 is taller.
Example 2:

Input: heights = [4,3,2,1]
Output: [0,1,2,3]
Explanation: All the buildings have an ocean view.
Example 3:

Input: heights = [1,3,2,4]
Output: [3]
Explanation: Only building 3 has an ocean view.
 

Constraints:

1 <= heights.length <= 105
1 <= heights[i] <= 109


Success
Details 
Runtime: 951 ms, faster than 61.04% of Python3 online submissions for Buildings With an Ocean View.
Memory Usage: 31.6 MB, less than 16.31% of Python3 online submissions for Buildings With an Ocean View.



class Solution:
    def findBuildings(self, buildings: List[int]) -> List[int]:
        
        
        res = []
        maxBuilding = 0
        for i in range(len(buildings)-1,-1,-1):
            buildingHeight = buildings[i]
            
            if buildingHeight > maxBuilding:
                res.append(i)
            
            maxBuilding = max(buildingHeight, maxBuilding)
        
        return res[::-1]
       
 
Success
Details 
Runtime: 765 ms, faster than 87.18% of Python3 online submissions for Buildings With an Ocean View.
Memory Usage: 31.5 MB, less than 71.97% of Python3 online submissions for Buildings With an Ocean View.

 class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        
        res,maxHeight = [], 0
        
        for i in range(len(heights)-1,-1,-1):
            buildingHeight = heights[i]
            
            if buildingHeight > maxHeight:
                res.append(i)
                maxHeight = buildingHeight
        
        return res[::-1]
