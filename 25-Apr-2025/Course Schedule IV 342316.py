# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        for pre,course in prerequisites:
            graph[pre].append(course)
            in_degree[course] +=1
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        order = []
        while queue:
            course = queue.popleft()
            order.append(course)
            for neighbor in graph[course]:
                in_degree[neighbor] -=1
                if(in_degree[neighbor] == 0):
                    queue.append(neighbor)
        if(len(order) != numCourses):
            return []
        print(order)
        print(graph)
        def dfs(node, graph, visited):
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor, graph, visited)
            return visited
        result = {}
        for node in graph:
            visited = dfs(node, graph, set())
            result[node] = list(visited)
        print(result,"result")
        ans = []
        if(len( prerequisites) ==0):
            for i in range(len(queries)):
                ans.append(False)
            return ans
        for i,j in queries:
            if((order.index(i) < order.index(j))and (j) in result[i]):
                ans.append(True)
            
            else:
                ans.append(False)
        return ans

        