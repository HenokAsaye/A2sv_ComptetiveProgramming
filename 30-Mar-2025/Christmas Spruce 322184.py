# Problem: Christmas Spruce - https://codeforces.com/contest/913/problem/B

from collections import defaultdict
n = int(input())
arr = []
for i in range(1,n):
    a = int(input())
    arr.append(a)
dic = defaultdict(list)
for i in range(2,n+1):
    dic[arr[i-2]].append(i)
# print(dic)
flag = True
for j in dic:
    count = 0
    child = dic[j]
    for c in child:
        if c in arr:
            count +=1
    if(len(child) - count) < 3:
        flag = False
        break
if(flag):
    print("Yes")
else:
    print("No")
    
    
