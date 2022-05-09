# 226. Invert Binary Tree
# Easy

# 6838

# 96

# Add to List

# Share
# Given the root of a binary tree, invert the tree, and return its root.

 

# Example 1:


# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
# Example 2:


# Input: root = [2,1,3]
# Output: [2,3,1]
# Example 3:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100


Success
Details 
Runtime: 16 ms, faster than 99.95% of Python3 online submissions for Invert Binary Tree.
Memory Usage: 14.1 MB, less than 76.07% of Python3 online submissions for Invert Binary Tree.

  
  
  
  # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root is not None:
            root.left,root.right = root.right,root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
            return root
        
        return root
       
       
 Success
Details 
Runtime: 32 ms, faster than 73.07% of Python3 online submissions for Invert Binary Tree.
Memory Usage: 14.1 MB, less than 92.14% of Python3 online submissions for Invert Binary Tree.
 
 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        queue = [root]
        while queue != []:
            current_node = queue.pop()
            if current_node is not None:
                self.swap(current_node)
                queue.append(current_node.left)
                queue.append(current_node.right)
            
        return root
        
    
    def swap(self,root):
         root.left, root.right = root.right,root.left

      
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return None
        
        left, right = self.invertTree(root.left), self.invertTree(root.right)
        
        root.left = right
        root.right = left
        
        return root
