# Problem: D - Repeating Cipher - https://codeforces.com/gym/585107/problem/D

t= int(input())
encrypt = str(input())
solution = ""
i=0
j=0
while i<t:
    solution +=encrypt[i]
    j+=1
    i=i+j
print(solution)