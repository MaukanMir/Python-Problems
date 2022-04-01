Given the root of a binary tree, return the postorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [3,2,1]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
 

Success
Details 
Runtime: 31 ms, faster than 88.24% of Python3 online submissions for Binary Tree Postorder Traversal.
Memory Usage: 14 MB, less than 15.44% of Python3 online submissions for Binary Tree Postorder Traversal.



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []
        
        def postOrder(node):
            if node:
                postOrder(node.left)
                postOrder(node.right)
                result.append(node.val)
        
        postOrder(root)
        return result
