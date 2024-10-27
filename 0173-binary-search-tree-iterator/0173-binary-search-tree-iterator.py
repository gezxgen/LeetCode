# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        def inorder(root):
            stack, cur = [], root
            while cur or stack:
                if cur:
                    stack.append(cur)
                    cur = cur.left
                else:
                    cur = stack.pop()
                    self.BST.append(cur.val)
                    cur = cur.right
            
        self.BST, self.index= [], 0
        inorder(root)
        self.length = len(self.BST)

    def next(self) -> int:
        self.index += 1
        return self.BST[self.index - 1]

    def hasNext(self) -> bool:
        return self.index != self.length


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()