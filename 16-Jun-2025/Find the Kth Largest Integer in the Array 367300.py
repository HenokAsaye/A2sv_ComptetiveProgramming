# Problem: Find the Kth Largest Integer in the Array - https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        x = [-int(i) for i in nums]
        heapq.heapify(x)
        while k!=1:
            heapq.heappop(x)
            k-=1
        return (str(-heapq.heappop(x)))


        