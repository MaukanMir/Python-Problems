# 102. Binary Tree Level Order Traversal
# Medium

# 6274

# 127

# Add to List

# Share
# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000



Success
Details 
Runtime: 28 ms, faster than 96.08% of Python3 online submissions for Binary Tree Level Order Traversal.
Memory Usage: 15.3 MB, less than 9.11% of Python3 online submissions for Binary Tree Level Order Traversal.

  
  
  # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        stages = []
        if not root:return stages
        
    
        def traverse(root,stage):
            if len(stages) == stage:
                stages.append([])

            stages[stage].append(root.val)


            if root.left:
                traverse(root.left,stage+1)
            if root.right:
                traverse(root.right,stage+1)
        
        traverse(root,0)
        return stages
