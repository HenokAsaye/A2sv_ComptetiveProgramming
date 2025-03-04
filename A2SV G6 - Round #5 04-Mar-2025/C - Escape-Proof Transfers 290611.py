# Problem: C - Escape-Proof Transfers - https://codeforces.com/gym/591928/problem/C

n,t,c = (map(int,input().split()))
arr = list(map(int,input().split()))
ans = 0
left = 0 
for right in range(n):
    if arr[right] > t:
        left = right + 1
    c_l =  right - left +1
    if c_l >=c:
        ans +=1
print(ans)