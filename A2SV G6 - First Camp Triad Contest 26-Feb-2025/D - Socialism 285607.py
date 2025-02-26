# Problem: D - Socialism - https://codeforces.com/gym/589822/problem/D

t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    
    arr.sort(reverse=True)  
    total = 0
    count = 0
    
    for i in range(n):
        total += arr[i]
        if total / (i + 1) >= x:
            count = i + 1
        else:
            break
    
    print(count)