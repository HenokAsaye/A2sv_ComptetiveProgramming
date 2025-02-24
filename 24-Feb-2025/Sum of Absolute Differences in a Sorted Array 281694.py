# Problem: Sum of Absolute Differences in a Sorted Array - https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []
        prefix_sum = [nums[0]]
        for i in range(1,len(nums)):
            prefix_sum.append(prefix_sum[i-1]+nums[i])
        prefix_sum = [0] + prefix_sum + [0]
        for i in range(len(nums)):
            c_s = (nums[i] *i) - prefix_sum[i]
            m_d = (prefix_sum[-2] - prefix_sum[i+1]) - (nums[i] * (len(nums)-i-1))
            ans.append(c_s + m_d)
        return ans


