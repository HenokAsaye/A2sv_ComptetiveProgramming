# Problem: 4Sum - https://leetcode.com/problems/4sum/

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                a, b = j + 1, len(nums) - 1
                while a < b:
                    sums = nums[i] + nums[j] + nums[a] + nums[b]
                    if sums > target:
                        b -= 1
                    elif sums < target:
                        a += 1
                    else:
                        result.append([nums[i], nums[j], nums[a], nums[b]])
                        while a < b and nums[a] == nums[a + 1]:
                            a += 1
                        while a < b and nums[b] == nums[b - 1]:
                            b -= 1
                        a += 1
                        b -= 1

        return result
