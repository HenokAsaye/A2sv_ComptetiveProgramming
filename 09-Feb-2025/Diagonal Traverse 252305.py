# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans = []
        rows = len(mat)
        column = len(mat[0])
        r,c = 0,0
        up = True
        while len(ans) != (rows * column):
            if up:
                while r >= 0 and c <  column:
                    ans.append(mat[r][c])
                    r-=1
                    c+=1
                if(c == column):
                    c-=1
                    r+=2
                else:
                    r+=1
                up=False
            else:
                while r < rows and c >=0:
                    ans.append(mat[r][c])
                    c-=1
                    r+=1
                if(r == rows):
                    c+=2
                    r-=1
                else:
                    c+=1
                up=True
        return ans



        
        