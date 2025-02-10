# Problem: X-Sum - https://codeforces.com/problemset/problem/1676/D

t = int(input())
 
for _ in range(t):
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    diag1 = {} 
    diag2 = {}  
    for i in range(n):
        for j in range(m):
            d1, d2 = i - j, i + j
            diag1[d1] = diag1.get(d1, 0) + grid[i][j]
            diag2[d2] = diag2.get(d2, 0) + grid[i][j]
 
    max_sum = 0
    for i in range(n):
        for j in range(m):
            d1, d2 = i - j, i + j
            current_sum = diag1[d1] + diag2[d2] - grid[i][j]
            max_sum = max(max_sum, current_sum)
    
    print(max_sum)