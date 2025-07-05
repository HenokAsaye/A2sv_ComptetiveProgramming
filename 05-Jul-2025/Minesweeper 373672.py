# Problem: Minesweeper - https://leetcode.com/problems/minesweeper/

from typing import List

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1),  (1, 0), (1, 1)]
        
        def countMines(x: int, y: int) -> int:
            count = 0
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] == 'M':
                    count += 1
            return count
        
        def dfs(x: int, y: int):
            if not (0 <= x < len(board) and 0 <= y < len(board[0])) or board[x][y] != 'E':
                return
            
            mines = countMines(x, y)
            if mines > 0:
                board[x][y] = str(mines)
            else:
                board[x][y] = 'B'
                for dx, dy in directions:
                    dfs(x + dx, y + dy)
        
        x, y = click
        if board[x][y] == 'M':
            board[x][y] = 'X'
        else:
            dfs(x, y)
        
        return board
