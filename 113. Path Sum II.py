Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

 

Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: []
Example 3:

Input: root = [1,2], targetSum = 0
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000

Success
Details 
Runtime: 40 ms, faster than 94.65% of Python3 online submissions for Path Sum II.
Memory Usage: 19.3 MB, less than 27.51% of Python3 online submissions for Path Sum II.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        result = []
        if not root:
            return
        def dfs(node = root, runningSum =0, cur= []):
            if not node.left and not node.right:
                if node.val + runningSum == targetSum:
                    cur = cur + [node.val]
                    result.append(cur[:])
            else:
                for child in [node.left, node.right]:
                    if child:
                        dfs(child, runningSum + node.val, cur + [node.val])
        
        
        dfs()
        return result

Success
Details 
Runtime: 61 ms, faster than 65.75% of Python3 online submissions for Path Sum II.
Memory Usage: 19.2 MB, less than 28.62% of Python3 online submissions for Path Sum II.
  
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        res = []
        def dfs(root,total, totalSum):
            if not root:
                return 0
            if not root.left and not root.right:
                if targetSum == totalSum + root.val:
                    res.append(total + [root.val])
                return total
        
            dfs(root.left, total + [root.val],totalSum + root.val )
            dfs(root.right, total + [root.val],totalSum + root.val)
        
        dfs(root,[],0)
        return res
