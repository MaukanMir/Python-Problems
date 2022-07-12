# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

# The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

 

# Example 1:


# Input: graph = [[1,2],[3],[3],[]]
# Output: [[0,1,3],[0,2,3]]
# Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
# Example 2:


# Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
# Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]


# Success
# Details 
# Runtime: 175 ms, faster than 7.11% of Python3 online submissions for All Paths From Source to Target.
# Memory Usage: 15.4 MB, less than 92.23% of Python3 online submissions for All Paths From Source to Target.


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        target = len(graph)-1
        directions =[]
        
        def backtrack(currNode,path):
            if currNode == target:
                directions.append(list(path))
                return
            
            for nextNode in graph[currNode]:
                path.append(nextNode)
                backtrack(nextNode,path)
                
                path.pop()
        path = deque([0])
        backtrack(0,path)
        return directions

 class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        q,res = deque(), []
        q.append([0])
        
        while q:
            
            top = q.popleft()
            if top[-1] == len(graph)-1:
                res.append(top)
                continue
            
            for node in graph[top[-1]]:
                q.append(top + [node])
        
        return res
 
