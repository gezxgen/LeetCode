# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def make(s , e):
            if s > e: return None
            nonlocal nums
            M = (s + e) // 2
            return TreeNode(nums[M], make(s, M - 1), make(M + 1, e))
        
        nums.sort()
        return make(0, len(nums) - 1)