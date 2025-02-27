# Problem: Ways to Make a Fair Array - https://leetcode.com/problems/ways-to-make-a-fair-array/description/

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: 
            return 1
        prefix_even = [0] * (n + 1)
        prefix_odd = [0] * (n + 1)
        for i in range(n):
            prefix_even[i + 1] = prefix_even[i] + (nums[i] if i % 2 == 0 else 0)
            prefix_odd[i + 1] = prefix_odd[i] + (nums[i] if i % 2 != 0 else 0)
        count = 0
        for j in range(n):
            left_even = prefix_even[j]
            left_odd = prefix_odd[j]
            right_even = prefix_odd[n] - prefix_odd[j + 1]
            right_odd = prefix_even[n] - prefix_even[j + 1]

            if left_even + right_even == left_odd + right_odd:
                count += 1

        return count





