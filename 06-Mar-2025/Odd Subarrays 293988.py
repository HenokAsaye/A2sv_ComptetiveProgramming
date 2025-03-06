# Problem: Odd Subarrays - https://codeforces.com/problemset/problem/1686/B

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    i=0
    j=1
    count = 0
    while j < len(arr):
        if(arr[j] < arr[i]):
            count +=1
            j+=2
            i=j-1
        else:
            i+=1
            j+=1
    print(count)