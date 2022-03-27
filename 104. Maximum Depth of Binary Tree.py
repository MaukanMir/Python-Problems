Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2

Success
Details 
Runtime: 57 ms, faster than 55.09% of Python3 online submissions for Maximum Depth of Binary Tree.
Memory Usage: 15.2 MB, less than 98.99% of Python3 online submissions for Maximum Depth of Binary Tree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root: return 0
        
        stack, maxValue =[[root,0]],float('-inf')
        
        while stack:
            node, distance = stack.pop()
            distance +=1
            maxValue = max(maxValue, distance)
            if node.left: stack.append([node.left, distance])
            if node.right: stack.append([node.right,distance])
        return maxValue
        
