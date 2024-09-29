# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        left, right = head, head
        for _ in range(k-1):
            right = right.next
        cur = right
        
        while cur.next:
            cur = cur.next
            left = left.next
        left.val, right.val = right.val, left.val    
        return head
            