# Problem: F - Covered Points Count - https://codeforces.com/gym/589822/problem/F


n = int(input())
intervals = []
points = set()
for _ in range(n):
    l, r = map(int, input().split())
    intervals.append((l, r))
    points.add(l)
    points.add(r + 1)
# print(intervals, "intervals")
points = sorted(points)
# print(points,"sorted_points")
compress = {point: idx for idx, point in enumerate(points)}
# print(compress,"compressed")
max_range = len(points)
diff = [0] * (len(points) + 1)
for l, r in intervals:
    diff[compress[l]] += 1
    diff[compress[r + 1]] -= 1
# print(diff)
for i in range(1, max_range):
    diff[i] += diff[i-1]
# print(diff,"diff")
ans = [0] * (n+1)
for i in range(len(points)-1):
    count = diff[i]
    if count > 0:
        length = points[i + 1] - points[i]
        ans[count] += length
print(" ".join(map(str,ans[1:])))