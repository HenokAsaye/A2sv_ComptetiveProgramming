# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        def factorial(n):
            if n==0:
                return 1
            return n * factorial(n-1)
        x = (factorial(n))
        count = 0
        while x >=10:
            if(x%10==0):
                count +=1
                x = x//10
            else:
                return count
        return count



