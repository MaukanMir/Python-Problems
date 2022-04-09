Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100

Success
Details 
Runtime: 36 ms, faster than 84.54% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
Memory Usage: 14.1 MB, less than 60.90% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root: return []
        stack, count, keys = deque([[root,0]]),0, defaultdict(list)
        
        while stack:
            node, lvl = stack.popleft()

            if node.left:
                stack.append([node.left, lvl+1])
            if node.right:
                stack.append([node.right, lvl+1])
            
            if node and lvl not in keys:
                keys[lvl] = [node.val]
            elif node and lvl in keys:
                keys[lvl].append(node.val)
            
            
            count +=1
        
        res = []
        for idx,k in enumerate(keys):
            if idx %2 ==0:
                res.append(keys[k])
            else:
                res.append(keys[k][::-1])
        return res

Success
Details 
Runtime: 38 ms, faster than 73.82% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
Memory Usage: 14.1 MB, less than 60.90% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
 
 
 
 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root: return []
        stack, keys = deque([[root,0]]), defaultdict(list)
        
        while stack:
            node, lvl = stack.popleft()

            if node.left:
                stack.append([node.left, lvl+1])
            if node.right:
                stack.append([node.right, lvl+1])
            
            if node and lvl not in keys:
                keys[lvl] = [node.val]
            elif node and lvl in keys:
                keys[lvl].append(node.val)

        
        return [ keys[j] if i %2 ==0 else keys[j][::-1] for i,j in enumerate(keys) ]
      
       
     
