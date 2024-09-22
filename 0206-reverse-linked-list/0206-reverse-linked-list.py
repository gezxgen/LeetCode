# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, h: Optional[ListNode]) -> Optional[ListNode]:
        # save the current element, the next and previous element
        # connect the next element to the previous while elements
        if not h:
            return h
        
        c = h
        p = None
        n = h.next
        
        while c:
            n = c.next
            c.next = p
            p = c
            c = n
        return p