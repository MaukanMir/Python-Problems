
# Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.

 

# Example 1:


# Input: root = [4,2,6,1,3]
# Output: 1
# Example 2:


# Input: root = [1,0,48,null,null,12,49]
# Output: 1
  
Success
Details 
Runtime: 24 ms, faster than 97.54% of Python3 online submissions for Minimum Distance Between BST Nodes.
Memory Usage: 14.4 MB, less than 8.96% of Python3 online submissions for Minimum Distance Between BST


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        
        minValue = 1000
        
        stack = [root]
        seen = []
        
        while stack:
            node = stack.pop()
            
            if node:
                 seen.append(node.val)
                 if node.left:
                    stack.append(node.left)
                 if node.right:
                    stack.append(node.right)
        seen.sort()
        return min([ abs(seen[n] - seen[n-1]) for n in range(1,len(seen))])
