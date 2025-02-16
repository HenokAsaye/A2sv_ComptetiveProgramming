# Problem: Longest Palindromic Substring - https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        max_length = 0
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                current_length = 0
                h = s[i:j]
                if(h==h[::-1]):
                    c_len = len(h)
                if c_len > max_length:
                    max_length = c_len
                    ans=h
        return ans