# Problem: Power of Four - https://leetcode.com/problems/power-of-four/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==1:
            return True
        y= 4
        while y < n:
            y = 4 * y
        if(y ==n):
            return True
        else:
            return False
