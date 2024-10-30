# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def search(root):
            curr, stack = root, []
            
            while curr or stack:
                if curr:
                    stack.append(curr)
                    curr = curr.left
                else:
                    curr = stack.pop()
                    if not curr.left and not curr.right:
                        res.append(curr.val)
                    curr = curr.right
            
        res = []
        search(root1)
        res, res2 = [], res
        search(root2)
        return res == res2
        
        