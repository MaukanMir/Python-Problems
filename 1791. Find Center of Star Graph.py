There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.

You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph.

 

Example 1:


Input: edges = [[1,2],[2,3],[4,2]]
Output: 2
Explanation: As shown in the figure above, node 2 is connected to every other node, so 2 is the center.
Example 2:

Input: edges = [[1,2],[5,1],[1,3],[1,4]]
Output: 1

Success
Details 
Runtime: 856 ms, faster than 71.86% of Python3 online submissions for Find Center of Star Graph.
Memory Usage: 49.8 MB, less than 88.36% of Python3 online submissions for Find Center of Star Graph.

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        counter ={}
        
        for x,y in edges:
            
            if x not in counter: counter[x] =1
            elif x in counter: counter[x] +=1
            if y not in counter:counter[y] =1
            elif y in counter: counter[y] +=1
        
        
        return max(counter, key=counter.get)
       
  Success
Details 
Runtime: 1191 ms, faster than 40.60% of Python3 online submissions for Find Center of Star Graph.
Memory Usage: 50 MB, less than 83.18% of Python3 online submissions for Find Center of Star Graph.
 
 
 class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        
        one, two = edges[0][0], edges[0][1]
        
        if one in edges[1]:
            return one
        return two
