# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        prefix_sum = 0
        count_goal =0
        for i in nums:
            prefix_sum +=i
            if(prefix_sum-goal) in count:
                count_goal += count[prefix_sum-goal]
            count[prefix_sum] += 1
        return count_goal
        