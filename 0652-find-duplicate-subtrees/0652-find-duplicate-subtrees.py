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
            
            subtree = f"{node.val},{serialize(node.left)},{serialize(node.right)}"
            count[subtree] += 1
            if count[subtree] == 2:
                duplicates.append(node)
            return subtree

        count, duplicates = defaultdict(int), []
        serialize(root)
        return duplicates