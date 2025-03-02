# Problem: D - Bernabas and the Harmonious Melody - https://codeforces.com/gym/588468/problem/D

def deletion_count(d):
    i,j = 0 , n-1
    deleted = 0
    while i < j:
        if(arr[i] != arr[j]):
            if(arr[i] == d):
                deleted+=1
                i+=1
            elif(arr[j]==d):
                deleted+=1
                j-=1
            else:
                return float("inf")
        else:
            i+=1
            j-=1
    return deleted
t = int(input())
for k in range(t):
    n = int(input())
    arr = input()
    i,j = 0,n-1
    palindrome = True
    while i < j:
        if(arr[i] != arr[j]):
            palindrome = False
            break
        i+=1
        j-=1
    if(palindrome):
        print(0)
    else:
        d1 = deletion_count(arr[i])
        d2 = deletion_count(arr[j])
        ans =  min(d1,d2)
        print(ans if ans != float("inf") else -1)
