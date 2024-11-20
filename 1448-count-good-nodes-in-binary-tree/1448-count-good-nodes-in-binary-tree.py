# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def search(curr, mx):
            if not curr:
                return
            
            nonlocal cnt
            if curr.val >= mx:
                cnt += 1
            
            new_mx = max(curr.val, mx)
            search(curr.left, new_mx)
            search(curr.right, new_mx)
        
        cnt = 0
        search(root, float("-inf"))
        return cnt