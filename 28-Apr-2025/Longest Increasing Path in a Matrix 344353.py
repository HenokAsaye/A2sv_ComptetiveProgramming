# Problem: Longest Increasing Path in a Matrix - https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        m,n = len(matrix),len(matrix[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        in_degree = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                for di,dj in directions:
                    ni,nj = i+di,j+dj
                    if((0 <= ni < m) and (0 <= nj <n)) and (matrix[ni][nj] > matrix[i][j]):
                        in_degree[ni][nj] += 1
        queue = deque()
        distance = [[1]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if(in_degree[i][j] == 0):
                    queue.append((i,j))
        max_length = 1
        while queue:
            i,j = queue.popleft()
            for di,dj in directions:
                ni,nj = i+di , j+dj
                if(0 <= ni < m) and (0 <= nj <n) and (matrix[ni][nj] > matrix[i][j]):
                    distance[ni][nj] = max(distance[ni][nj], distance[i][j]+1)
                    in_degree[ni][nj] -=1
                    if(in_degree[ni][nj] ==0):
                        queue.append((ni,nj))
            max_length = max(max_length,distance[i][j])
        return max_length
                
        