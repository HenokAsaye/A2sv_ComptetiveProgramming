# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum= nums[0]
        ans = nums[0]
        for i in range(1,len(nums)):
            if(nums[i]+ current_sum > nums[i]):
                current_sum = nums[i] + current_sum
                ans = max(current_sum,ans)
            else:
                current_sum = nums[i]
                ans = max(current_sum,ans)
        return ans
         