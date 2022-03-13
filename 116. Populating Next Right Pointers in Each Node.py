You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Example 1:


Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
Example 2:

Input: root = []
Output: []

Success
Details 
Runtime: 110 ms, faster than 26.27% of Python3 online submissions for Populating Next Right Pointers in Each Node.
Memory Usage: 15.6 MB, less than 62.25% of Python3 online submissions for Populating Next Right Pointers in Each Node.

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        leftMost = root
        
        while leftMost.left:
            
            head = leftMost
            
            while head:
                head.left.next = head.right
                
                if head.next:
                    head.right.next = head.next.left
                
                head = head.next
            
            leftMost = leftMost.left
        
        return root
