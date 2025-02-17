# Problem: Running Sum of 1d Array - https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            ans.append(sum(nums[:i+1]))
        return ans
        