# Problem: Couse Schedule - https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, pre: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for i in range(len(pre)):
            graph[pre[i][0]].append(pre[i][1])
        white = 1
        black = 2
        gray = 3
        color = {k: white for k in range(numCourses)}
        print(color[0])
        no_cycle = True
        def dfs(node):
            nonlocal no_cycle 
            color[node] = gray
            for neighbour in graph[node]:
                if(color[neighbour] == white):
                    dfs(neighbour)
                elif(color[neighbour] == gray):
                    no_cycle = False
            color[node] = black
        for i in range(numCourses):
            if color[i] == white:
                dfs(i)
        return no_cycle


        