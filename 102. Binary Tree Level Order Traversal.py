Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000


Success
Details 
Runtime: 51 ms, faster than 42.19% of Python3 online submissions for Binary Tree Level Order Traversal.
Memory Usage: 14.3 MB, less than 52.65% of Python3 online submissions for Binary Tree Level Order Traversal.



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        stack,res = deque([[root, 0]]), {}
        
        while stack:
            node,lvl = stack.popleft()
            
            if node.left:
                stack.append([node.left,lvl+1])
            if node.right:
                stack.append([node.right,lvl+1])
            
            if lvl not in res:
                res[lvl] = [node.val]
            else:
                res[lvl].append(node.val)

        return res.values()

       
Success
Details 
Runtime: 46 ms, faster than 55.13% of Python3 online submissions for Binary Tree Level Order Traversal.
Memory Usage: 15 MB, less than 9.21% of Python3 online submissions for Binary Tree Level Order Traversal.

       
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        levels = []
        if not root:
            return levels
        
        def bfs(root,lvl):
            if len(levels) == lvl:
                levels.append([])
            
            levels[lvl].append(root.val)
            if root.left:
                bfs(root.left,lvl+1)
            if root.right:
                bfs(root.right,lvl+1)
        bfs(root,0)
        return levels
