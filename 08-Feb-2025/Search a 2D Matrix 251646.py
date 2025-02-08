# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        row,col = len(matrix),len(matrix[0])
        left = 0
        right = row*col -1
        while left <= right:
            mid = (left+right) // 2
            r,c = divmod(mid,col)
            if matrix[r][c] == target:
                return True
            elif(matrix[r][c] < target):
                left = mid+1
            elif (matrix[r][c] > target):
                right = mid-1
        return False



