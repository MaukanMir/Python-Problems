# Given the root of a binary tree, return all root-to-leaf paths in any order.

# A leaf is a node with no children.

 

# Example 1:


# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]
# Example 2:

# Input: root = [1]
# Output: ["1"]

# Success
# Details 
# Runtime: 28 ms, faster than 93.01% of Python3 online submissions for Binary Tree Paths.
# Memory Usage: 14.4 MB, less than 29.42% of Python3 online submissions for Binary Tree Paths.


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return ["1"]
        
            
        seen = []
        
        def dfs(node,ans):
            if not node.left and not node.right:
                ans += "->" + str(node.val)
                seen.append(ans[2:])
                ans =""
                return seen
            
            if node.left:
                dfs(node.left, ans + "->" + str(node.val))
            if node.right:
                dfs(node.right, ans + "->" + str(node.val))
        
        dfs(root,"")
        return seen
