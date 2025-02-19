# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        shift_diff = [0] * (n + 1)
        for start, end, direction in shifts:
            if direction == 1:  
                shift_diff[start] += 1
                shift_diff[end + 1] -= 1
            else:  
                shift_diff[start] -= 1
                shift_diff[end + 1] += 1
        for i in range(1, n):
            shift_diff[i] += shift_diff[i - 1]
        result = []
        for i in range(n):
            shift = (ord(s[i]) - ord('a') + shift_diff[i]) % 26
            result.append(chr(ord('a') + shift))
        return ''.join(result)