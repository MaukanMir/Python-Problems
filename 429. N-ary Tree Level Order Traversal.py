Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

 

Example 1:



Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]
Example 2:



Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
 

Constraints:

The height of the n-ary tree is less than or equal to 1000
The total number of nodes is between [0, 104]

Success
Details 
Runtime: 81 ms, faster than 47.04% of Python3 online submissions for N-ary Tree Level Order Traversal.
Memory Usage: 16 MB, less than 51.23% of Python3 online submissions for N-ary Tree Level Order Traversal.



"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        levels, stack = {0:[root.val]}, deque([[root,1]])
        
        while stack:
            node,lvl = stack.popleft()
            if node:
                for child in node.children:
                    stack.append([child,lvl+1])
                    
                    if lvl not in levels:
                        levels[lvl] = [child.val]
                    else:
                        levels[lvl].append(child.val)
        return levels.values()
