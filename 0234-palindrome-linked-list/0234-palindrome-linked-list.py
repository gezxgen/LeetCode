# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        res: list[int] = []
            
        while head:
            res.append(head.val)
            head = head.next
        
        n: int = len(res)
        for i in range(n // 2):
            if res[i] != res[n-i-1]:
                return False
        return True