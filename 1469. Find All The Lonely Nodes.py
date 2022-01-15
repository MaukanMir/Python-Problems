# In a binary tree, a lonely node is a node that is the only child of its parent node. The root of the tree is not lonely because it does not have a parent node.

# Given the root of a binary tree, return an array containing the values of all lonely nodes in the tree. Return the list in any order.

 

# Example 1:


# Input: root = [1,2,3,null,4]
# Output: [4]
# Explanation: Light blue node is the only lonely node.
# Node 1 is the root and is not lonely.
# Nodes 2 and 3 have the same parent and are not lonely.
# Example 2:


# Input: root = [7,1,4,6,null,5,3,null,null,null,null,null,2]
# Output: [6,2]
# Explanation: Light blue nodes are lonely nodes.
# Please remember that order doesn't matter, [2,6] is also an acceptable answer.
# Example 3:



# Input: root = [11,99,88,77,null,null,66,55,null,null,44,33,null,null,22]
# Output: [77,55,33,66,44,22]
# Explanation: Nodes 99 and 88 share the same parent. Node 11 is the root.
# All other nodes are lonely.

# Success
# Details 
# Runtime: 64 ms, faster than 41.62% of Python3 online submissions for Find All The Lonely Nodes.
# Memory Usage: 15.5 MB, less than 42.23% of Python3 online submissions for Find All The Lonely Nodes.


class Solution:
 
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        
        seen = []
        def traverse(root):
            if root:
                if root.right and root.left:
                    traverse(root.left)
                    traverse(root.right)
                elif root.left:
                    seen.append(root.left.val)
                    traverse(root.left)
                elif root.right:
                    seen.append(root.right.val)
                    traverse(root.right)
        
        traverse(root)
        return seen

  Success
Details 
Runtime: 59 ms, faster than 48.01% of Python3 online submissions for Find All The Lonely Nodes.
Memory Usage: 14.6 MB, less than 98.01% of Python3 online submissions for Find All The Lonely Nodes.
    
       
       # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        
        stack = []
        deque = collections.deque([(root,TreeNode())])
        
        while deque:
            node, parent = deque.popleft()
            print(parent)
            if node:
                if parent.right and not parent.left or parent.left and not parent.right:
                    stack.append(node.val)
                if node.left:
                    deque.append((node.left,node))
                if node.right:
                    deque.append((node.right, node))
        return stack
