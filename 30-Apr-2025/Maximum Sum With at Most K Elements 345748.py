# Problem: Maximum Sum With at Most K Elements - https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/description/

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        heaps = []
        for i in range(len(grid)):
            for _ in range(min(limits[i], len(grid[i]))):
                row_max = max(grid[i])
                heapq.heappush(heaps, -row_max)
                grid[i].remove(row_max)
        sum = 0
        while k>0:
            sum +=abs(heapq.heappop(heaps)) 
            k-=1
        return sum

        