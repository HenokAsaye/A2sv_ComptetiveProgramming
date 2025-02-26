# Problem: C - Restoring to the Original - https://codeforces.com/gym/589822/problem/C

n = int(input())
s = list(str(input()))
j = "z"
k = "n"
count_1 = 0
count_0 = 0
for i in range(len(s)):
    if(s[i] == j):
        count_0 +=1
    elif(s[i] == k):
        count_1 +=1
print('1 ' * count_1 + '0 ' * count_0)