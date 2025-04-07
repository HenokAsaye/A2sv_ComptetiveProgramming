# Problem: N Queens - https://leetcode.com/problems/n-queens/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]
        cols = set()
        pos_diagonals = set()  
        neg_diagonals = set()  

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in cols or (r + c) in pos_diagonals or (r - c) in neg_diagonals:
                    continue
                board[r][c] = "Q"
                cols.add(c)
                pos_diagonals.add(r + c)
                neg_diagonals.add(r - c)
                backtrack(r + 1)
                board[r][c] = "."
                cols.remove(c)
                pos_diagonals.remove(r + c)
                neg_diagonals.remove(r - c)

        backtrack(0)
        return res
