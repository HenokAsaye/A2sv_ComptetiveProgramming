# Problem: Reverse Words in a String - https://leetcode.com/problems/reverse-words-in-a-string/

class Solution:
    def reverseWords(self, s: str) -> str:
        h = list(map(str,s.split()))
        return " ".join(h[::-1])
        