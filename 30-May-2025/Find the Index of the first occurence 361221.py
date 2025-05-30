# Problem: Find the Index of the first occurence - https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        n = len(needle)
        
        for i in range(len(haystack) - n + 1):
            if haystack[i:i+n] == needle:
                return i
        
        return -1