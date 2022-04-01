Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.
 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].
Example 2:


Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]

Success
Details 
Runtime: 48 ms, faster than 83.09% of Python3 online submissions for Average of Levels in Binary Tree.
Memory Usage: 16.8 MB, less than 21.36% of Python3 online submissions for Average of Levels in Binary Tree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        
        stack, averages = [root], []
       
        while stack:
            total =0
            
            lenOfNodes = len(stack)
            print(lenOfNodes)
            for i in range(lenOfNodes):
                node = stack.pop(0)
                print(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            
                total += node.val
                
            averages.append(total / lenOfNodes)
        return averages

       
       Success
Details 
Runtime: 40 ms, faster than 99.60% of Python3 online submissions for Average of Levels in Binary Tree.
Memory Usage: 16.4 MB, less than 89.61% of Python3 online submissions for Average of Levels in Binary Tree.
 
 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        result, stack = [],deque([root])
        while stack:
            
            total, length =0, len(stack)
            for i in range(length):
                node = stack.popleft()
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
                
                total += node.val
            result.append(total/length)
        return result
