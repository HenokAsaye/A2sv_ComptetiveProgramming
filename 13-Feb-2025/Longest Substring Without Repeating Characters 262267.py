# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s)==0):
            return 0
        max_distance = 1
        left=0
        h=set()
        for right in range(0,len(s)):
            while(s[right] in h):
                h.remove(s[left])
                left+=1
            h.add(s[right])
            max_distance=max(max_distance,right-left+1)
        return max_distance

  