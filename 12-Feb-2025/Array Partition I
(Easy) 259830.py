# Problem: Array Partition I
(Easy) - https://leetcode.com/problems/array-partition-i/

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        summation = 0
        i=0
        while i <= len(nums)-2:
            x = min(nums[i],nums[i+1])
            print(x)
            summation += x
            i+=2
        return summation