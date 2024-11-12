# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def make(start: int, end: int) -> Optional[TreeNode]:
            nonlocal nums
            
            # escape sequence
            if start > end:
                return None
            
            # initialize root
            M = (start + end) // 2
            curr = TreeNode(nums[M])
            
            # calculate children & return
            curr.left = make(start, M - 1)
            curr.right = make(M + 1, end)
            return curr
        
        nums.sort()
        return make(0, len(nums) - 1)