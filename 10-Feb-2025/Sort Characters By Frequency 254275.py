# Problem: Sort Characters By Frequency - https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        sorted_dic= sorted(count.items(),key=lambda x:x[1],reverse = True)
        y = dict(sorted_dic)
        z = []
        for i,j in y.items():
            while j>0:
                z.append(i)
                j-=1
        return "".join(z)