Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:


Success
Details 
Runtime: 42 ms, faster than 93.29% of Python3 online submissions for Remove Duplicates from Sorted List II.
Memory Usage: 13.8 MB, less than 73.81% of Python3 online submissions for Remove Duplicates from Sorted List II.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0,head)
        curr = head
        first = dummy
        
        while curr:
            if curr and curr.next and curr.val == curr.next.val:
                while curr and curr.next and curr.val == curr.next.val:
                    curr = curr.next
                dummy.next = curr.next
            else:
                dummy = dummy.next
            curr = curr.next
        
        return first.next
