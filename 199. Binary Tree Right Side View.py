
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

Example 1:


Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = []
Output: []


Success
Details 
Runtime: 41 ms, faster than 60.37% of Python3 online submissions for Binary Tree Right Side View.
Memory Usage: 13.8 MB, less than 71.42% of Python3 online submissions for Binary Tree Right Side View.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        res,stack = [],deque([root])
        
        while stack:
            rightSide, stackSize = None, len(stack)
            
            for i in range(stackSize):
                node = stack.popleft()
                if node:
                    stack.append(node.left)
                    stack.append(node.right)
                    rightSide = node
            
            if rightSide:
                res.append(rightSide.val)
        
        return res
