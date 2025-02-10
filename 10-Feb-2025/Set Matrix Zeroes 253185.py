# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return
        row = len(matrix)
        col = len(matrix[0])
        z_infirst_row = any(matrix[0][j] == 0 for j in range(col))
        z_infirst_col = any(matrix[i][0] == 0 for i in range(row))
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if z_infirst_row:
            for j in range(col):
                matrix[0][j] = 0
        if z_infirst_col:
            for i in range(row):
                matrix[i][0] = 0
