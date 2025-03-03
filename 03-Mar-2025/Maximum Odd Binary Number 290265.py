# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        x = list(map(int,s))
        ans = ''
        if(x.count(1) ==1):
            x.sort()
            return "".join(map(str,x))
        if(x.count(1) > 1):
            y = x.count(1)
            z = len(x) -y
            while y!=1:
                ans+="1"
                y-=1
            while z !=0:
                ans+="0"
                z-=1
            ans+="1"
        return ans
            
