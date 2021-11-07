# 145. Binary Tree Postorder Traversal
# Easy

# 3311

# 128

# Add to List

# Share
# Given the root of a binary tree, return the postorder traversal of its nodes' values.

 

# Example 1:


# Input: root = [1,null,2,3]
# Output: [3,2,1]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [1]
# Output: [1]
# Example 4:


# Input: root = [1,2]
# Output: [2,1]
# Example 5:


# Input: root = [1,null,2]
# Output: [2,1]
 

# Constraints:

# The number of the nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100




Success
Details 
Runtime: 28 ms, faster than 88.36% of Python3 online submissions for Binary Tree Postorder Traversal.
Memory Usage: 14.1 MB, less than 76.57% of Python3 online submissions for Binary Tree Postorder Traversal.
  
  
  
  # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.array = []
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if root:
            Solution.postorderTraversal(self,root.left)
            Solution.postorderTraversal(self,root.right)
            self.array.append(root.val)
            
            return self.array
        return 
        
