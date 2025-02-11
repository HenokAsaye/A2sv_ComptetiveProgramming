# Problem: H-Index - https://leetcode.com/problems/h-index/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        h_index = 0
        
        for i in range(n):
            if citations[i] >= n - i:  
                h_index = n - i
                break
        
        return h_index


        