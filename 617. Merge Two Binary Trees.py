# You are given two binary trees root1 and root2.

# Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

# Return the merged tree.

# Note: The merging process must start from the root nodes of both trees.

 

# Example 1:


# Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
# Output: [3,4,5,5,4,null,7]
# Example 2:

# Input: root1 = [1], root2 = [1,2]
# Output: [2,2]
 

# Constraints:

# The number of nodes in both trees is in the range [0, 2000].
# -104 <= Node.val <= 104


Success
Details 
Runtime: 84 ms, faster than 83.24% of Python3 online submissions for Merge Two Binary Trees.
Memory Usage: 15.1 MB, less than 99.00% of Python3 online submissions for Merge Two Binary Trees.

  
  
  
  # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root1 == None:return root2
        if root2 == None: return root1
        
        root1.val += root2.val
        
        root1.left = self.mergeTrees(root1.left , root2.left)
        root1.right = self.mergeTrees(root1.right , root2.right)
        
        return root1

       
       # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root1 and not root2:
            return None
        
        r1 = root1.val if root1 is not None else 0
        r2 = root2.val if root2 is not None else 0
        root = TreeNode(r1 + r2)
        
        root.left = self.mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
        root.right = self.mergeTrees(root1.right if root1 else None, root2.right if root2 else None)
        
        return root
    
    # Success
# Details 
# Runtime: 94 ms, faster than 81.20% of Python3 online submissions for Merge Two Binary Trees.
# Memory Usage: 15.4 MB, less than 81.35% of Python3 online submissions for Merge Two Binary Trees.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None:
            return root2
        
        stack = [[root1,root2]]
        
        while stack:
            t1, t2 = stack.pop()
            
            if t1 is None or t2 is None:continue

            t1.val += t2.val

            if t1.left is None:
                t1.left = t2.left
            else:stack.append([t1.left,t2.left])
            
            if t1.right is None:
                t1.right = t2.right
            else:
                stack.append([t1.right, t2.right])
        
        return root1
