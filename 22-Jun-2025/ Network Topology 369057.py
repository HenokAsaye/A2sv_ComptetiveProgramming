# Problem:  Network Topology - https://codeforces.com/problemset/problem/292/B

from collections import defaultdict

n,m = map(int,input().split())
graph = [[] for i in range(n+1)]

for i in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
one = 0
two =0
centered = 0
valid = True
for i in range(1,n+1):
    if m == n-1:
        if(len(graph[i]) == 1):
            one += 1
        elif(len(graph[i]) == 2):
            two +=1
        elif(len(graph[i]) == n-1):
            centered +=1
        else:
            valid = False
            break
    elif m==n:
        if(len(graph[i]) != 2):
            valid = False
            break
        else:
            two += 1
    else:
        valid = False
        break
if(m==n-1 and two == n-2 and one == 2 and valid):
    print("bus topology")
elif(m==n and two ==n and valid):
    print("ring topology")
elif(m==n-1 and centered == 1 and one == n-1):
    print("star topology")
else:
    print("unknown topology")

 
    

        