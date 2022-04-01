Given the root of a binary tree, return the preorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [1,2,3]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100


Success
Details 
Runtime: 76 ms, faster than 5.38% of Python3 online submissions for Binary Tree Preorder Traversal.
Memory Usage: 13.8 MB, less than 63.16% of Python3 online submissions for Binary Tree Preorder Traversal.



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []
        
        def preOrder(node):
            if node:
                result.append(node.val)
                preOrder(node.left)
                preOrder(node.right)
        
        
        preOrder(root)
        return result

       
       
Success
Details 
Runtime: 46 ms, faster than 44.67% of Python3 online submissions for Binary Tree Preorder Traversal.
Memory Usage: 13.9 MB, less than 63.16% of Python3 online submissions for Binary Tree Preorder Traversal.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
    
        result,stack = [], [root]
        
        while stack:
            node = stack.pop()
            
            if node:
                result.append(node.val)
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
        return result
