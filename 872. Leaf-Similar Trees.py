# Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.



# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

# Two binary trees are considered leaf-similar if their leaf value sequence is the same.

# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

 

# Example 1:


# Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
# Output: true
# Example 2:


# Input: root1 = [1,2,3], root2 = [1,3,2]
# Output: false
 

# Constraints:

# The number of nodes in each tree will be in the range [1, 200].
# Both of the given trees will have values in the range [0, 200].

Success
Details 
Runtime: 20 ms, faster than 99.80% of Python3 online submissions for Leaf-Similar Trees.
Memory Usage: 14.2 MB, less than 70.97% of Python3 online submissions for Leaf-Similar Trees.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def find(root):
            seen = []
            stack = [root]
            
            while stack:
                node = stack.pop()
                if not node:
                    continue
                if not node.left and not node.right:
                    seen.append(node.val)
                else:
                    stack.append(node.right)
                    stack.append(node.left)
            return seen
        return find(root1) == find(root2)
