# Problem: Minimize Maximum of Array - https://leetcode.com/problems/minimize-maximum-of-array/

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        def is_possible(max_val: int) -> bool:
            total = 0
            for i, num in enumerate(nums):
                total += num
                if total > max_val * (i + 1):
                    return False
            return True
        
        left, right = 0, max(nums)
        while left < right:
            mid = (left + right) // 2
            if is_possible(mid):
                right = mid
            else:
                left = mid + 1
        return left