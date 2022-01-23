# A binary expression tree is a kind of binary tree used to represent arithmetic expressions. Each node of a binary expression tree has either zero or two children. Leaf nodes (nodes with 0 children) correspond to operands (variables), and internal nodes (nodes with two children) correspond to the operators. In this problem, we only consider the '+' operator (i.e. addition).

# You are given the roots of two binary expression trees, root1 and root2. Return true if the two binary expression trees are equivalent. Otherwise, return false.

# Two binary expression trees are equivalent if they evaluate to the same value regardless of what the variables are set to.

 

# Example 1:

# Input: root1 = [x], root2 = [x]
# Output: true
# Example 2:



# Input: root1 = [+,a,+,null,null,b,c], root2 = [+,+,a,b,c]
# Output: true
# Explaination: a + (b + c) == (b + c) + a
# Example 3:



# Input: root1 = [+,a,+,null,null,b,c], root2 = [+,+,a,b,d]
# Output: false
# Explaination: a + (b + c) != (b + d) + a
 

# Constraints:

# The number of nodes in both trees are equal, odd and, in the range [1, 4999].
# Node.val is '+' or a lower-case English letter.
# It's guaranteed that the tree given is a valid binary expression tree.


# Success
# Details 
# Runtime: 556 ms, faster than 96.97% of Python3 online submissions for Check If Two Expression Trees are Equivalent.
# Memory Usage: 17 MB, less than 35.35% of Python3 online submissions for Check If Two Expression Trees are Equivalent.


# Definition for a binary tree node.
# class Node(object):
#     def __init__(self, val=" ", left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEquivalence(self, root1: 'Node', root2: 'Node') -> bool:
        
        return self.findChars(root1) == self.findChars(root2)
    def findChars(self,root):
        
        queue = deque( [(root)] )
        keys = defaultdict(int)
        
        while queue:
            node = queue.popleft()
            if node.val.isalpha():
                keys[node.val] +=1
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return keys
