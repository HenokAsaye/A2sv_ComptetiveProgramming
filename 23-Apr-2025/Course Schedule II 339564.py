# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        for course,pre in prerequisites:
            graph[pre].append(course)
            in_degree[course] +=1
        print(in_degree)
        print(graph)
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
        return order

        