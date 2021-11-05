# 206. Reverse Linked List
# Easy

# 9077

# 162

# Add to List

# Share
# Given the head of a singly linked list, reverse the list, and return the reversed list.

 

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Example 2:


# Input: head = [1,2]
# Output: [2,1]
# Example 3:

# Input: head = []
# Output: []
 

# Constraints:

# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000
 


Success
Details 
Runtime: 24 ms, faster than 99.51% of Python3 online submissions for Reverse Linked List.
Memory Usage: 15.7 MB, less than 45.75% of Python3 online submissions for Reverse Linked List.




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        if head and head.next is None:
            return head
        
        curr = head
        p1,p2 = None,curr
        
        while curr is not None:
            p3 = curr.next
            curr.next = p1
            p1 = curr
            curr = p3
        head = p1
        return head
