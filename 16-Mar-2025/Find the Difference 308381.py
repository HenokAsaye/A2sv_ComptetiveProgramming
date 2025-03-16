# Problem: Find the Difference - https://leetcode.com/problems/find-the-difference/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for i in t:
            if(i not in s):
                return i
            elif((s.count(i))< (t.count(i))):
                return i
        