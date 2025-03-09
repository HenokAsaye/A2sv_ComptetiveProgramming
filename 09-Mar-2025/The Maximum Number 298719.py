# Problem: The Maximum Number - https://leetcode.com/problems/third-maximum-number/description/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        x = list(set(nums))
        y = sorted(x)
        
        if(len(y)<3):
            return max(y)
        else:
            return y[-3]
        
        