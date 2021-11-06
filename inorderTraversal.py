# 94. Binary Tree Inorder Traversal
# Easy

# 6076

# 258

# Add to List

# Share
# Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

# Example 1:


# Input: root = [1,null,2,3]
# Output: [1,3,2]
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
# Output: [1,2]
 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100




Success
Details 
Runtime: 28 ms, faster than 88.28% of Python3 online submissions for Binary Tree Inorder Traversal.
Memory Usage: 14.2 MB, less than 75.67% of Python3 online submissions for Binary Tree Inorder Traversal.






# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.array=[]
        
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is not None: 
        
            Solution.inorderTraversal(self,root.left)
            self.array.append(root.val)
            Solution.inorderTraversal(self,root.right)
            return self.array
        else:
            return 
        
        return self.array
