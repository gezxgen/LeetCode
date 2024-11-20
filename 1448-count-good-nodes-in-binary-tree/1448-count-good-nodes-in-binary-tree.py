# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def search(current, maximum):
            if not current:
                return
            
            nonlocal counter
            if current.val >= maximum:
                counter += 1
            
            new_max = max(current.val, maximum)
            search(current.left, new_max)
            search(current.right, new_max)
        
        counter = 0
        search(root, float("-inf"))
        return counter