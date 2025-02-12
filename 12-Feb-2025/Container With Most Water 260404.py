# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        p=0
        l=len(height)-1
        max_area=0
        while l>=p:
            if(height[p]<=height[l]):
                current_max = height[p] * (abs(l-p))
                p+=1
            else:
                current_max = height[l] * (abs(l-p))
                l-=1
            max_area=max(current_max,max_area)
        return max_area