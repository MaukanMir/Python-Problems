You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []

Success
Details 
Runtime: 211 ms, faster than 24.56% of Python3 online submissions for Merge k Sorted Lists.
Memory Usage: 17.6 MB, less than 94.70% of Python3 online submissions for Merge k Sorted Lists.



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists)==0:
            return None
        
        while len(lists) >1:
            mergedLists = []
            
            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                mergedLists.append(self.mergeList(l1,l2))
            
            lists = mergedLists
        
        return lists[0]
    
    def mergeList(self,l1,l2):
        dummy = ListNode(0)
        tail = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next,l1 = l1, l1.next
            else:
                tail.next,l2 = l2, l2.next
            tail = tail.next
        
        tail.next = l1 if l1 else l2
        
        return dummy.next

       
       
 Success
Details 
Runtime: 114 ms, faster than 79.33% of Python3 online submissions for Merge k Sorted Lists.
Memory Usage: 17.6 MB, less than 76.39% of Python3 online submissions for Merge k Sorted Lists.
 
 # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists or len(lists) ==0:
            return None
        
        while len(lists) >1:
            merged = []
            for i in range(0,len(lists),2):
                l1, l2 = lists[i], lists[i+1] if i+1 < len(lists) else None
                
                merged.append(self.merge(l1,l2))
            lists = merged
        return lists[0]
    
    def merge(self,l1,l2):
        dummy = ListNode(0)
        tail = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next,l1 = l1, l1.next
            else:
                tail.next,l2 = l2, l2.next
            tail = tail.next
        
        tail.next = l1 if l1 else l2
        
        return dummy.next
