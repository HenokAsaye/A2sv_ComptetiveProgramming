# Problem: Construct Smallest Number From DI String - https://leetcode.com/problems/construct-smallest-number-from-di-string/description/

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res = []
        stack = []
        num = 1

        for ch in pattern + 'I':  
            stack.append(str(num))
            num += 1

            if ch == 'I':
                while stack:
                    res.append(stack.pop())

        return ''.join(res)

        