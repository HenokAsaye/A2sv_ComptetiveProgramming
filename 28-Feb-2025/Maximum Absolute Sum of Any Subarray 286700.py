# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int: 
        max_sum = 0
        min_sum = 0
        max_end = 0
        min_end = 0
        for j in range(len(nums)):
            max_end = max(nums[j], max_end + nums[j])  
            min_end = min(nums[j], min_end + nums[j])  
            max_sum = max(max_end, max_sum)
            min_sum = min(min_end, min_sum)
        return max(abs(min_sum),max_sum)






             