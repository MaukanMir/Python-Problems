Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

 

Example 1:


Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]
Example 2:

Input: root = [1,2,3]
Output: [1,3]
 

Constraints:

The number of nodes in the tree will be in the range [0, 104].
-231 <= Node.val <= 231 - 1

Success
Details 
Runtime: 40 ms, faster than 95.92% of Python3 online submissions for Find Largest Value in Each Tree Row.
Memory Usage: 16.3 MB, less than 84.21% of Python3 online submissions for Find Largest Value in Each Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        values,queue = [],deque([root])
        
        while queue:
            size,maxVal = len(queue),float("-inf")
            for _ in range(size):
                node = queue.popleft()
                maxVal = max(maxVal,node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            values.append(maxVal)
        return values
