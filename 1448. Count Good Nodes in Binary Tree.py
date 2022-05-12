# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

# Return the number of good nodes in the binary tree.

 

# Example 1:



# Input: root = [3,1,4,3,null,1,5]
# Output: 4
# Explanation: Nodes in blue are good.
# Root Node (3) is always a good node.
# Node 4 -> (3,4) is the maximum value in the path starting from the root.
# Node 5 -> (3,4,5) is the maximum value in the path
# Node 3 -> (3,1,3) is the maximum value in the path.
# Example 2:



# Input: root = [3,3,null,4,2]
# Output: 3
# Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
# Example 3:

# Input: root = [1]
# Output: 1
# Explanation: Root is considered as good.

# Success
# Details 
# Runtime: 244 ms, faster than 82.01% of Python3 online submissions for Count Good Nodes in Binary Tree.
# Memory Usage: 33.5 MB, less than 49.44% of Python3 online submissions for Count Good Nodes in Binary Tree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        stack =[(root, float('-inf'))]
        maxValue = float('-inf')
        total =0
        while stack:
            node,check = stack.pop()
            
            if node:
            
                if check<=node.val:
                    total +=1
                if node.left:
                    
                    stack.append((node.left,max(check,node.val)))
                if node.right:
                    
                    stack.append((node.right, max(check,node.val)))
                     
                
        return total
       
Success
Details 
Runtime: 467 ms, faster than 12.65% of Python3 online submissions for Count Good Nodes in Binary Tree.
Memory Usage: 32.5 MB, less than 87.77% of Python3 online submissions for Count Good Nodes in Binary Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node,maxVal):
            if not node:
                return 0
            
            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal,node.val)
            res+= dfs(node.left,maxVal)
            res += dfs(node.right, maxVal)
            
            return res
        
        return dfs(root,root.val)
