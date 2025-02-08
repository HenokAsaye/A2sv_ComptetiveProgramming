# Problem: Largest Local Values in a Matrix - https://leetcode.com/problems/largest-local-values-in-a-matrix/

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        row = len(grid)
        col = len(grid[0])
        ans = [[0] * (col-2) for _ in range(row-2)]
        for i in range(row-2):
            for j in range((col-2)):
                mx  = float("-inf")
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        current = grid[k][l]
                        mx = max(mx,current)
                        ans[i][j] = mx
        return ans


   

        