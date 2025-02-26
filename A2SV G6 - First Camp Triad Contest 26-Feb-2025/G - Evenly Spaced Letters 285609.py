# Problem: G - Evenly Spaced Letters - https://codeforces.com/gym/589822/problem/G


t = int(input())
for i in range(t):
    s = list(str(input()))
    s.sort()
    print("".join(s))