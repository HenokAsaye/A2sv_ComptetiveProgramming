# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        even_positions = (n + 1) // 2  
        odd_positions = n // 2         
        even_count = pow(5, even_positions, MOD)  
        odd_count = pow(4, odd_positions, MOD)    
        return (even_count * odd_count) % MOD



        