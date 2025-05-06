# Problem: Spanning Tree - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/E

n,m = map(int,input().split())
graph = []
for i in range(m):
    row = list(map(int,input().split()))
    graph.append(row)
graph = sorted(graph, key=lambda x:x[2])
# print(graph)
parent = [i for i in range(n+1)]
rank = [0] * (n+1)
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
def union(x,y):
    rootx = find(x)
    rooty = find(y)

    if(rootx != rooty):
        if rank[rootx] < rank[rooty]:
            parent[rooty] = rootx
        elif rank[rooty] < rank[rootx]:
            parent[rootx] = rooty
        else:
            parent[rooty] = rootx
            rank[rootx] +=1
total_weight = 0
for u,v,w in graph:
    if find(u) != find(v):
        total_weight += w
        union(u,v)
print(total_weight)