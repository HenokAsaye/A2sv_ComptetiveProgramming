# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_count = {}
        for char in s1:
            char_count[char] = char_count.get(char, 0) + 1
        left = 0
        window_count = {}
        for right in range(len(s2)):
            if s2[right] in char_count:
                window_count[s2[right]] = window_count.get(s2[right], 0) + 1
            while right - left + 1 > len(s1):
                if s2[left] in window_count:
                    window_count[s2[left]] -= 1
                    if window_count[s2[left]] == 0:
                        del window_count[s2[left]]
                left += 1
            if window_count == char_count:
                return True
        
        return False