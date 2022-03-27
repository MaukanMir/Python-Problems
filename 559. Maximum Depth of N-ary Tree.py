# Given a n-ary tree, find its maximum depth.

# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

 

# Example 1:



# Input: root = [1,null,3,2,4,null,5,6]
# Output: 3
# Example 2:



# Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# Output: 5



Success
Details 
Runtime: 77 ms, faster than 14.84% of Python3 online submissions for Maximum Depth of N-ary Tree.
Memory Usage: 16 MB, less than 80.71% of Python3 online submissions for Maximum Depth of N-ary Tree.


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        stack = []
        stack.append((1,root))
        distance = 0
        
        while stack:
            current,node = stack.pop()
            
            
            if node:
                distance = max(current,distance)
                for c in node.children:
                    stack.append((current+1, c))
        return distance
       
Success
Details 
Runtime: 49 ms, faster than 79.80% of Python3 online submissions for Maximum Depth of N-ary Tree.
Memory Usage: 16.1 MB, less than 54.38% of Python3 online submissions for Maximum Depth of N-ary Tree.
 
 
 """
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:return 0
        
        stack, maxV = [[root,0]], float('-inf')
        
        while stack:
            node, dist = stack.pop()
            
            maxV = max(maxV,dist+1)
            if node:
                for child in node.children:
                    stack.append([child,dist+1])
        return maxV

