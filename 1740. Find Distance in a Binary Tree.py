# Given the root of a binary tree and two integers p and q, return the distance between the nodes of value p and value q in the tree.

# The distance between two nodes is the number of edges on the path from one to the other.

 

# Example 1:


# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 0
# Output: 3
# Explanation: There are 3 edges between 5 and 0: 5-3-1-0.
# Example 2:


# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 7
# Output: 2
# Explanation: There are 2 edges between 5 and 7: 5-2-7.
# Example 3:


# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 5
# Output: 0
# Explanation: The distance between a node and itself is 0.

# Success
# Details 
# Runtime: 112 ms, faster than 54.58% of Python3 online submissions for Find Distance in a Binary Tree.
# Memory Usage: 31.2 MB, less than 7.89% of Python3 online submissions for Find Distance in a Binary Tree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        
        if not root:
            return 1
        
        nodeMap ={}
        
        def preOrder(node,parent):
            if not node:
                return 
            nodeMap[node.val] = node
            node.parent = parent
            preOrder(node.left, node)
            preOrder(node.right, node)
        preOrder(root,None)
        
        
        
        queue = deque( [(nodeMap[p], 0)])
        
        visited = set()
        
        while queue:
            node,level = queue.popleft()
            if node in visited:
                continue
            visited.add(node)
            
            if node == nodeMap[q]:
                return level
            
            directions = [node.left,node.right, node.parent]
            for direct in directions:
                if direct and direct not in visited:
                    queue.append((direct,level+1))
