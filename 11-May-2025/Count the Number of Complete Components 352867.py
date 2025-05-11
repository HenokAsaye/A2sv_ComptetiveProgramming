# Problem: Count the Number of Complete Components - https://leetcode.com/problems/count-the-number-of-complete-components/

from typing import List
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        count = 0

        for i in range(n):
            if not visited[i]:
                queue = deque([i])
                visited[i] = True
                nodes = [i]
                edge_count = 0

                while queue:
                    node = queue.popleft()
                    for neighbor in graph[node]:
                        edge_count += 1
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
                            nodes.append(neighbor)
                edge_count //= 2
                k = len(nodes)
                if edge_count == k * (k - 1) // 2:
                    count += 1

        return count
