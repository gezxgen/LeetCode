class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:  # Validate the index
            return -1
        
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:  # Validate the index
            return
        
        # Use a dummy node to simplify edge case handling
        dummy = ListNode(0)
        dummy.next = self.head
        cur = dummy
        
        # Traverse to the node before the target index
        for _ in range(index):
            cur = cur.next

        # Insert the new node
        new_node = ListNode(val)
        new_node.next = cur.next
        cur.next = new_node

        # Update head in case the new node is inserted at the start
        self.head = dummy.next
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:  # Validate the index
            return
        
        # Use a dummy node to simplify edge case handling
        dummy = ListNode(0)
        dummy.next = self.head
        cur = dummy
        
        # Traverse to the node before the target index
        for _ in range(index):
            cur = cur.next

        # Delete the target node
        cur.next = cur.next.next

        # Update head in case the head is removed
        self.head = dummy.next
        self.size -= 1
