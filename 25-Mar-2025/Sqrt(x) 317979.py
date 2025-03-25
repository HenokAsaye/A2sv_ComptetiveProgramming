# Problem: Sqrt(x) - https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x 
        #  0 1 2 3 4 5 6 7 8
        if (x==0):
            return 0
        elif(x==1):
            return 1
        else:
            while left < right:
                mid = (left + right) //2
                if(mid ** 2 < x):
                    left = mid +1 
                elif(mid**2 > x):
                    right = mid
                else:
                    return mid
            return left-1
        