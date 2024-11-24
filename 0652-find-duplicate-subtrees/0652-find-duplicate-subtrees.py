# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def serialize(node: Optional[TreeNode]) -> str:
            if not node:
                return "#"
            
            sub = f"{node.val},{serialize(node.left)},{serialize(node.right)}"
            cnt[sub] += 1
            if cnt[sub] == 2:
                dup.append(node)
            return sub

        cnt, dup = defaultdict(int), []
        serialize(root)
        return dup