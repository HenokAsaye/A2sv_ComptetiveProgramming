# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heaps = []
        for i in range(len(heights) - 1):
            if  heights[i + 1] - heights[i] > 0:
                heapq.heappush(heaps,  heights[i + 1] - heights[i])
            if len(heaps) > ladders:
                bricks -= heapq.heappop(heaps)
            if bricks < 0:
                return i
        return len(heights) - 1
