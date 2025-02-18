# Problem: Maximum Sum Obtained of Any Permutation - https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        prefix_sum = [0] * (len(nums)+1)
        for i,j in requests:
            prefix_sum[i]+=1
            prefix_sum[j+1] -=1
        for i in range(1,len(prefix_sum)):
            prefix_sum[i]+=prefix_sum[i-1]
        print(prefix_sum)
        ans = []
        prefix_sum.sort(reverse=True)
        nums.sort(reverse = True)
        for _ in range(len(nums)):
            ans.append(prefix_sum[_]*nums[_])
        return sum(ans)%(10**9+7)