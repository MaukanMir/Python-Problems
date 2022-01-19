



Example 1:


Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15
Example 2:

Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 19
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
1 <= Node.val <= 100

Success
Details 
Runtime: 204 ms, faster than 85.25% of Python3 online submissions for Deepest Leaves Sum.
Memory Usage: 17.8 MB, less than 73.16% of Python3 online submissions for Deepest Leaves Sum.
Given the root of a binary tree, return the sum of values of its deepest leaves.
 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        
        if not root:
            return 0

        deepest, depth = 0,0
        stack =[ (root,0) ]
       
        while stack:
            node, currDepth = stack.pop()
            
            if node:
                if not node.right and not node.left:
                    if currDepth > depth:
                        deepest = node.val
                        depth = currDepth
                    elif currDepth == depth:
                        deepest += node.val
                else:
                    
                    if node.right:
                        stack.append((node.right,currDepth+1))
                    if node.left:
                        stack.append((node.left,currDepth+1))
                
        return deepest
