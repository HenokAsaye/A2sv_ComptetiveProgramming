# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = defaultdict(list)
        for rich, poor in richer:
            graph[poor].append(rich)
        answer = [-1] * n
        def dfs(x):
            if answer[x] != -1:
                return answer[x]
            min_person = x
            for richer_person in graph[x]:
                candidate = dfs(richer_person)
                if quiet[candidate] < quiet[min_person]:
                    min_person = candidate
            answer[x] = min_person
            return min_person
        for i in range(n):
            dfs(i)
        return answer
