# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1 for _ in range(len(graph))]
        def dfs(node,graph):
            temp = True
            for neighbour in graph[node]:
                if(color[neighbour] == -1):
                    if(color[node] == 0):
                        color[neighbour] = 1
                    else:
                        color[neighbour] = 0
                    temp = temp and dfs(neighbour,graph)
                else:
                    if(color[neighbour] == color[node]):
                        return False
            return temp
        result = True
        for node in range(len(graph)):
            if(color[node] == -1):
                color[node] = 0
                result = result and dfs(node,graph)
        return result



