# Problem: Destroying Bridges - https://codeforces.com/problemset/problem/1944/A

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    for s in range(1, n+1):
        cuts_needed = s * (n - s)
        if cuts_needed <= k:
            print(s)
            break
