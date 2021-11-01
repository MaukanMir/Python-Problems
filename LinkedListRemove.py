
# 203. Remove Linked List Elements
# Easy

# 3607

# 139

# Add to List

# Share
# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

 

# Example 1:


# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]
# Example 2:

# Input: head = [], val = 1
# Output: []
# Example 3:

# Input: head = [7,7,7,7], val = 7
# Output: []





# Success
# Details 
# Runtime: 60 ms, faster than 97.49% of Python3 online submissions for Remove Linked List Elements.
# Memory Usage: 17.2 MB, less than 68.48% of Python3 online submissions for Remove Linked List Elements.
  
  
  
  
  
  class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
    
        sentinel = ListNode(0)
        sentinel.next = head
        prev,curr = sentinel, head
        
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return sentinel.next
