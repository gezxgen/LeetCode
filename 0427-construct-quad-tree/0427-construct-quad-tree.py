"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def same(grid: List[List[int]]) -> bool:
            n = len(grid)
            for i in range(n):
                for j in range(n):
                    if grid[i][j] != grid[0][0]:
                        return False
            return True
        
        # check if it is a leaf node
        if same(grid):
            return Node(bool(grid[0][0]), True)
        
        # if not, return a node with all smaller grids
        n = len(grid) // 2
        topleft, topright, bottomleft, bottomright = [], [], [], []
        
        for i in range(len(grid)):
            # top half
            if i < n:
                topleft.append(grid[i][0:n])
                topright.append(grid[i][n:])
            
            # bottom half
            else:
                bottomleft.append(grid[i][0:n])
                bottomright.append(grid[i][n:])
        
        return Node(True, False, self.construct(topleft),
                                 self.construct(topright),
                                 self.construct(bottomleft),
                                 self.construct(bottomright))
        