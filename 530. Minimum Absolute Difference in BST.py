# Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

 

# Example 1:


# Input: root = [4,2,6,1,3]
# Output: 1
# Example 2:


# Input: root = [1,0,48,null,null,12,49]
# Output: 1


# Success
# Details 
# Runtime: 48 ms, faster than 96.17% of Python3 online submissions for Minimum Absolute Difference in BST.
# Memory Usage: 16.1 MB, less than 90.68% of Python3 online submissions for Minimum Absolute Difference in BST.

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        
        # current =float("inf")
        # minValue = float("inf")
        stack = [root]
        seen = []
        
        while stack:
            node = stack.pop()
            
            if node:
                 seen.append(node.val)
                
                 if node.left:
                        stack.append(node.left)
                 if node.right: 
                        stack.append(node.right)
            

        
        seen.sort()
        
        return min([seen[n] - seen[n-1] for n in range(1,len(seen))])
