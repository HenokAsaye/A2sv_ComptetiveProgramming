# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows, cols = len(isWater), len(isWater[0])
        height = [[-1 for _ in range(cols)] for _ in range(rows)]
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if isWater[r][c] == 1:
                    height[r][c] = 0
                    q.append((r, c))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  

        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and height[nr][nc] == -1:
                    height[nr][nc] = height[r][c] + 1
                    q.append((nr, nc))

        return height
