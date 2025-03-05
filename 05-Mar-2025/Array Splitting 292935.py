# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C

n, k = map(int, input().split())
arr = list(map(int, input().split()))
ans = []
for i in range(n - 1):
    ans.append(arr[i + 1] - arr[i])
ans.sort(reverse=True)
total = arr[-1] - arr[0]
for i in range(k - 1):
    total -= ans[i]
print(total)