# Problem: B. Ehab Is an Odd Person - https://codeforces.com/problemset/problem/1174/B

t = int(input())
arr = list(map(int,input().split()))
y = sorted(arr)
count_even = 0
count_odd = 0
for i in range(t):
    if(arr[i] %2 ==0):
        count_even +=1
    else:
        count_odd +=1
if ((count_even) == len(arr)):
    print(*arr)
elif((count_odd) == len(arr)):
    print(*arr)
else:
    print(*y)

 