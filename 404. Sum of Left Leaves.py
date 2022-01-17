

Given the root of a binary tree, return the sum of all left leaves.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
Example 2:

Input: root = [1]
Output: 0
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-1000 <= Node.val <= 1000

Success
Details 
Runtime: 56 ms, faster than 14.09% of Python3 online submissions for Sum of Left Leaves.
Memory Usage: 14.4 MB, less than 94.92% of Python3 online submissions for Sum of Left Leaves.



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        
        def dfs(node):
            return node is not None and node.left is None and node.right is None
        stack= [root]
        total =0
        while stack:
            node = stack.pop()
            
            if dfs(node.left):
                    total += node.left.val
            if node.right is not None:
                    stack.append(node.right)
            if node.left is not None:
                    stack.append(node.left)
        
                
        return total
        
