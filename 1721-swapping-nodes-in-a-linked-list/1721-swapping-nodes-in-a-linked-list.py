# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # check empty
        if not (head and head.next):
            return head

        # create dummy & node save
        dummy = ListNode(0)
        dummy.next, first, cnt = head, None, 0
        
        # get length & save before first
        while head:
            cnt += 1
            if cnt == k: first = head    # first is the node at the first swap
            head = head.next
        j: int = cnt-k          # j is the index node before second swap
        head = dummy.next
        
        # loop & check if second node is next
        cnt = 0
        while True:
            if cnt == j:
                first.val, head.val = head.val, first.val   # swap second with first
                return dummy.next
            cnt += 1
            head = head.next
            