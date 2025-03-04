# Problem: D - Life Across the Stars - https://codeforces.com/gym/591928/problem/D

n = int(input())  
intervals = []    
points = set()
for _ in range(n):
    b, d = map(int, input().split())
    intervals.append((b, d))
    points.add(b)
    points.add(d)  
points = sorted(points)
compress = {point: idx for idx, point in enumerate(points)}
max_range = len(points)
m = [0] * (max_range)
for b, d in intervals:
    m[compress[b]] += 1
    if d in compress:
        m[compress[d]] -= 1  
prefix_sum = [0] * max_range
prefix_sum[0] = m[0]
for i in range(1, max_range):
    prefix_sum[i] = prefix_sum[i - 1] + m[i]
x = max(prefix_sum)
y = prefix_sum.index(x)
print(points[y], x)