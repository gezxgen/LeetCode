# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root, sm):
        if not root:
            return False

        if not root.left and not root.right and root.val == sm:
            return True
        
        sm -= root.val

        return self.hasPathSum(root.left, sm) or self.hasPathSum(root.right, sm)