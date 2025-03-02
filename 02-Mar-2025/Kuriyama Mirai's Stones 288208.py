# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B

n = int(input())
v = list(map(int,input().split()))
m = int(input())
unsorted_one = [v[0]]
for j in range(1, len(v)):
    unsorted_one.append(v[j] + unsorted_one[j - 1])
v.sort()
sorted_one = [v[0]]
for j in range(1, len(v)):
    sorted_one.append(v[j] + sorted_one[j - 1])
for i in range(m):
    t, l, r = map(int, input().split())
    if t == 1:
        result = unsorted_one[r - 1] - (unsorted_one[l - 2] if l > 1 else 0)
        print(result)
    elif t == 2:
        result = sorted_one[r - 1] - (sorted_one[l - 2] if l > 1 else 0)
        print(result)