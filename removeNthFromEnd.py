# 19. Remove Nth Node From End of List
# Medium

# 7397

# 374

# Add to List

# Share
# Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

# Example 1:


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]
 

# Constraints:

# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz




Success
Details 
Runtime: 20 ms, faster than 99.85% of Python3 online submissions for Remove Nth Node From End of List.
Memory Usage: 14.2 MB, less than 76.81% of Python3 online submissions for Remove Nth Node From End of List.
  
  
  
  # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        
        fast,slow = head,head
        counter = 0
        
        while counter < n:
            fast = fast.next
            counter += 1
            
        if not fast:
            return head.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return head  
  
