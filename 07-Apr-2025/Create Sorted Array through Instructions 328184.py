# Problem: Create Sorted Array through Instructions - https://leetcode.com/problems/create-sorted-array-through-instructions/

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        mod = 10**9 + 7
        mx = max(instructions)
        bit = [0] * (mx + 2)
        
        def update(i):
            while i <= mx + 1:
                bit[i] += 1
                i += i & -i

        def query(i):
            res = 0
            while i > 0:
                res += bit[i]
                i -= i & -i
            return res

        res = 0
        for i, x in enumerate(instructions):
            left = query(x - 1)
            right = i - query(x)
            res = (res + min(left, right)) % mod
            update(x)
        return res
