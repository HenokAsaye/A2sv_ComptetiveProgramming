# Problem: E - From S To T - https://codeforces.com/gym/585107/problem/E

from collections import Counter
q = int(input())
for _ in range(q):
    s = input().strip()
    t = input().strip()
    p = input().strip()
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    if i != len(s):
        print("NO")
        continue
    count_s = Counter(s)
    count_t = Counter(t)
    count_p = Counter(p)
    possible = True
    for char in count_t:
        if count_t[char] > count_s.get(char, 0):
            required = count_t[char] - count_s.get(char, 0)
            if count_p.get(char, 0) < required:
                possible = False
                break
    if possible:
        print("YES")
    else:
        print("NO")
