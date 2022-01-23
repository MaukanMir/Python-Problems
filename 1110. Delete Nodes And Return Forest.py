# Given the root of a binary tree, each node in the tree has a distinct value.

# After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

# Return the roots of the trees in the remaining forest. You may return the result in any order.

 

# Example 1:


# Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
# Output: [[1,2,null,4],[6],[7]]
# Example 2:

# Input: root = [1,2,4,null,3], to_delete = [3]
# Output: [[1,2,4]]
 

# Constraints:

# The number of nodes in the given tree is at most 1000.
# Each node has a distinct value between 1 and 1000.
# to_delete.length <= 1000
# to_delete contains distinct values between 1 and 1000.

Success
Details 
Runtime: 68 ms, faster than 76.83% of Python3 online submissions for Delete Nodes And Return Forest.
Memory Usage: 15 MB, less than 25.29% of Python3 online submissions for Delete Nodes And Return Forest.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        def delete(node,parent,values):
            if not node:
                return None
            
            if node.val in to_delete:
                delete(node.left, None, values)
                delete(node.right,None,values)
                return None
            else:
                if not parent:
                    values.append(node)
                node.left = delete(node.left,node,values)
                node.right = delete(node.right,node,values)
                return node
        
        to_delete = set(to_delete)
        values = []
        delete(root,None,values)
        return values
