# Given the root of a binary tree and a leaf node, reroot the tree so that the leaf is the new root.

# You can reroot the tree with the following steps for each node cur on the path starting from the leaf up to the root​​​ excluding the root:

# If cur has a left child, then that child becomes cur's right child.
# cur's original parent becomes cur's left child. Note that in this process the original parent's pointer to cur becomes null, making it have at most one child.
# Return the new root of the rerooted tree.

# Note: Ensure that your solution sets the Node.parent pointers correctly after rerooting or you will receive "Wrong Answer".

 

# Example 1:


# Input: root = [3,5,1,6,2,0,8,null,null,7,4], leaf = 7
# Output: [7,2,null,5,4,3,6,null,null,null,1,null,null,0,8]
# Example 2:

# Input: root = [3,5,1,6,2,0,8,null,null,7,4], leaf = 0
# Output: [0,1,null,3,8,5,null,null,null,6,2,null,null,7,4]
 

# Constraints:

# The number of nodes in the tree is in the range [2, 100].
# -109 <= Node.val <= 109
# All Node.val are unique.
# leaf exist in the tree.

# Success
# Details 
# Runtime: 50 ms, faster than 32.26% of Python3 online submissions for Change the Root of a Binary Tree.
# Memory Usage: 14.6 MB, less than 85.48% of Python3 online submissions for Change the Root of a Binary Tree.


"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def flipBinaryTree(self, root: 'Node', leaf: 'Node') -> 'Node':
        def dfs(node,parent):
            if not node:
                return
            elif node == root:
                node.parent = parent; return
            if node.left:
                node.right = node.left
            if node.parent.left == node:
                node.parent.left = None
            else:
                node.parent.right = None
            node.left, node.parent = node.parent,parent
            dfs(node.left, node)
        dfs(leaf,None)
        return leaf
