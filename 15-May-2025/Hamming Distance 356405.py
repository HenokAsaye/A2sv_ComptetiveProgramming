# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x^y
        count = 0
        while z>0:
            if(z%2 == 1):
                count +=1
            z >>=1
        return count
        