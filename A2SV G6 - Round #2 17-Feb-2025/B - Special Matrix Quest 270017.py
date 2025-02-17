# Problem: B - Special Matrix Quest - https://codeforces.com/gym/586960/problem/B

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
summation = 0
middle = n // 2
for i in range(n):
    for j in range(n):
        if i == j:
            summation += grid[i][j]
        if i + j == n - 1:
            summation += grid[i][j]
        if i == middle:
            summation += grid[i][j]
        if j == middle:
            summation += grid[i][j]
summation -= grid[middle][middle] * 3
print(summation)