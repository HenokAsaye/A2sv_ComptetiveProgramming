# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr = nums[-1]
        for i in range(len(nums)-1,-1,-1):
            if nums[i] + i >= curr:
                curr = i
        if curr ==0:
            return True
        else:
            return False




        
'''
[4,3,2,1,0]


[4,3,2,1,0]

'''