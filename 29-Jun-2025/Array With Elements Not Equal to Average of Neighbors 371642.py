# Problem: Array With Elements Not Equal to Average of Neighbors - https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        left, right = 0, len(nums) - 1
        turn = True  # Start with the largest number (right)

        while left <= right:
            if turn:
                res.append(nums[right])
                right -= 1
            else:
                res.append(nums[left])
                left += 1
            turn = not turn

        return res
