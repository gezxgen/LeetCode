# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        count = 0
        
        def search(node):
            if not node:
                return None
            
            nonlocal count
            count += 1
            search(node.left)
            search(node.right)
        
        search(root)
        return count