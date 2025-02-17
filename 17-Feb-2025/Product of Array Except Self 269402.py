# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * (len(nums) + 1)
        suffix = [1] * ((len(nums) + 1))
        for i in range(len(nums)):
            prefix[i + 1] = nums[i] * prefix[i]
        print(prefix)
        for i in range(len(nums)-1,-1,-1):
            suffix[i] = nums[i] * suffix[i+1]
        print(suffix)
        for i in range(len(nums)):
            nums[i] = prefix[i] * suffix[i+1]
        return nums











