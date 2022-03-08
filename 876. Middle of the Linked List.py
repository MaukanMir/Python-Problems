Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:


Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

Success
Details 
Runtime: 41 ms, faster than 58.17% of Python3 online submissions for Middle of the Linked List.
Memory Usage: 13.8 MB, less than 97.75% of Python3 online submissions for Middle of the Linked List.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        curr, fast,count,check = head, head,0, head
        
        while check is not None:
            count+=1
            check= check.next
    
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            curr = curr.next
            
        
        return curr if count %2 !=0 else curr.next
