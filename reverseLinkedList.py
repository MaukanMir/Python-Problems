






class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
	if head is None:
		return head
	if head and head.next == None:
		return head
	
	prev,curr = None,head
	
	while curr:
		next_node = curr.next
		curr.next = prev
		prev = curr
		curr = next_node
	head = prev
	return head
