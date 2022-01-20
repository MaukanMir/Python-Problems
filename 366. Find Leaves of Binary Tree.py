# Given the root of a binary tree, collect a tree's nodes as if you were doing this:

# Collect all the leaf nodes.
# Remove all the leaf nodes.
# Repeat until the tree is empty.
 

# Example 1:


# Input: root = [1,2,3,4,5]
# Output: [[4,5,3],[2],[1]]
# Explanation:
# [[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers since per each level it does not matter the order on which elements are returned.
# Example 2:

# Input: root = [1]
# Output: [[1]]


# Success
# Details 
# Runtime: 32 ms, faster than 74.02% of Python3 online submissions for Find Leaves of Binary Tree.
# Memory Usage: 14.2 MB, less than 83.70% of Python3 online submissions for Find Leaves of Binary Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        output = collections.defaultdict(list)
        
        def dfs(node,layer):
            if not node:
                return layer
            
            left = dfs(node.left,layer)
            right = dfs(node.right,layer)
            
            layer = max(left,right)
            output[layer].append(node.val)
            return layer+1
        dfs(root,0)
        return output.values()
        
