# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res, queue = [], deque([root])
        cnt = 0
        
        while queue:
            curr = []
            for i in range(len(queue)):
                node = queue.popleft()
                
                # Append node values in current level
                curr.append(node.val)
                
                # Add child nodes to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Reverse the current level's values if it's an odd level
            if cnt % 2 == 1:
                curr.reverse()
                
            res.append(curr)
            cnt += 1
        
        return res