# Problem: F - Binary Substrings with Exactly k Ones - https://codeforces.com/gym/588468/problem/F

def at_most_k(s,k):
    if k < 0:
        return 0
    count = 0
    one = 0
    left = 0
    for right in range(len(s)):
        if(int(s[right])==1):
            count +=1
        while count > k:
            count -= (int(s[left]))
            left +=1
        one += right - left +1
    return one
k = int(input())
s = str(input())
print(at_most_k(s,k) - at_most_k(s,k-1))