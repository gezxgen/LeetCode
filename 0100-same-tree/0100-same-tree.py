# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        match (p, q):
            case (None, None):
                return True
            case (r, None) | (None, r):
                return False
            case _:
                return p.val == q.val and self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
        