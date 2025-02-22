# Problem: Number of Ways to Select Buildings - https://leetcode.com/problems/number-of-ways-to-select-buildings/

class Solution:
    def numberOfWays(self, s: str) -> int:
        n = len(s)
        count0 = [0] * (n + 1)
        count1 = [0] * (n + 1)

        for i in range(n):
            count0[i + 1] = count0[i] + (s[i] == '0')
            count1[i + 1] = count1[i] + (s[i] == '1')

        total_zeros = count0[n]
        total_ones = count1[n]
        valid_count = 0

        for j in range(1, n - 1):
            if s[j] == '0':
                valid_count += count1[j] * (total_ones - count1[j + 1])
            else:
                valid_count += count0[j] * (total_zeros - count0[j + 1])

        return valid_count
            