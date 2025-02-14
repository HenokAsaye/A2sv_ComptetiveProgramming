# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    left = 0
    right = 0
    ans = []
    while right < n:
        if(arr[left] < 0):
            c_n = float("-inf")
            while  right < n and arr[right] < 0 :
                cn = arr[right]
                c_n = max(cn,c_n)
                right +=1
            ans.append(c_n)
            left = right
        elif(arr[left] >0):
            c_p = 0
            while  right < n and arr[right] >0:
                cp = arr[right]
                c_p = max(c_p,cp)
                right +=1
            ans.append(c_p)
            left = right
    print(sum(ans))



