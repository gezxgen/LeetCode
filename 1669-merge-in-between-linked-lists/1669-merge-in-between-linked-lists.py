# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        s2 = list1
        for _ in range(a - 1):
            s2 = s2.next
        
        e2 = s2.next
        for _ in range(b - a + 1):
            e2 = e2.next
        
        s2.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = e2
        
        return list1