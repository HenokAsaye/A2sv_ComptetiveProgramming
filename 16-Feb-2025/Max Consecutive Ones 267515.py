# Problem: Max Consecutive Ones - https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        i=0
        count =0
        while i < len(nums):
            if(nums[i] ==1):
                count +=1
                max_count= max(count,max_count)
            else:
                count =0
            i+=1
        return max_count

