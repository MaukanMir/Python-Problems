# 876. Middle of the Linked List
# Easy

# 3603

# 95

# Add to List

# Share
# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.

 

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.
# Example 2:


# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

Success
Details 
Runtime: 20 ms, faster than 99.49% of Python3 online submissions for Middle of the Linked List.
Memory Usage: 14.1 MB, less than 73.84% of Python3 online submissions for Middle of the Linked List.

  
  
  # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head and not head.next:
            return 
        
        slow, fast = head, head
        
        while fast and  fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
