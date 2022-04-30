Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz



Success
Details 
Runtime: 36 ms, faster than 84.05% of Python3 online submissions for Remove Nth Node From End of List.
Memory Usage: 13.8 MB, less than 98.90% of Python3 online submissions for Remove Nth Node From End of List.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count,check = 0,head
        
        while check:
            count+=1
            check = check.next
        
        if count == n:
            return head.next
        check,foundNode = head, count - n -1
        
        for i in range(0, foundNode):
            check = check.next
        
        check.next = check.next.next
        
        return head

       
       Success
Details 
Runtime: 24 ms, faster than 99.61% of Python3 online submissions for Remove Nth Node From End of List.
Memory Usage: 13.9 MB, less than 82.98% of Python3 online submissions for Remove Nth Node From End of List.
 
 
 
 # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        currentNode = head
        
        for i in range(n):
            currentNode = currentNode.next
        
        if currentNode is None:
            return head.next
        
        newNode = head
        
        while currentNode.next is not None:
            newNode = newNode.next
            currentNode = currentNode.next
        
        newNode.next = newNode.next.next
        
        return head

       
Success
Details 
Runtime: 26 ms, faster than 98.46% of Python3 online submissions for Remove Nth Node From End of List.
Memory Usage: 13.9 MB, less than 21.58% of Python3 online submissions for Remove Nth Node From End of List.
 
 
 
 # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        left, right = dummy, head
        
        while n >0 and right:
            right = right.next
            n -=1
            
        while right:
            right = right.next
            left = left.next
        
        left.next = left.next.next
        
        return dummy.next
