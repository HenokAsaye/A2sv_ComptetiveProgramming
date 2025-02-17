# Problem: Find Pivot Index - https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l = 0
        total = sum(nums)
        for i,j in enumerate(nums):
            if l == total - l-j :
                return i
            l+=j
        return -1

        