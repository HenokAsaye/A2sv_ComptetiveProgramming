# Problem: Boats to Save People - https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, nums: List[int], limit: int) -> int:
        nums.sort()
        boats = 0
        i=0
        j=len(nums)-1
        if(sum(nums) < limit):
            return 1
        while i<j:
            if(nums[j] == limit):
                boats +=1
                j-=1
            if(nums[i]+nums[j] <= limit):
                boats +=1
                i+=1
                j-=1
            else:
                boats +=1
                j-=1
        if(i==j):
            boats +=1
        return boats