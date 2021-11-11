# 98. Validate Binary Search Tree
# Medium

# 7826

# 780

# Add to List

# Share
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
 

# Example 1:


# Input: root = [2,1,3]
# Output: true
# Example 2:


# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.

Success
Details 
Runtime: 40 ms, faster than 91.64% of Python3 online submissions for Validate Binary Search Tree.
Memory Usage: 16.4 MB, less than 53.85% of Python3 online submissions for Validate Binary Search Tree.
  
  
  
  
  # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self,root:TreeNode):
        if not root:
            return True
        stack = [(root,-math.inf,math.inf)]
        while stack:
            root,lower,upper = stack.pop()
            if not root:
                continue
            
            val = root.val
            
            if val <= lower or val >= upper:
                return False
            stack.append((root.right,val,upper))
            stack.append((root.left,lower,val))
        return True
       
 Success
Details 
Runtime: 40 ms, faster than 91.64% of Python3 online submissions for Validate Binary Search Tree.
Memory Usage: 16.4 MB, less than 80.73% of Python3 online submissions for Validate Binary Search Tree.
 
 
 
 
 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def validate(node,low = -math.inf, high= math.inf):
            if not node:
                return True
            
            if node.val <= low or node.val >= high:return False
            
            return validate(node.right,node.val,high) and validate(node.left,low,node.val)
        
        return validate(root)

