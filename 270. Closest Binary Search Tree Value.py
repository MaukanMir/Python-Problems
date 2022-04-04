# Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target.

 

# Example 1:


# Input: root = [4,2,5,1,3], target = 3.714286
# Output: 4
# Example 2:

# Input: root = [1], target = 4.428571
# Output: 1
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# 0 <= Node.val <= 109
# -109 <= target <= 109

# Success
# Details 
# Runtime: 60 ms, faster than 24.75% of Python3 online submissions for Closest Binary Search Tree Value.
# Memory Usage: 16 MB, less than 97.94% of Python3 online submissions for Closest Binary Search Tree Value.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        
        if not root:
            return 0
        
        stack = [root]
        target = round(target)
        minValue = 10000
        key = None
        while stack:
            node = stack.pop()
            
            if node:
                if node.val == target:
                    return node.val
                if node.val > target and node.left:
                    stack.append(node.left)
                if node.val < target and node.right:
                    stack.append(node.right)
                if minValue > abs(node.val - target):
                    minValue = abs(node.val - target)
                    key = node.val
                
        return key

       
       
Success
Details 
Runtime: 62 ms, faster than 43.01% of Python3 online submissions for Closest Binary Search Tree Value.
Memory Usage: 17.1 MB, less than 5.17% of Python3 online submissions for Closest Binary Search Tree Value.

 
 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        
        if not root:
            return 0
        nodes = []
        def inOrder(node):
            if not node:
                return 0
            inOrder(node.left)
            nodes.append(node.val)
            inOrder(node.right)
        
        inOrder(root)
        return min([[abs(n- target),n] for n in nodes])[1]
