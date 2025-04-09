# Problem: Construct Quad Tree - https://leetcode.com/problems/construct-quad-tree/description/

# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def isSame(r1, c1, length):
            val = grid[r1][c1]
            for i in range(r1, r1 + length):
                for j in range(c1, c1 + length):
                    if grid[i][j] != val:
                        return False
            return True
        
        def build(r1, c1, length):
            if isSame(r1, c1, length):
                return Node(val=bool(grid[r1][c1]), isLeaf=True)
            half = length // 2
            return Node(
                val=True,  
                isLeaf=False,
                topLeft=build(r1, c1, half),
                topRight=build(r1, c1 + half, half),
                bottomLeft=build(r1 + half, c1, half),
                bottomRight=build(r1 + half, c1 + half, half)
            )
        
        return build(0, 0, len(grid))
