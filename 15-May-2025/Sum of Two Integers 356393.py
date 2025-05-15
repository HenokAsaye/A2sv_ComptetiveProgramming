# Problem: Sum of Two Integers - https://leetcode.com/problems/sum-of-two-integers/description/

class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF  # 32 bits mask
        INT_MAX = 0x7FFFFFFF  # Max positive int for 32 bits

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & MASK
            b = carry & MASK

        # if a is greater than INT_MAX, it means a is negative in 32-bit signed int
        return a if a <= INT_MAX else ~(a ^ MASK)
