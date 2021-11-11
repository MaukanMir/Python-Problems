# Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.

 

# Example 1:


# Input: root = [5,3,6,2,4,null,7], k = 9
# Output: true
# Example 2:


# Input: root = [5,3,6,2,4,null,7], k = 28
# Output: false
# Example 3:

# Input: root = [2,1,3], k = 4
# Output: true
# Example 4:

# Input: root = [2,1,3], k = 1
# Output: false
# Example 5:

# Input: root = [2,1,3], k = 3
# Output: true
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -104 <= Node.val <= 104
# root is guaranteed to be a valid binary search tree.
# -105 <= k <= 105


Success
Details 
Runtime: 76 ms, faster than 85.81% of Python3 online submissions for Two Sum IV - Input is a BST.
Memory Usage: 18.1 MB, less than 53.65% of Python3 online submissions for Two Sum IV - Input is a BST.




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        container = set()
    
        def findValue(root, k, container):
            if not root: return False
            
            if k - root.val in container:
                return True
            
            container.add(root.val)
            
            return findValue(root.left,k,container) or findValue(root.right,k, container)
        return findValue(root,k,container)
