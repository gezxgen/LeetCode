# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head
        nums: list[int] = []
        
        # get nums
        while head:
            nums.append(head.val)
            head = head.next
        
        # sort nums
        nums.sort()
        head = dummy
        
        # set nums
        while nums:
            head.val = nums.pop(0)
            head = head.next
        
        return dummy