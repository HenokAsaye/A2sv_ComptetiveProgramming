# Problem: B - Kidus Couldn't Sleep - https://codeforces.com/gym/589822/problem/B

n,k = map(int,input().split())
arr = list(map(int,input().split()))
current = sum(arr[:k])
total_sum = current
for right in range(k,len(arr)):
    current += arr[right]-arr[right-k]
    total_sum += current
print(total_sum/(n-k+1))