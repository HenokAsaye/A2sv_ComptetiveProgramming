# Problem: Largest Number - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        x = list(map(str,nums))
        for i in range(len(x)):
            for j in range(len(x)-i-1):
                if(int(x[j] + x[j+1])  < int(x[j+1] + x[j])):
                    x[j],x[j+1] = x[j+1],x[j]
        if(int("".join(x)) == 0):
            return "0"
        return "".join(x)
                