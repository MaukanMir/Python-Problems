
You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.

 

Example 1:


Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true
Example 2:


Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false

Success
Details 
Runtime: 183 ms, faster than 13.49% of Python3 online submissions for Graph Valid Tree.
Memory Usage: 17.7 MB, less than 6.99% of Python3 online submissions for Graph Valid Tree.
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        
        adj = {i:[] for i in range(n)}
        
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visited = set()
        def dfs(i,prev):
            if i in visited:
                return False
            
            visited.add(i)
            
            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
            
            return True
        
        return dfs(0,-1) and n == len(visited)
