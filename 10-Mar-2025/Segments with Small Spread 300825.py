# Problem: Segments with Small Spread - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/F

from collections import deque
n,s = map(int,input().split())
arr = list(map(int,input().split()))
left = 0
min_q = deque()
max_q = deque()
ans = 0
for right in range(len(arr)):
    while min_q and min_q[-1] > arr[right]:
        min_q.pop()
    while max_q and max_q[-1] < arr[right]:
        max_q.pop()
    max_q.append(arr[right])
    min_q.append(arr[right])
    while max_q[0] - min_q[0] > s:
        if arr[left] == max_q[0]:
            max_q.popleft()
        if(arr[left] == min_q[0]):
            min_q.popleft()
        left+=1
    ans += right-left +1
print(ans)