# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

# A leaf is a node with no children.

 

# Example 1:


# Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# Output: true
# Example 2:


# Input: root = [1,2,3], targetSum = 5
# Output: false
# Example 3:

# Input: root = [1,2], targetSum = 0
# Output: false
 

# Constraints:

# The number of nodes in the tree is in the range [0, 5000].
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000


Success
Details 
Runtime: 36 ms, faster than 95.75% of Python3 online submissions for Path Sum.
Memory Usage: 15 MB, less than 77.61% of Python3 online submissions for Path Sum.
  
  
  
  
  # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        targetSum -= root.val
        if not root.left and not root.right:
            return targetSum ==0
        return self.hasPathSum(root.left,targetSum) or self.hasPathSum(root.right,targetSum)
  
  
Success
Details 
Runtime: 44 ms, faster than 69.62% of Python3 online submissions for Path Sum.
Memory Usage: 15 MB, less than 77.61% of Python3 online submissions for Path Sum.
 
 
 
 
 
 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        track = [(root,targetSum - root.val),]
        while track:
            node,curr_sum = track.pop()
            if not node.left and not node.right and curr_sum == 0:
                return True
            if node.right:
                track.append((node.right, curr_sum - node.right.val))
            if node.left:
                track.append((node.left, curr_sum - node.left.val))
        return False
