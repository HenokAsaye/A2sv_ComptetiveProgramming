# Problem: Strange Printer II - https://leetcode.com/problems/strange-printer-ii/

class Solution:
    def isPrintable(self, matrix: List[List[int]]) -> bool:
        color_react = {}
        m,n = len(matrix) , len(matrix[0])

        for i in range(m):
            for j in range(n):
                color = matrix[i][j]
                if color not in color_react:
                    color_react[color] = [i,i,j,j]
                else:
                    color_react[color][0] = min(color_react[color][0],i)
                    color_react[color][1] = max(color_react[color][1],i)
                    color_react[color][2] = min(color_react[color][2],j)
                    color_react[color][3] = max(color_react[color][3],j)
        graph = defaultdict(set)
        in_degree = defaultdict(int)
        for color in color_react:
            min_row, max_row, min_col, max_col = color_react[color]
            for i in range(min_row,max_row+1):
                for j in range(min_col,max_col+1):
                    other_color = matrix[i][j]
                    if other_color != color:
                        if color not in graph[other_color]:
                            graph[other_color].add(color)
                            in_degree[color] +=1
        queue = []
        for color in color_react:
            if in_degree.get(color,0) == 0:
                queue.append(color)

        processed = 0
        while queue:
            current = queue.pop(0)
            processed +=1
            for neighbor in graph.get(current,set()):
                in_degree[neighbor] -=1
                if(in_degree[neighbor] == 0):
                    queue.append(neighbor)
        return processed == len(color_react)

                    




        