# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree = [0] * n
        for u,v in edges:
            indegree[v] +=1
        champions = [i for i in range(n) if indegree[i] == 0]
        print(champions)
        return champions[0] if len(champions) == 1 else -1
        