# Given the root of a binary tree, construct a string consisting of parenthesis and integers from a binary tree with the preorder traversal way, and return it.

# Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship between the string and the original binary tree.

 

# Example 1:


# Input: root = [1,2,3,4]
# Output: "1(2(4))(3)"
# Explanation: Originally, it needs to be "1(2(4)())(3()())", but you need to omit all the unnecessary empty parenthesis pairs. And it will be "1(2(4))(3)"
# Example 2:


# Input: root = [1,2,3,null,4]
# Output: "1(2()(4))(3)"
# Explanation: Almost the same as the first example, except we cannot omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -1000 <= Node.val <= 1000

# Success
# Details 
# Runtime: 44 ms, faster than 95.03% of Python3 online submissions for Construct String from Binary Tree.
# Memory Usage: 16.7 MB, less than 12.44% of Python3 online submissions for Construct String from Binary Tree



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        seen = []
        
        def preOrder(root):
            if root is None:
                return ""
            ans =""
            ans = str(root.val)
            if root.right:
                ans = ans + "(" + preOrder(root.left) +")"
                ans = ans + "(" + preOrder(root.right) +")"
            elif root.left:
                ans = ans + "(" + preOrder(root.left) +")"
            return ans
        return preOrder(root)
