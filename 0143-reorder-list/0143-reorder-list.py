# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # check empty
        if (not head) or (not head.next) or (not head.next.next):
            return head
        
        # get middle
        prev, slow, fast = None, head, head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        
        # reverse second half
        prev, cur, temp = None, slow, slow.next
        while temp:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        # merge both halfs
        while head.next:
            temp = head.next    # save next
            temp2 = prev.next
            head.next = prev    # realign merge
            prev.next = temp
            head = temp         # load save
            prev = temp2
        head.next = prev        # assign rest of second half