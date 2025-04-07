# Problem: Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def backtrack(start=0, path=[]):
            if len(path) == 4 and start == len(s):
                res.append(".".join(path))
                return
            if len(path) == 4:
                return
            for length in range(1, 4):  
                if start + length > len(s):
                    break
                part = s[start:start+length]
                if (part.startswith('0') and len(part) > 1) or int(part) > 255:
                    continue
                backtrack(start + length, path + [part])

        backtrack()
        return res
