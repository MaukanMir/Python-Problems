You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.

 

Example 1:


Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2
Example 2:


Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1

Success
Details 
Runtime: 104 ms, faster than 73.24% of Python3 online submissions for Number of Connected Components in an Undirected Graph.
Memory Usage: 17.1 MB, less than 25.42% of Python3 online submissions for Number of Connected Components in an Undirected Graph.


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        count =0
        graph = [[] for _ in range(n)]
        seen = [False for _ in range(n)]
        
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
        def dfs(node):
            for neigh in graph[node]:
                if not seen[neigh]:
                    seen[neigh] = True
                    dfs(neigh)
        
        for j in range(n):
            if not seen[j]:
                count+=1
                seen[j] = True
                dfs(j)
        
        return count
