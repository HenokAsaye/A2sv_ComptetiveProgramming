# Problem: F - Array Transformation - https://codeforces.com/gym/586960/problem/F

from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    freq = list(Counter(arr).values())
    candidates = sorted(set(freq))
    ans = float('inf')
    for c in candidates:
        removals = 0
        for f in freq:
            if f < c:
                removals += f
            else:
                removals += (f - c)
        ans = min(ans, removals)
    print(ans)
