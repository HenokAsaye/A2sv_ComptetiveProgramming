# Problem: E - Equalizing Arrays - https://codeforces.com/gym/588468/problem/E

n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))
 
if sum(arr1) != sum(arr2):
    print(-1)
    exit()
i, j = 0, 0
sum1, sum2 = 0, 0
ans = 0
while i < n and j < m:
    if sum1 < sum2:
        sum1 += arr1[i]
        i += 1
    elif sum1 > sum2:
        sum2 += arr2[j]
        j += 1
    else:
        if sum1 != 0:
            ans += 1
        if i < n:
            sum1 += arr1[i]
            i += 1
        if j < m:
            sum2 += arr2[j]
            j += 1
 
while i < n:
    sum1 += arr1[i]
    i += 1
while j < m:
    sum2 += arr2[j]
    j += 1
 
if sum1 == sum2 and sum1 != 0:
    ans += 1
 
print(ans)
