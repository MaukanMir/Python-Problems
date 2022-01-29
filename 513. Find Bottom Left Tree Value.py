Given the root of a binary tree, return the leftmost value in the last row of the tree.

 

Example 1:


Input: root = [2,1,3]
Output: 1
Example 2:


Input: root = [1,2,3,4,null,5,6,null,null,7]
Output: 7

Success
Details 
Runtime: 36 ms, faster than 97.19% of Python3 online submissions for Find Bottom Left Tree Value.
Memory Usage: 16.9 MB, less than 23.41% of Python3 online submissions for Find Bottom Left Tree Value.
  
  
  
  # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        values = [-1,0]
        def dfs(node,level):
            if not node:
                return 
            if level > values[0]:
                values[0], values[1] = level, node.val
            dfs(node.left,level+1)
            dfs(node.right,level+1)
        
        dfs(root,0)
        return values[-1]
