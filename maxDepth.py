# 104. Maximum Depth of Binary Tree
# Easy

# 5140

# 109

# Add to List

# Share
# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: 3
# Example 2:

# Input: root = [1,null,2]
# Output: 2
# Example 3:

# Input: root = []
# Output: 0
# Example 4:

# Input: root = [0]
# Output: 1
 

# Constraints:

# The number of nodes in the tree is in the range [0, 104].
# -100 <= Node.val <= 100


Success
Details 
Runtime: 36 ms, faster than 93.78% of Python3 online submissions for Maximum Depth of Binary Tree.
Memory Usage: 16 MB, less than 60.47% of Python3 online submissions for Maximum Depth of Binary Tree.
  
  
  # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return  max(self.maxDepth(root.left)+1, self.maxDepth(root.right)+1)
