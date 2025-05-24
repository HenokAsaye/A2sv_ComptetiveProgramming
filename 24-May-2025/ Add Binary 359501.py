# Problem:  Add Binary - https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a,2)
        b = int(b,2)
        return (str(bin(a+b))[2:])

        