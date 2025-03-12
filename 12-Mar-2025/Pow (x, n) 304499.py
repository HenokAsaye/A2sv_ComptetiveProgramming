# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x,n):
            if(n==0):
                return 1
            y = power(x,n//2)
            v = y * y
            if(n%2):
                v = v * x
            return v
        ans = power(x,abs(n))
        return ans if n>=0 else 1/ans


            
     