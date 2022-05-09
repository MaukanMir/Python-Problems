# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as:

# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: true
# Example 2:


# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
# Example 3:

# Input: root = []
# Output: true

# Success
# Details 
# Runtime: 44 ms, faster than 95.45% of Python3 online submissions for Balanced Binary Tree.
# Memory Usage: 19.4 MB, less than 16.54% of Python3 online submissions for Balanced Binary Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balance = True
        def dfs(root):
            if not root:
                return 0
            if not self.balance:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if abs(left - right) >1:
                self.balance = False
            
            return 1 + max(left,right)
        
        dfs(root)
        return self.balance

       
       
       # Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as:

# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: true
# Example 2:


# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
# Example 3:

# Input: root = []
# Output: true

# Success
# Details 
# Runtime: 44 ms, faster than 95.45% of Python3 online submissions for Balanced Binary Tree.
# Memory Usage: 19.4 MB, less than 16.54% of Python3 online submissions for Balanced Binary Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
Success
Details 
Runtime: 53 ms, faster than 86.03% of Python3 online submissions for Balanced Binary Tree.
Memory Usage: 18.8 MB, less than 29.54% of Python3 online submissions for Balanced Binary Tree.


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balance = True
        def dfs(root):
            if not root:
                return 0
            if not self.balance:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if abs(left - right) >1:
                self.balance = False
            
            return 1 + max(left,right)
        
        dfs(root)
        return self.balance
