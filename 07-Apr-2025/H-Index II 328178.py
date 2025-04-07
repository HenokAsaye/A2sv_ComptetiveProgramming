# Problem: H-Index II - https://leetcode.com/problems/h-index-ii/description/

class Solution:
    def hIndex(self, c: List[int]) -> int:
        l, r = 0, len(c)
        while l < r:
            m = (l + r) // 2
            if c[m] >= len(c) - m:
                r = m
            else:
                l = m + 1
        return len(c) - l

        