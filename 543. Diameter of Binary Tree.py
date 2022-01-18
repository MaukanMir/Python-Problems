# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

 

# Example 1:


# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
# Example 2:

# Input: root = [1,2]
# Output: 1
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -100 <= Node.val <= 100

# Success
# Details 
# Runtime: 36 ms, faster than 97.72% of Python3 online submissions for Diameter of Binary Tree.
# Memory Usage: 16.5 MB, less than 26.87% of Python3 online submissions for Diameter of Binary Tree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        width =0
        
        def DFS(node):
            if not node:
                return 0
            nonlocal width
            
            leftPath = DFS(node.left)
            rightPath = DFS(node.right)
            
            width = max(width, leftPath+rightPath)
            
            return max(leftPath, rightPath)+1
        
        DFS(root)
        return width
