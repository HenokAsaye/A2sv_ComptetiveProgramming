# Problem: Squares of a Sorted Array
(Easy) - https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        list=[]
        for i in range(len(nums)):
            list.append((nums[i]**2))
        list.sort()
        return list
        