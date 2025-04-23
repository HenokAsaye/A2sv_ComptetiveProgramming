# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        reverse_graph = defaultdict(list)
        in_degree = [0] * n
        for u in range(n):
            for v in (graph[u]):
                reverse_graph[v].append(u)
                in_degree[u] +=1
        print(in_degree)
        print(reverse_graph)
        queue = deque([i for i in range(n) if in_degree[i] == 0])
        safe = [False] * n
        while queue:
            node = queue.popleft()
            safe[node] = True
            for neighbor in reverse_graph[node]:
                in_degree[neighbor] -=1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        return [i for i, is_safe in enumerate(safe) if is_safe]
        