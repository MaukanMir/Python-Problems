
# 83. Remove Duplicates from Sorted List
# Easy

# 3512

# 163

# Add to List

# Share
# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

# Example 1:


# Input: head = [1,1,2]
# Output: [1,2]
# Example 2:


# Input: head = [1,1,2,3,3]
# Output: [1,2,3]
 

# Constraints:

# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.





# Success
# Details 
# Runtime: 44 ms, faster than 68.60% of Python3 online submissions for Remove Duplicates from Sorted List.
# Memory Usage: 14.3 MB, less than 24.73% of Python3 online submissions for Remove Duplicates from Sorted List.















# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current_node = head
        
        while head:
            while head.next and head.next.val == head.val:
                head.next = head.next.next
            
            head = head.next
        
        return current_node
