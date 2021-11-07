# 144. Binary Tree Preorder Traversal
# Easy

# 3121

# 106

# Add to List

# Share
# Given the root of a binary tree, return the preorder traversal of its nodes' values.

 

# Example 1:


# Input: root = [1,null,2,3]
# Output: [1,2,3]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [1]
# Output: [1]
# Example 4:


# Input: root = [1,2]
# Output: [1,2]
# Example 5:


# Input: root = [1,null,2]
# Output: [1,2]
 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

Success
Details 
Runtime: 16 ms, faster than 99.91% of Python3 online submissions for Binary Tree Preorder Traversal.
Memory Usage: 14.3 MB, less than 46.10% of Python3 online submissions for Binary Tree Preorder Traversal.
  
  
  
  # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        node,output = root, []
        
        while node:
            if not node.left:
                output.append(node.val)
                node = node.right
            else:
                predecessor = node.left
                
                while predecessor.right and predecessor.right is not node:
                    predecessor = predecessor.right
                    
                if not predecessor.right:
                    output.append(node.val)
                    predecessor.right = node
                    node = node.left
                else:
                    predecessor.right = None
                    node = node.right
        return output
        
