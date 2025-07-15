# Problem: Snakes and Ladders - https://leetcode.com/problems/snakes-and-ladders/

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def get_coordinates(square: int) -> tuple[int, int]:
            row_from_bottom = (square - 1) // n
            row = n - 1 - row_from_bottom
            col = (square - 1) % n
            if row_from_bottom % 2 == 1:  
                col = n - 1 - col
            return row, col
        visited = set()
        queue = deque([(1, 0)]) 
        while queue:
            square, moves = queue.popleft()
            for roll in range(1, 7): 
                next_square = square + roll
                if next_square > n * n:
                    continue
                row, col = get_coordinates(next_square)
                if board[row][col] != -1:
                    next_square = board[row][col]
                if next_square == n * n:
                    return moves + 1
                if next_square not in visited:
                    visited.add(next_square)
                    queue.append((next_square, moves + 1))

        return -1
