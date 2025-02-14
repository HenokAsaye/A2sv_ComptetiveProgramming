# Problem: Segment with Small Sum - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/A

n,m = (map(int,input().split()))
arr =list(map(int,input().split()))
length = 0
left = 0
c_s = 0
ans = 0
for i in range(len(arr)):
    c_s +=arr[i]
    while c_s >m:
        c_s -= arr[left]
        left+=1
    length = i-left +1
    ans = max(ans, length)
print(ans)
    


    




