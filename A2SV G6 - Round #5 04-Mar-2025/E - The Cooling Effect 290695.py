# Problem: E - The Cooling Effect - https://codeforces.com/gym/591928/problem/E

import sys
t = int(input())
data = sys.stdin.read().splitlines()
index = 0
for _ in range(t):
    while not data[index]:
        index += 1
    n, k = map(int, data[index].split())
    index += 1
    while not data[index]:
        index += 1
    arr1 = list(map(int, data[index].split()))
    index += 1
    while not data[index]:
        index += 1
    arr2 = list(map(int, data[index].split()))
    index += 1
    inf = [float("inf")] * n
    for i in range(k):
        inf[arr1[i] - 1] = arr2[i]
    first = [float("inf")] * n
    first[0] = inf[0]
    for i in range(1, n):
        first[i] = min(first[i - 1] + 1, inf[i])
    second = [float("inf")] * n
    second[-1] = inf[-1]
    for i in range(n - 2, -1, -1):
        second[i] = min(second[i + 1] + 1, inf[i])
    ans = [min(first[i], second[i]) for i in range(n)]
    print(*ans)

    
