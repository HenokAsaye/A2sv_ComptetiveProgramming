# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        indexed_tasks = [(et, pt, i) for i, (et, pt) in enumerate(tasks)]
        indexed_tasks.sort()

        res = []
        heap = []
        time = 0
        i = 0
        n = len(tasks)

        while len(res) < n:
            while i < n and indexed_tasks[i][0] <= time:
                et, pt, idx = indexed_tasks[i]
                heapq.heappush(heap, (pt, idx))
                i += 1

            if heap:
                pt, idx = heapq.heappop(heap)
                time += pt
                res.append(idx)
            else:
                time = indexed_tasks[i][0]

        return res

        