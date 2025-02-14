# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

from collections import defaultdict
n,m = (map(int,input().split()))
arr = list(map(int,input().split()))
current = defaultdict(int)
mx_length = 0
count = 0
ans = [0,1]
left = 0
for right in range(len(arr)):
    current[arr[right]]+=1
    while (len(current) > m):
        current[arr[left]]-=1
        if(current[arr[left]] == 0):
            del current[arr[left]]
        left +=1
    count = right - left +1
    if (count > mx_length):
        mx_length= count
        ans[0] = left +1
        ans[1] = right +1
print(*ans)

