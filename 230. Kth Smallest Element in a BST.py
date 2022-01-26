Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

 

Example 1:


Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:


Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

Success
Details 
Runtime: 70 ms, faster than 36.68% of Python3 online submissions for Kth Smallest Element in a BST.
Memory Usage: 18 MB, less than 59.68% of Python3 online submissions for Kth Smallest Element in a BST.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        
        stack, values = [root], []
        
        while stack:
            node = stack.pop()
            
            if node:
                values.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        values.sort()
        
        return values[k-1]

       
       
Success
Details 
Runtime: 48 ms, faster than 87.24% of Python3 online submissions for Kth Smallest Element in a BST.
Memory Usage: 18.2 MB, less than 16.52% of Python3 online submissions for Kth Smallest Element in a BST.
 
 
 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        values = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            values.append(node.val)
            dfs(node.right)
        dfs(root)
        return values[k-1]
