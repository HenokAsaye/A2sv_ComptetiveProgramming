# Problem: Island Perimeter - https://leetcode.com/problems/island-perimeter/description/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = [[False for i in range(len(grid[0]))]for j in range(len(grid))]
        def inbound(row,col):
            return (0<=row< len(grid)) and (0<=col<len(grid[0]))
        perimeter = 0
        def dfs(grid,visited,row,col):
            nonlocal perimeter
            visited[row][col] = True
            for row_change,col_change in directions:
                new_row = row + row_change
                new_col =  col + col_change
                if not inbound(new_row,new_col) or grid[new_row][new_col] == 0:
                    perimeter +=1
                elif inbound(new_row,new_col) and not visited[new_row][new_col]:
                    dfs(grid,visited,new_row,new_col)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] ==1):
                    dfs(grid,visited,i,j)
                    return perimeter
        return 0
            

	
