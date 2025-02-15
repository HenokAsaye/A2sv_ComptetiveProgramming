# Problem: Find the Index of the first occurence - https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
          if (needle == ""):
            return 0
          if (needle in haystack[:]):
            return haystack.index((needle))
          else:
            return -1