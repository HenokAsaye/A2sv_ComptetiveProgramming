# Problem: Books - https://codeforces.com/contest/279/problem/B

t().split()))
arr =list(map(int,input().split()))
mx= 0
left = 0
summation =0
for right in range(n):
    summation +=arr[right]
    while summation > t:
        summation -=arr[left]
        left +=1
    count = (right -left +1)
    mx = max(count,mx)
print(mx)