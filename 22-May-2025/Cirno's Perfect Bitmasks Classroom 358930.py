# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

t = int(input())
for i in range(t):
    given = int(input())
    littlebit = (given & (-given))
    if(given == 1):
        print(3)
    elif((littlebit ^ given) == 0):
        print(littlebit+1)
    else:
        print(littlebit)
