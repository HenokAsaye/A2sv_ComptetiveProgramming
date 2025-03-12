# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def inverse(s):
            z = []
            for i in range(len(s)):
                if(s[i]=="0"):
                    z.append("1")
                else:
                    z.append("0")
            return "".join(z)
        def reverse(s):
            return s[::-1]
        def generator(n):
            if(n==1):
                return "0"
            return generator(n-1) + "1" + reverse(inverse(generator(n-1)))
        return generator(n)[k-1]

            

        



        