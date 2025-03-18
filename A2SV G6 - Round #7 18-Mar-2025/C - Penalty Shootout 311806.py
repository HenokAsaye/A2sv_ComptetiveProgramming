# Problem: C - Penalty Shootout - https://codeforces.com/gym/596141/problem/C

t = int(input())

for _ in range(t):
    x = input().strip()

    a, b, c, d = 0, 0, 5, 5
    res = 10

    for i in range(10):
        if i % 2 == 0:
            if x[i] == '1' or x[i] == '?':
                a += 1
            c -= 1
        else:
            if x[i] == '1':
                b += 1
            d -= 1

        if a > b + d or b > a + c:
            res = min(res, i + 1)
            break

    a, b, c, d = 0, 0, 5, 5

    for i in range(10):
        if i % 2 == 0:
            if x[i] == '1':
                a += 1
            c -= 1
        else:
            if x[i] == '1' or x[i] == '?':
                b += 1
            d -= 1

        if a > b + d or b > a + c:
            res = min(res, i + 1)
            break

    print(res)
