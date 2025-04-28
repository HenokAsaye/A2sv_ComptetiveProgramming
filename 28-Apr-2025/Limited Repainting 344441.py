# Problem: Limited Repainting - https://codeforces.com/contest/2070/problem/C

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    a = list(map(int, input().split()))
    if k == 0:
        ans = 0
        for ai, ci in zip(a, s):
            if ci == 'B':
                ans = max(ans, ai)
        print(ans)
        continue
    def can(X):
        ops = 0
        in_block = False
        for ci, ai in zip(s, a):
            if ai > X and ci == 'R':
                in_block = False
            elif ai > X and ci == 'B':
                if not in_block:
                    ops += 1
                    in_block = True
        return ops <= k
    low, high = 0, max(a)
    ans = high
    while low <= high:
        mid = (low + high) // 2
        if can(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    print(ans)

