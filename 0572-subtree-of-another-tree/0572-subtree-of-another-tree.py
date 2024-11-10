# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(r1, r2):
            match (r1, r2):
                case (None, None):
                    return True
                case (None, r) | (r, None):
                    return False
                case _:
                    return r1.val == r2.val and isSame(r1.left, r2.left) and isSame(r1.right, r2.right)
        
        res = isSame(root, subRoot)
        if root.left: res |= self.isSubtree(root.left, subRoot)
        if root.right: res |= self.isSubtree(root.right, subRoot)
        return res