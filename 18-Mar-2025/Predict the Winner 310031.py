# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def helper(left,right,turn):
            if left == right:
                return nums[left] if turn == 1 else 0
            if turn ==1:
                leftpick = nums[left] + helper(left+1,right,2)
                rightpick = nums[right] + helper(left,right-1,2)
                return max(leftpick,rightpick)
            else:
                leftpick = helper(left+1,right,1)
                rightpick = helper(left,right-1,1)
                return min(leftpick,rightpick)
        totalScore = sum(nums)
        ps = helper(0,len(nums)-1,1)
        return ps >= totalScore / 2