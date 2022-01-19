

Success
Details 
Runtime: 184 ms, faster than 16.74% of Python3 online submissions for Sum of Nodes with Even-Valued Grandparent.
Memory Usage: 17.7 MB, less than 91.38% of Python3 online submissions for Sum of Nodes with Even-Valued


Given the root of a binary tree, return the sum of values of nodes with an even-valued grandparent. If there are no nodes with an even-valued grandparent, return 0.

A grandparent of a node is the parent of its parent if it exists.

 

Example 1:


Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18
Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.
Example 2:


Input: root = [1]
Output: 0
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
1 <= Node.val <= 100
  
  # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        self. result, stack = 0,[root]
        
        
        while stack:
            node = stack.pop(0)
            
            if node.val %2 ==0:
                    self.find(node,0)
            if node.left:
                    stack.append(node.left)
            if node.right:
                    stack.append(node.right)
        return self.result
    
    def find(self,node,level):
        if level ==2:
            self.result += node.val
            return
        
        if node.left:
            self.find(node.left,level+1)
        if node.right:
            self.find(node.right,level+1)
