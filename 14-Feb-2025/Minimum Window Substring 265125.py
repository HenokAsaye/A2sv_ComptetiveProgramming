# Problem: Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/submissions/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_elements = Counter(t)
        min_length = float("inf")
        temporary = defaultdict(int)
        i=0
        ans = ""
        for j in range(len(s)):
            if(s[j] in t_elements):
                temporary[s[j]] +=1
            while all(temporary[n] >= t_elements[n] for n in t_elements):
                if(j-i+1 < min_length):
                    min_length = j-i+1
                    ans = s[i:j+1]
                if(s[i] in temporary):
                    temporary[s[i]] -=1
                    if(temporary[s[i]] ==0):
                        del temporary[s[i]]
                i+=1
        return ans





        
