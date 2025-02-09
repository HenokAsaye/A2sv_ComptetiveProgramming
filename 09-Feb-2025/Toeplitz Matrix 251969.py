# Problem: Toeplitz Matrix - https://leetcode.com/problems/toeplitz-matrix/

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        for i in range(col):
            r=0
            c = i
            first_element = matrix[r][c]
            while r < row and c < col:
                if(matrix[r][c] != first_element):
                    return False
                r+=1
                c+=1
        for j in range(1,row):
            r=j
            c=0
            second_element = matrix[r][c]
            while r<row and c <col:
                if(matrix[r][c] != second_element):
                    return False
                r+=1
                c+=1
        return True

