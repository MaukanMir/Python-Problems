# A binary tree is uni-valued if every node in the tree has the same value.

# Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.

 

# Example 1:


# Input: root = [1,1,1,1,1,null,1]
# Output: true
# Example 2:


# Input: root = [2,2,2,5,2]
# Output: false

Success
Details 
Runtime: 32 ms, faster than 71.45% of Python3 online submissions for Univalued Binary Tree.
Memory Usage: 14.1 MB, less than 77.75% of Python3 online submissions for Univalued Binary Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        
        if not root: return True
        
        stack,previous = [root], None
    
        while stack:
            node = stack.pop()
            
            if node and previous is None:
                previous = node.val
            if node and previous is not None:
                if node.val != previous:
                    return False
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return True
