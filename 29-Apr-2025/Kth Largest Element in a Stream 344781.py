# Problem: Kth Largest Element in a Stream - https://leetcode.com/problems/kth-largest-element-in-a-stream/

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heaps = []
        for num in nums:
            heapq.heappush(self.heaps,num)
            if (len(self.heaps) > k):
                heapq.heappop(self.heaps)
    def add(self, val: int) -> int:
        if len(self.heaps) < self.k:
            heapq.heappush(self.heaps,val)
        else:
            heapq.heappushpop(self.heaps,val)
        return self.heaps[0]

