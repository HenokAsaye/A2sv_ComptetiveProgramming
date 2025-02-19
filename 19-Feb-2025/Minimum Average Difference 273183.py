# Problem: Minimum Average Difference - https://leetcode.com/problems/minimum-average-difference/

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        if(len(nums)==0):
            return 0
        prefix_sum = [nums[0]]
        for i in range(1,len(nums)):
            prefix_sum.append(nums[i]+prefix_sum[i-1])
        prefix_sum = prefix_sum
        n=len(prefix_sum)
        print(prefix_sum)
        minimum = float("inf")
        m_index = 0
        for j in range(len(prefix_sum)):
            left = prefix_sum[j] // (j+1)
            if j != n - 1: right = (prefix_sum[n-1]-prefix_sum[j])//(n-j-1)
            else: right = 0
            c_d = abs(left - right)
            if(minimum > c_d):
                minimum = c_d
                m_index = j
        return m_index


