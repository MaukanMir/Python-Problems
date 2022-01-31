Given the root of a binary tree, return the most frequent subtree sum. If there is a tie, return all the values with the highest frequency in any order.

The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself).

 

Example 1:


Input: root = [5,2,-3]
Output: [2,-3,4]
Example 2:


Input: root = [5,2,-5]
Output: [2]
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105

Success
Details 
Runtime: 48 ms, faster than 84.65% of Python3 online submissions for Most Frequent Subtree Sum.
Memory Usage: 17.4 MB, less than 64.33% of Python3 online submissions for Most Frequent Subtree Sum.



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        
        values = defaultdict(int)
        
        def findNodes(node):
            if not node:
                return 0
            
            total = findNodes(node.left) + findNodes(node.right) + node.val
            values[total] +=1
            return total
            
        
        findNodes(root)
        
        found = max(values.values())
        
        return [key for key, v in values.items() if v == found]
