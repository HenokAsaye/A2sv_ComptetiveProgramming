# Problem: Reshape the Matrix - https://leetcode.com/problems/reshape-the-matrix/

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        new_mat = [[0] * c for _ in range(r)]
        row = len(mat)
        col = len(mat[0])
        if((col * row) != r*c):
            return mat
        temp = []
        for i in range(row):
            for j in range(col):
                temp.append(mat[i][j])
        print(temp)
        nr =0
        l=0
        while nr < r:
            for k in range(c):
                new_mat[nr][k] = temp[l]
                l+=1
            nr+=1
        return new_mat

        