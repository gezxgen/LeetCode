# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # define reverse function
        def reverse(head: Optional[ListNode]):
            cur, prev = head, None
            while cur:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            return prev
        
        # reverse list
        rev = reverse(head)
        cur = rev
        mx: int = cur.val
        
        # remove next element if smaller than previous
        while cur and cur.next:
            mx = max(mx, cur.val)
            if cur.next.val < mx:
                cur.next = cur.next.next
            else:
                cur = cur.next
        
        # reverse list again
        # return head
        return reverse(rev)