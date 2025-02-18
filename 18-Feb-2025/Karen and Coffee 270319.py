# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

from collections import defaultdict
n, k, q = map(int, input().split())
max_temp = 200000  
arr1 = [0] *(max_temp+2)
for _ in range(n):
    i,j = (map(int,input().split()))
    arr1[i] +=1
    arr1[j+1] -=1
for i in range(1,len(arr1)):
    arr1[i] += arr1[i - 1] 
arr2 = [0] * len(arr1)
for i ,j in enumerate(arr1):
    if(j >=k):
        arr2[i] = 1
for i in range(1,len(arr2)):
    arr2[i] += arr2[i - 1] 
for _ in range(q):
    c,d = (map(int,input().split()))
    result = arr2[d] - arr2[c-1]
    print(result)