# Problem: Possible Bipartition - https://leetcode.com/problems/possible-bipartition/

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        from collections import defaultdict
        graph = defaultdict(list)
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        color = {}
        def dfs(person, c):
            if person in color:
                return color[person] == c
            color[person] = c
            return all(dfs(nei, -c) for nei in graph[person])
        for person in range(1, n + 1):
            if person not in color:
                if not dfs(person, 1):
                    return False
        return True
