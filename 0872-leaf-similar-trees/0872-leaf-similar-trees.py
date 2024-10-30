# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def search(root):
            if not root:
                return
            
            nonlocal res
            search(root.right)
            if not root.left and not root.right:
                res.append(root.val)
            else:
                search(root.left)
            
        res = []
        search(root1)
        res, res2 = [], res
        search(root2)
        print(res, res2)
        return res == res2
        
        