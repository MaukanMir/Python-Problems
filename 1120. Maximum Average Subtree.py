# Given the root of a binary tree, return the maximum average value of a subtree of that tree. Answers within 10-5 of the actual answer will be accepted.

# A subtree of a tree is any node of that tree plus all its descendants.

# The average value of a tree is the sum of its values, divided by the number of nodes.

 

# Example 1:


# Input: root = [5,6,1]
# Output: 6.00000
# Explanation: 
# For the node with value = 5 we have an average of (5 + 6 + 1) / 3 = 4.
# For the node with value = 6 we have an average of 6 / 1 = 6.
# For the node with value = 1 we have an average of 1 / 1 = 1.
# So the answer is 6 which is the maximum.
# Example 2:

# Input: root = [0,null,1]
# Output: 1.00000

Success
Details 
Runtime: 48 ms, faster than 90.26% of Python3 online submissions for Maximum Average Subtree.
Memory Usage: 17 MB, less than 57.99% of Python3 online submissions for Maximum Average Subtree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        self.maxVal = float('-inf')
        
        def dfs(node):
            if not node:
                return (0,0)
            
            leftSum, leftCount = dfs(node.left)
            rightSum,rightCount = dfs(node.right)
            total = node.val + leftSum + rightSum
            count = leftCount + rightCount +1
            self.maxVal = max(self.maxVal, total/count)
            return total, count
        dfs(root)
        
        return self.maxVal
