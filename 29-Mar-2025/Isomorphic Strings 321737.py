# Problem: Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = defaultdict(int)
        for i in range(len(s)):
            dic[s[i]] = t[i]
        ans = [j for j in dic.values()]
        if(len(ans)!= len(set(ans))):
            return False
        else:
            for j in range(len(s)):
                if([s[j],dic[s[j]]] != [s[j],t[j]]):
                    return False
            return True

        