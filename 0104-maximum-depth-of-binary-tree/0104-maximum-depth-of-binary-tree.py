# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def search(root) -> int:
            if not root:
                return 0
            
            length1 = search(root.right) + 1
            length2 = search(root.left) + 1
            return max(length1, length2)
        
        return search(root)