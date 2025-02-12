# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = defaultdict(int)
        for i in range(len(s)):
            count[s[i]] = i  
        ans = []
        size = 0
        end = 0
        for i in range(len(s)):
            end = max(end,count[s[i]])
            size+=1
            if(i == end):
                ans.append(size)
                size=0
        return ans

