# Problem: Maximum Average Subarray I  - https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = sum(nums[0:k])
        max_sum = current_sum
        for i in range(0,len(nums)-k):
            current_sum = current_sum - nums[i] + nums[i+k]
            max_sum = max(max_sum,current_sum)
        max_average = max_sum /k
        return max_average



        