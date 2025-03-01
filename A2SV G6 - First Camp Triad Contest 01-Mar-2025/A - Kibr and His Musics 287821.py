# Problem: A - Kibr and His Musics - https://codeforces.com/gym/589822/problem/A

n,m = (map(int,input().split()))
prefix_sum = [0] * (n+1)
arr = []
for i in range(n):
    a,b = (map(int,input().split()))
    arr.append(a*b)
x = 0
for i in range(len(arr)):
    x+=arr[i]
    prefix_sum[i+1] = x
 
array = list(map(int,input().split()))
k = 0
j = 0
while j < len(prefix_sum) and k < len(array):
    if(array[k] <= prefix_sum[j]):
        print(j)
        k+=1
    else:
        j+=1