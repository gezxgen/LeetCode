# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        def inorder(root):
            if not root:
                return
            
            inorder(root.left)
            self.stack.append(root.val)
            inorder(root.right)
            
        self.stack, self.index= [], 0
        inorder(root)
        self.length = len(self.stack)

    def next(self) -> int:
        self.index += 1
        return self.stack[self.index - 1]

    def hasNext(self) -> bool:
        return self.index != self.length


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()