# Problem: Minimum Operations to Exceed Threshold Value II - https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        count = 0
        while nums[0] < k:
            if len(nums) < 2:
                break
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            new_val = x * 2 + y
            heapq.heappush(nums, new_val)
            count += 1
        
        return count