# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def search(root):
            if not root:
                return
            
            nonlocal mn, prev
            search(root.left)
            if prev:
                mn = min(mn, abs(prev.val-root.val))
            prev = root
            search(root.right)
        
        mn, prev = float("inf"), None
        search(root)
        return mn