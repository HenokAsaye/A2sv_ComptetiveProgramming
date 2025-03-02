# Problem: E - Tv Off - https://codeforces.com/gym/589822/problem/E

n = int(input())
intervals = []
points = set()
for _ in range(n):
    l, r = map(int, input().split())
    intervals.append((l, r))
    points.add(l)
    points.add(r + 1)
points = sorted(points)
compress = {point: idx for idx, point in enumerate(points)}
max_range = len(points)
m = [0] * (max_range)
for l, r in intervals:
    m[compress[l]] += 1
    if (r + 1) in compress:
        m[compress[r + 1]] -= 1
prefix_sum = [0] * max_range
prefix_sum[0] = m[0]
for i in range(1, max_range):
    prefix_sum[i] = prefix_sum[i - 1] + m[i]
a = [1 if prefix_sum[i] == 1 else 0 for i in range(max_range)]
pref = [0] * max_range
pref[0] = a[0]
for i in range(1, max_range):
    pref[i] = pref[i - 1] + a[i]
 
def range_sum(l_idx, r_idx):
    if l_idx == 0:
        return pref[r_idx]
    else:
        return pref[r_idx] - pref[l_idx - 1]
ans = -1
for k, (l, r) in enumerate(intervals):
    l_idx = compress[l]
    r_idx = compress[r + 1] - 1 if (r + 1) in compress else max_range - 1
    if range_sum(l_idx, r_idx) == 0:
        ans = k + 1  
        break
print(ans)