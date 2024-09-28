# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # get middle
        dummy, slow, fast, prev = head, head, head, None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # reverse second half
        slow = prev
        prev, cur, temp = None, slow, slow.next
        while temp:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        # check max twin
        mx: int = 0
        while dummy:
            mx = max(mx, prev.val + dummy.val)
            prev, dummy = prev.next, dummy.next
        return mx