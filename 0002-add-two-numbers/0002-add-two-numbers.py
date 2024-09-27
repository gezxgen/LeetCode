# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1: list[str] = []
        list2: list[str] = []
        
        # get numbers of l1 and l2 and store them in an array
        while l1 and l2:
            list1.append(str(l1.val))
            list2.append(str(l2.val))
            l1, l2 = l1.next, l2.next
        
        if l1:
            while l1:
                list1.append(str(l1.val))
                l1 = l1.next
        else:
            while l2:
                list2.append(str(l2.val))
                l2 = l2.next
        
        # calculate the new array
        list1.reverse()
        list2.reverse()
        tot: str = str(int("".join(list1)) + int("".join(list2)))[::-1]
        cnt: int = 0
        
        # create new linked list & return
        cur = ListNode()
        dummy = cur
        
        while cnt != len(tot):
            cur.next = ListNode(tot[cnt])
            cur = cur.next
            cnt += 1
        
        return dummy.next
        
        