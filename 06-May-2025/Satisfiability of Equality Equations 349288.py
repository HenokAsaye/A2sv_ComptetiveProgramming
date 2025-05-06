# Problem: Satisfiability of Equality Equations - https://leetcode.com/problems/satisfiability-of-equality-equations/

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = [i for i in range(26)]
        rank = [0] * 26
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x,y):
            rootx = find(x)
            rooty = find(y)

            if rootx != rooty:
                if (rank[rootx] < rank[rooty]):
                    parent[rooty]= rootx
                elif (rank[rooty] < rank[rootx]):
                    parent[rootx] = rooty
                else:
                    parent[rooty] = rootx
                    rank[rootx] +=1
        for i in equations:
            if i[1:3] == "==":
                x = ord(i[0]) - ord('a')
                y = ord(i[3]) - ord('a')
                union(x,y)
        for i in equations:
            if i[1:3] == "!=":
                x = ord(i[0]) - ord('a')
                y = ord(i[3]) - ord('a')
                if find(x) == find(y):
                    return False
        return True