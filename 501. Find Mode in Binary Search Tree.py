# Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

# If the tree has more than one mode, return them in any order.

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# Both the left and right subtrees must also be binary search trees.
 

# Example 1:


# Input: root = [1,null,2,2]
# Output: [2]
# Example 2:

# Input: root = [0]
# Output: [0]
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -105 <= Node.val <= 105
 

# Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).

# Success
# Details 
# Runtime: 48 ms, faster than 96.83% of Python3 online submissions for Find Mode in Binary Search Tree.
# Memory Usage: 18.4 MB, less than 54.49% of Python3 online submissions for Find Mode in Binary Search Tree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return [0]
        keys = {}
        
        stack = [root]
        seen = []
        
        while stack:
            node = stack.pop()
            
            if node:
                if node.val in keys: 
                    keys[node.val] +=1
                if node.val not in keys:
                    keys[node.val] =1
                
                
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        highest = max(keys, key=keys.get)
        for i in keys:
            if keys[i] == keys[highest]: seen.append(i)
        return seen if len(seen) >0 else keys.keys()

Success
Details 
Runtime: 2804 ms, faster than 5.01% of Python3 online submissions for Find Mode in Binary Search Tree.
Memory Usage: 18.5 MB, less than 44.13% of Python3 online submissions for Find Mode in Binary Search Tree.       
 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return 0
        
        stack,track = [root], {}
        
        while stack:
            node = stack.pop()
            
            if node:
                track[node.val] = track.get(node.val,0)+1
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return [n for n in track if track[n] == max(track.values())]
