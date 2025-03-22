# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        def feb(n):
            if n==0:
                return 0
            elif n==1 or n==2:
                return 1
            y = feb(n-1) + feb(n-2)
            return y
        return feb(n)



    