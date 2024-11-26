class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def search(curr):
            if not curr:
                return
            
            search(curr.left)
            res.append(curr.val)
            search(curr.right)
        
        res = []
        search(root)
        return res[k - 1]