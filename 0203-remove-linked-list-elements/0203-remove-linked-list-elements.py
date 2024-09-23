# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        d = ListNode(0)
        d.next = head
        p = d
        c = head
        
        while c:
            if c.val == val:
                p.next = c.next
            else:
                p = c
            c = c.next
            
        return d.next