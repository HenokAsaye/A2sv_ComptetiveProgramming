# Problem: Red and Blue - https://codeforces.com/contest/1469/problem/B

t = int(input())
for i in range(t):
    y = int(input())
    m = list(map(int,input().split()))
    n = int(input())
    l = list(map(int,input().split()))
    max1 = 0
    max2 = 0
    x = 0
    z = 0
    for i in range(n):
        z += l[i]
        max2 = max(z,max2)
    for j in range(y):
        x+=m[j]
        max1 = max(x,max1)
    print(max1 + max2)