# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # set up dummy
        c = d = ListNode()
        
        # merge while both have values
        while l1 and l2:
            if l1.val < l2.val:
                c.next = l1
                l1 = l1.next
                c = c.next
            else:
                c.next = l2
                l2 = l2.next
                c = c.next
        
        # merge after 1 is empty
        c.next = l1 if l1 else l2
            
        # return
        return d.next
                