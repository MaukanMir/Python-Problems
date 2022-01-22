# You are given the root of a binary tree with n nodes where each node in the tree has node.val coins. There are n coins in total throughout the whole tree.

# In one move, we may choose two adjacent nodes and move one coin from one node to another. A move may be from parent to child, or from child to parent.

# Return the minimum number of moves required to make every node have exactly one coin.

 

# Example 1:


# Input: root = [3,0,0]
# Output: 2
# Explanation: From the root of the tree, we move one coin to its left child, and one coin to its right child.
# Example 2:


# Input: root = [0,3,0]
# Output: 3
# Explanation: From the left child of the root, we move two coins to the root [taking two moves]. Then, we move one coin from the root of the tree to the right child.

# Success
# Details 
# Runtime: 45 ms, faster than 41.64% of Python3 online submissions for Distribute Coins in Binary Tree.
# Memory Usage: 14 MB, less than 99.58% of Python3 online submissions for Distribute Coins in Binary Tree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.total =0
        
        def dfs(node):
            if not node:
                return 0
            
            l,r = dfs(node.left), dfs(node.right)
            
            self.total += abs(l) + abs(r)
            return node.val + l + r -1
        
        dfs(root)
        return self.total
