# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def search(root):
            if not root:
                return
            
            nonlocal res
            search(root.left)
            if root.val >= low and root.val <= high:
                res += root.val
            search(root.right)
        
        res = 0
        search(root)
        return res