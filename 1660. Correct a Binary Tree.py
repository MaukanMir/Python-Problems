

Success
Details 
Runtime: 176 ms, faster than 90.45% of Python3 online submissions for Correct a Binary Tree.
Memory Usage: 27.6 MB, less than 63.28% of Python3 online submissions for Correct a Binary Tree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        
        queue = deque([root])
        
        while queue:
            curr = queue.popleft()
            
            if curr.right:
                if curr.right and curr.right.right and curr.right.right in queue:
                    curr.right = None
                    return root
                
                queue.append(curr.right)
            
            if curr.left:
                if curr.left and curr.left.right and curr.left.right in queue:
                    curr.left = None
                    return root
                queue.append(curr.left)
