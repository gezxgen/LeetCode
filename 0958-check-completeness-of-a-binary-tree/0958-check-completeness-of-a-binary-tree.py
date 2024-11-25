# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue, prev = deque(), 0
        queue.append([root, 1])
        
        while queue:
            node, index = queue.popleft()
            
            if index - 1 != prev:
                return False
            prev = index
            
            if node.left:
                queue.append([node.left, 2 * index])
            if node.right:
                queue.append([node.right, 2 * index + 1])
                
        return True
            