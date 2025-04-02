# Problem: Split Array Largest Sum - https://leetcode.com/problems/split-array-largest-sum/

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)
        ans = []
        while left <= right:
            mid = (left + right) // 2  
            summation = 0
            i = 0
            count = 1
            while i < len(nums):
                if summation + nums[i] > mid:  
                    count += 1
                    summation = 0
                summation += nums[i]
                i += 1
            if count >k :  
                left = mid + 1
            else:  
                ans.append(mid)
                right = mid - 1
        return min(ans)      




















        