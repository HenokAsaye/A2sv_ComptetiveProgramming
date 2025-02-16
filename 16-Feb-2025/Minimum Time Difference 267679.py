# Problem: Minimum Time Difference - https://leetcode.com/problems/minimum-time-difference/

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        nums = []
        for k in timePoints:
            x, m = map(int, k.strip().split(":"))
            nums.append([x, [x, m]])
        nums.sort()
        print(nums)
        min_diff = float("inf")
        for i in range(len(nums) - 1):
            if nums[i][0] == nums[i + 1][0]:  #
                current_diff = abs(nums[i + 1][1][1] - nums[i][1][1])
            else:  
                hour_diff = abs(nums[i + 1][1][0] - nums[i][1][0]) * 60
                minute_diff = (nums[i + 1][1][1] - nums[i][1][1])
                current_diff = hour_diff + minute_diff
            min_diff = min(min_diff, current_diff)
        first_time = nums[0][0] * 60 + nums[0][1][1]
        last_time = nums[-1][0] * 60 + nums[-1][1][1]
        circular_diff = (1440 - last_time) + first_time
        min_diff = min(min_diff, circular_diff)

        return min_diff
