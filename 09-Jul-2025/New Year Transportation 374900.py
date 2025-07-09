# Problem: New Year Transportation - https://codeforces.com/problemset/problem/500/A

def can_reach_cell(n, t, a):
    pos = 1
    while pos < t:
        pos = pos + a[pos - 1]
    return "YES" if pos == t else "NO"
 
 
n, t = map(int, input().split())
a = list(map(int, input().split()))
 
print(can_reach_cell(n, t, a))