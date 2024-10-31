# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def search(root):
            if not root:
                return 0
            
            L, R = search(root.left), search(root.right)
            self.mx = max(self.mx, L + R + 1)
            return max(L, R) + 1
            
        self.mx = 0
        search(root)
        return self.mx - 1