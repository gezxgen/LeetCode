# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # save the current element, the next and previous element
        # connect the next element to the previous while elements
        if not head:
            return head
        
        current = head
        previous = None
        comming = head.next
        
        while current:
            comming = current.next
            current.next = previous
            previous = current
            current = comming
        return previous